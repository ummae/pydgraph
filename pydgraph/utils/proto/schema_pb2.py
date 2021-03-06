# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schema.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='schema.proto',
  package='protos',
  syntax='proto3',
  serialized_pb=_b('\n\x0cschema.proto\x12\x06protos\"E\n\rSchemaRequest\x12\x10\n\x08group_id\x18\x01 \x01(\r\x12\x12\n\npredicates\x18\x02 \x03(\t\x12\x0e\n\x06\x66ields\x18\x03 \x03(\t\"2\n\x0cSchemaResult\x12\"\n\x06schema\x18\x01 \x03(\x0b\x32\x12.protos.SchemaNode\"`\n\nSchemaNode\x12\x11\n\tpredicate\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\r\n\x05index\x18\x03 \x01(\x08\x12\x11\n\ttokenizer\x18\x04 \x03(\t\x12\x0f\n\x07reverse\x18\x05 \x01(\x08\"\xaa\x01\n\x0cSchemaUpdate\x12\x11\n\tpredicate\x18\x01 \x01(\t\x12\x12\n\nvalue_type\x18\x02 \x01(\r\x12\x31\n\tdirective\x18\x03 \x01(\x0e\x32\x1e.protos.SchemaUpdate.Directive\x12\x11\n\ttokenizer\x18\x04 \x03(\t\"-\n\tDirective\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05INDEX\x10\x01\x12\x0b\n\x07REVERSE\x10\x02\x62\x06proto3')
)



_SCHEMAUPDATE_DIRECTIVE = _descriptor.EnumDescriptor(
  name='Directive',
  full_name='protos.SchemaUpdate.Directive',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDEX', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REVERSE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=371,
  serialized_end=416,
)
_sym_db.RegisterEnumDescriptor(_SCHEMAUPDATE_DIRECTIVE)


_SCHEMAREQUEST = _descriptor.Descriptor(
  name='SchemaRequest',
  full_name='protos.SchemaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_id', full_name='protos.SchemaRequest.group_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predicates', full_name='protos.SchemaRequest.predicates', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fields', full_name='protos.SchemaRequest.fields', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=93,
)


_SCHEMARESULT = _descriptor.Descriptor(
  name='SchemaResult',
  full_name='protos.SchemaResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schema', full_name='protos.SchemaResult.schema', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=145,
)


_SCHEMANODE = _descriptor.Descriptor(
  name='SchemaNode',
  full_name='protos.SchemaNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='predicate', full_name='protos.SchemaNode.predicate', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='protos.SchemaNode.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='protos.SchemaNode.index', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tokenizer', full_name='protos.SchemaNode.tokenizer', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reverse', full_name='protos.SchemaNode.reverse', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=147,
  serialized_end=243,
)


_SCHEMAUPDATE = _descriptor.Descriptor(
  name='SchemaUpdate',
  full_name='protos.SchemaUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='predicate', full_name='protos.SchemaUpdate.predicate', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_type', full_name='protos.SchemaUpdate.value_type', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='directive', full_name='protos.SchemaUpdate.directive', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tokenizer', full_name='protos.SchemaUpdate.tokenizer', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SCHEMAUPDATE_DIRECTIVE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=246,
  serialized_end=416,
)

_SCHEMARESULT.fields_by_name['schema'].message_type = _SCHEMANODE
_SCHEMAUPDATE.fields_by_name['directive'].enum_type = _SCHEMAUPDATE_DIRECTIVE
_SCHEMAUPDATE_DIRECTIVE.containing_type = _SCHEMAUPDATE
DESCRIPTOR.message_types_by_name['SchemaRequest'] = _SCHEMAREQUEST
DESCRIPTOR.message_types_by_name['SchemaResult'] = _SCHEMARESULT
DESCRIPTOR.message_types_by_name['SchemaNode'] = _SCHEMANODE
DESCRIPTOR.message_types_by_name['SchemaUpdate'] = _SCHEMAUPDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SchemaRequest = _reflection.GeneratedProtocolMessageType('SchemaRequest', (_message.Message,), dict(
  DESCRIPTOR = _SCHEMAREQUEST,
  __module__ = 'schema_pb2'
  # @@protoc_insertion_point(class_scope:protos.SchemaRequest)
  ))
_sym_db.RegisterMessage(SchemaRequest)

SchemaResult = _reflection.GeneratedProtocolMessageType('SchemaResult', (_message.Message,), dict(
  DESCRIPTOR = _SCHEMARESULT,
  __module__ = 'schema_pb2'
  # @@protoc_insertion_point(class_scope:protos.SchemaResult)
  ))
_sym_db.RegisterMessage(SchemaResult)

SchemaNode = _reflection.GeneratedProtocolMessageType('SchemaNode', (_message.Message,), dict(
  DESCRIPTOR = _SCHEMANODE,
  __module__ = 'schema_pb2'
  # @@protoc_insertion_point(class_scope:protos.SchemaNode)
  ))
_sym_db.RegisterMessage(SchemaNode)

SchemaUpdate = _reflection.GeneratedProtocolMessageType('SchemaUpdate', (_message.Message,), dict(
  DESCRIPTOR = _SCHEMAUPDATE,
  __module__ = 'schema_pb2'
  # @@protoc_insertion_point(class_scope:protos.SchemaUpdate)
  ))
_sym_db.RegisterMessage(SchemaUpdate)


# @@protoc_insertion_point(module_scope)