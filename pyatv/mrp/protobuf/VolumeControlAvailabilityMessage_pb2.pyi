# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FieldDescriptor as google___protobuf___descriptor___FieldDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
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


class VolumeControlAvailabilityMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    volumeControlAvailable = ... # type: builtin___bool
    volumeCapabilities = ... # type: builtin___int

    def __init__(self,
        *,
        volumeControlAvailable : typing___Optional[builtin___bool] = None,
        volumeCapabilities : typing___Optional[builtin___int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> VolumeControlAvailabilityMessage: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"volumeCapabilities",u"volumeControlAvailable"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"volumeCapabilities",u"volumeControlAvailable"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"volumeCapabilities",b"volumeCapabilities",u"volumeControlAvailable",b"volumeControlAvailable"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"volumeCapabilities",b"volumeCapabilities",u"volumeControlAvailable",b"volumeControlAvailable"]) -> None: ...

volumeControlAvailabilityMessage = ... # type: google___protobuf___descriptor___FieldDescriptor
