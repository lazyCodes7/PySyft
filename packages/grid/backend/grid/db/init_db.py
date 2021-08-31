# third party
from sqlalchemy.orm import Session

# syft absolute
from syft.core.node.common.node_service.node_setup.node_setup_messages import (
    CreateInitialSetUpMessage,
)

# grid absolute
from grid.core.config import settings
from grid.core.node import node
from grid.db import base  # noqa: F401
# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    # Build Syft Message
    msg = CreateInitialSetUpMessage(
        address=node.address,
        name="Jane Doe",
        email=settings.FIRST_SUPERUSER,
        password=settings.FIRST_SUPERUSER_PASSWORD,
        domain_name=settings.DOMAIN_NAME,
        reply_to=node.address,
    ).sign(signing_key=node.signing_key)

    # Process syft message
    _ = node.recv_immediate_msg_with_reply(msg=msg).message