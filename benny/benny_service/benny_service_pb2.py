# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: benny_service/benny_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='benny_service/benny_service.proto',
  package='sono',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!benny_service/benny_service.proto\x12\x04sono\";\n\x0cUserResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"I\n\x0ePaginateParams\x12\x12\n\nsearchTerm\x18\x01 \x01(\t\x12\x11\n\tpageIndex\x18\x02 \x01(\x05\x12\x10\n\x08pageSize\x18\x03 \x01(\x05\"5\n\x10PaginateResponse\x12!\n\x05users\x18\x01 \x03(\x0b\x32\x12.sono.UserResponse\" \n\x0fUserEmailParams\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"\x1a\n\x0cUserIdParams\x12\n\n\x02id\x18\x01 \x01(\x05\x32\xc6\x01\n\x0e\x41\x63\x63ountService\x12\x38\n\x0cReadUserById\x12\x12.sono.UserIdParams\x1a\x12.sono.UserResponse\"\x00\x12>\n\x0fReadUserByEmail\x12\x15.sono.UserEmailParams\x1a\x12.sono.UserResponse\"\x00\x12:\n\x08Paginate\x12\x14.sono.PaginateParams\x1a\x16.sono.PaginateResponse\"\x00\x62\x06proto3')
)




_USERRESPONSE = _descriptor.Descriptor(
  name='UserResponse',
  full_name='sono.UserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sono.UserResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='sono.UserResponse.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='sono.UserResponse.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=102,
)


_PAGINATEPARAMS = _descriptor.Descriptor(
  name='PaginateParams',
  full_name='sono.PaginateParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='searchTerm', full_name='sono.PaginateParams.searchTerm', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageIndex', full_name='sono.PaginateParams.pageIndex', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='sono.PaginateParams.pageSize', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=177,
)


_PAGINATERESPONSE = _descriptor.Descriptor(
  name='PaginateResponse',
  full_name='sono.PaginateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='sono.PaginateResponse.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=179,
  serialized_end=232,
)


_USEREMAILPARAMS = _descriptor.Descriptor(
  name='UserEmailParams',
  full_name='sono.UserEmailParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='sono.UserEmailParams.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=234,
  serialized_end=266,
)


_USERIDPARAMS = _descriptor.Descriptor(
  name='UserIdParams',
  full_name='sono.UserIdParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sono.UserIdParams.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=268,
  serialized_end=294,
)

_PAGINATERESPONSE.fields_by_name['users'].message_type = _USERRESPONSE
DESCRIPTOR.message_types_by_name['UserResponse'] = _USERRESPONSE
DESCRIPTOR.message_types_by_name['PaginateParams'] = _PAGINATEPARAMS
DESCRIPTOR.message_types_by_name['PaginateResponse'] = _PAGINATERESPONSE
DESCRIPTOR.message_types_by_name['UserEmailParams'] = _USEREMAILPARAMS
DESCRIPTOR.message_types_by_name['UserIdParams'] = _USERIDPARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserResponse = _reflection.GeneratedProtocolMessageType('UserResponse', (_message.Message,), dict(
  DESCRIPTOR = _USERRESPONSE,
  __module__ = 'benny_service.benny_service_pb2'
  # @@protoc_insertion_point(class_scope:sono.UserResponse)
  ))
_sym_db.RegisterMessage(UserResponse)

PaginateParams = _reflection.GeneratedProtocolMessageType('PaginateParams', (_message.Message,), dict(
  DESCRIPTOR = _PAGINATEPARAMS,
  __module__ = 'benny_service.benny_service_pb2'
  # @@protoc_insertion_point(class_scope:sono.PaginateParams)
  ))
_sym_db.RegisterMessage(PaginateParams)

PaginateResponse = _reflection.GeneratedProtocolMessageType('PaginateResponse', (_message.Message,), dict(
  DESCRIPTOR = _PAGINATERESPONSE,
  __module__ = 'benny_service.benny_service_pb2'
  # @@protoc_insertion_point(class_scope:sono.PaginateResponse)
  ))
_sym_db.RegisterMessage(PaginateResponse)

UserEmailParams = _reflection.GeneratedProtocolMessageType('UserEmailParams', (_message.Message,), dict(
  DESCRIPTOR = _USEREMAILPARAMS,
  __module__ = 'benny_service.benny_service_pb2'
  # @@protoc_insertion_point(class_scope:sono.UserEmailParams)
  ))
_sym_db.RegisterMessage(UserEmailParams)

UserIdParams = _reflection.GeneratedProtocolMessageType('UserIdParams', (_message.Message,), dict(
  DESCRIPTOR = _USERIDPARAMS,
  __module__ = 'benny_service.benny_service_pb2'
  # @@protoc_insertion_point(class_scope:sono.UserIdParams)
  ))
_sym_db.RegisterMessage(UserIdParams)



_ACCOUNTSERVICE = _descriptor.ServiceDescriptor(
  name='AccountService',
  full_name='sono.AccountService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=297,
  serialized_end=495,
  methods=[
  _descriptor.MethodDescriptor(
    name='ReadUserById',
    full_name='sono.AccountService.ReadUserById',
    index=0,
    containing_service=None,
    input_type=_USERIDPARAMS,
    output_type=_USERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReadUserByEmail',
    full_name='sono.AccountService.ReadUserByEmail',
    index=1,
    containing_service=None,
    input_type=_USEREMAILPARAMS,
    output_type=_USERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Paginate',
    full_name='sono.AccountService.Paginate',
    index=2,
    containing_service=None,
    input_type=_PAGINATEPARAMS,
    output_type=_PAGINATERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ACCOUNTSERVICE)

DESCRIPTOR.services_by_name['AccountService'] = _ACCOUNTSERVICE

# @@protoc_insertion_point(module_scope)