# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/pycolab/position.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.lib.python import dict_pb2 as proto_dot_lib_dot_python_dot_dict__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/pycolab/position.proto",
    package="syft.lib.pycolab",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n proto/lib/pycolab/position.proto\x12\x10syft.lib.pycolab\x1a\x1bproto/lib/python/dict.proto\"3\n\x08Position\x12'\n\x08position\x18\x01 \x01(\x0b\x32\x15.syft.lib.python.Dictb\x06proto3",
    dependencies=[
        proto_dot_lib_dot_python_dot_dict__pb2.DESCRIPTOR,
    ],
)


_POSITION = _descriptor.Descriptor(
    name="Position",
    full_name="syft.lib.pycolab.Position",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="position",
            full_name="syft.lib.pycolab.Position.position",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=83,
    serialized_end=134,
)

_POSITION.fields_by_name[
    "position"
].message_type = proto_dot_lib_dot_python_dot_dict__pb2._DICT
DESCRIPTOR.message_types_by_name["Position"] = _POSITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Position = _reflection.GeneratedProtocolMessageType(
    "Position",
    (_message.Message,),
    {
        "DESCRIPTOR": _POSITION,
        "__module__": "proto.lib.pycolab.position_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.pycolab.Position)
    },
)
_sym_db.RegisterMessage(Position)


# @@protoc_insertion_point(module_scope)