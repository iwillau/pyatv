# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FieldDescriptor as google___protobuf___descriptor___FieldDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from pyatv.mrp.protobuf.TransactionPackets_pb2 import (
    TransactionPackets as pyatv___mrp___protobuf___TransactionPackets_pb2___TransactionPackets,
)

from typing import (
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


class TransactionMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: builtin___int

    @property
    def packets(self) -> pyatv___mrp___protobuf___TransactionPackets_pb2___TransactionPackets: ...

    def __init__(self,
        *,
        name : typing___Optional[builtin___int] = None,
        packets : typing___Optional[pyatv___mrp___protobuf___TransactionPackets_pb2___TransactionPackets] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> TransactionMessage: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"name",u"packets"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"name",u"packets"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"name",b"name",u"packets",b"packets"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name",u"packets",b"packets"]) -> None: ...

transactionMessage = ... # type: google___protobuf___descriptor___FieldDescriptor
