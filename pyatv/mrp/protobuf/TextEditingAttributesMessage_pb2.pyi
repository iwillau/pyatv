# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from pyatv.mrp.protobuf.TextInputTraitsMessage_pb2 import (
    TextInputTraits as pyatv___mrp___protobuf___TextInputTraitsMessage_pb2___TextInputTraits,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class TextEditingAttributes(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    title = ... # type: typing___Text
    prompt = ... # type: typing___Text

    @property
    def inputTraits(self) -> pyatv___mrp___protobuf___TextInputTraitsMessage_pb2___TextInputTraits: ...

    def __init__(self,
        *,
        title : typing___Optional[typing___Text] = None,
        prompt : typing___Optional[typing___Text] = None,
        inputTraits : typing___Optional[pyatv___mrp___protobuf___TextInputTraitsMessage_pb2___TextInputTraits] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> TextEditingAttributes: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"inputTraits",u"prompt",u"title"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"inputTraits",u"prompt",u"title"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"inputTraits",b"inputTraits",u"prompt",b"prompt",u"title",b"title"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"inputTraits",b"inputTraits",u"prompt",b"prompt",u"title",b"title"]) -> None: ...