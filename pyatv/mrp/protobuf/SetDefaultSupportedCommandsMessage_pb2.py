# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/mrp/protobuf/SetDefaultSupportedCommandsMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2
from pyatv.mrp.protobuf import SupportedCommands_pb2 as pyatv_dot_mrp_dot_protobuf_dot_SupportedCommands__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/mrp/protobuf/SetDefaultSupportedCommandsMessage.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n;pyatv/mrp/protobuf/SetDefaultSupportedCommandsMessage.proto\x1a(pyatv/mrp/protobuf/ProtocolMessage.proto\x1a*pyatv/mrp/protobuf/SupportedCommands.proto\"f\n\"SetDefaultSupportedCommandsMessage\x12-\n\x11supportedCommands\x18\x02 \x01(\x0b\x32\x12.SupportedCommands\x12\x11\n\tdisplayID\x18\x04 \x01(\t:a\n\"setDefaultSupportedCommandsMessage\x12\x10.ProtocolMessage\x18K \x01(\x0b\x32#.SetDefaultSupportedCommandsMessage')
  ,
  dependencies=[pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.DESCRIPTOR,pyatv_dot_mrp_dot_protobuf_dot_SupportedCommands__pb2.DESCRIPTOR,])


SETDEFAULTSUPPORTEDCOMMANDSMESSAGE_FIELD_NUMBER = 75
setDefaultSupportedCommandsMessage = _descriptor.FieldDescriptor(
  name='setDefaultSupportedCommandsMessage', full_name='setDefaultSupportedCommandsMessage', index=0,
  number=75, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)


_SETDEFAULTSUPPORTEDCOMMANDSMESSAGE = _descriptor.Descriptor(
  name='SetDefaultSupportedCommandsMessage',
  full_name='SetDefaultSupportedCommandsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='supportedCommands', full_name='SetDefaultSupportedCommandsMessage.supportedCommands', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='displayID', full_name='SetDefaultSupportedCommandsMessage.displayID', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=251,
)

_SETDEFAULTSUPPORTEDCOMMANDSMESSAGE.fields_by_name['supportedCommands'].message_type = pyatv_dot_mrp_dot_protobuf_dot_SupportedCommands__pb2._SUPPORTEDCOMMANDS
DESCRIPTOR.message_types_by_name['SetDefaultSupportedCommandsMessage'] = _SETDEFAULTSUPPORTEDCOMMANDSMESSAGE
DESCRIPTOR.extensions_by_name['setDefaultSupportedCommandsMessage'] = setDefaultSupportedCommandsMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetDefaultSupportedCommandsMessage = _reflection.GeneratedProtocolMessageType('SetDefaultSupportedCommandsMessage', (_message.Message,), {
  'DESCRIPTOR' : _SETDEFAULTSUPPORTEDCOMMANDSMESSAGE,
  '__module__' : 'pyatv.mrp.protobuf.SetDefaultSupportedCommandsMessage_pb2'
  # @@protoc_insertion_point(class_scope:SetDefaultSupportedCommandsMessage)
  })
_sym_db.RegisterMessage(SetDefaultSupportedCommandsMessage)

setDefaultSupportedCommandsMessage.message_type = _SETDEFAULTSUPPORTEDCOMMANDSMESSAGE
pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(setDefaultSupportedCommandsMessage)

# @@protoc_insertion_point(module_scope)
