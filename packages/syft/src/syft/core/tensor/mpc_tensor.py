# stdlib
from functools import lru_cache
from functools import reduce
import operator

# third party
import numpy as np

# syft absolute
from syft.core.tensor.passthrough import PassthroughTensor
from syft.core.tensor.share_tensor import ShareTensor
from syft.core.tensor.tensor import Tensor


def is_pointer(val):
    if "Pointer" in type(val).__name__:
        return True


class MPCTensor(PassthroughTensor):
    def __init__(
        self,
        parties=None,
        secret=None,
        shares=None,
        shape=None,
        seed_shares=None
    ):
        if secret is None and shares is None:
            raise ValueError("Secret or shares should be populated!")

        if seed_shares is None:
            seed_shares = 42

        if secret is not None:
            shares = MPCTensor._get_shares_from_secret(
                secret=secret,
                parties=parties,
                shape=shape,
                seed_shares=seed_shares,
            )

        res = MPCTensor._mpc_from_shares(shares, parties)
        self.mpc_shape = shape

        super().__init__(res)

    @staticmethod
    def _mpc_from_shares(shares, parties):
        if not isinstance(shares, list):
            raise ValueError("_mpc_from_shares expected a list of shares")

        if is_pointer(shares[0]):
            # Remote shares
            return shares
        else:
            MPCTensor._mpc_from_local_shares(shares, parties)

    @staticmethod
    def _mpc_from_local_shares(shares, parties):
        # TODO: ShareTensor needs to have serde serializer/deserializer
        shares_ptr = [share.send(party) for share, party in zip(shares, parties)]
        return shares_ptr

    @staticmethod
    def _get_shares_from_secret(secret, parties, shape, seed_shares):
        if is_pointer(secret):
            if shape is None:
                raise ValueError("Shape must be specified when the secret is remote")
            return MPCTensor._get_shares_from_remote_secret(
                secret, shape, parties, seed_shares
            )

        return MPCTensor._get_shares_from_local_secret(secret, nr_parties=len(parties))

    @staticmethod
    def _get_shares_from_remote_secret(secret, shape, parties, seed_shares):
        shares = []
        for i, party in enumerate(parties):
            if party == secret.client:
                value = secret
            else:
                value = None

            remote_share = (
                party.syft.core.tensor.share_tensor.ShareTensor.generate_przs(
                    rank=i,
                    nr_parties=len(parties),
                    value=value,
                    shape=shape,
                    seed_shares=seed_shares,
                )
            )

            shares.append(remote_share)

        return shares

    @staticmethod
    def _get_shares_from_local_secret(secret, nr_parties):
        # TODO: ShareTensor needs to have serde serializer/deserializer
        shares = ShareTensor.generate_shares(secret=secret, nr_shares=nr_parties)
        return shares

    def reconstruct(self):
        local_shares = [share.get() for share in self.child]
        is_share_tensor = isinstance(local_shares[0], ShareTensor)

        if is_share_tensor:
            local_shares = [share.child for share in local_shares]

        result = local_shares[0]
        for share in local_shares[1:]:
            result = result + share

        if not is_share_tensor:
            result = result.decode()
        return result

    @staticmethod
    def __get_shape(x_shape, y_shape, operator):
        res = operator(np.empty(x_shape), np.empty(y_shape)).shape
        return res

    def __add__(self, other):
        if isinstance(other, MPCTensor):
            res_shares = [operator.add(a, b) for a, b in zip(self.child, other.child)]
        else:
            res_shares = [operator.add(a, b) for a, b in zip(self.child, other)]

        new_shape = MPCTensor.__get_shape(self.mpc_shape, other.mpc_shape, operator.add)
        res = MPCTensor(shares = res_shares, shape=new_shape)

        return res