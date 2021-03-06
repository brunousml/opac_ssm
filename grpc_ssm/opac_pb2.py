# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: opac.proto

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
  name='opac.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\nopac.proto\"X\n\x05\x41sset\x12\x0c\n\x04\x66ile\x18\x01 \x01(\x0c\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x10\n\x08metadata\x18\x04 \x01(\t\x12\x0f\n\x07task_id\x18\x05 \x01(\t\"*\n\tAssetInfo\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x10\n\x08url_path\x18\x02 \x01(\t\"\x14\n\x06TaskId\x12\n\n\x02id\x18\x01 \x01(\t\"\x1a\n\tTaskState\x12\r\n\x05state\x18\x01 \x01(\t2\xa0\x01\n\x0c\x41ssetService\x12\x1e\n\tget_asset\x12\x07.TaskId\x1a\x06.Asset\"\x00\x12\x1e\n\tadd_asset\x12\x06.Asset\x1a\x07.TaskId\"\x00\x12\'\n\x0eget_asset_info\x12\x07.TaskId\x1a\n.AssetInfo\"\x00\x12\'\n\x0eget_task_state\x12\x07.TaskId\x1a\n.TaskState\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ASSET = _descriptor.Descriptor(
  name='Asset',
  full_name='Asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='Asset.file', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filename', full_name='Asset.filename', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Asset.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='Asset.metadata', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='Asset.task_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=14,
  serialized_end=102,
)


_ASSETINFO = _descriptor.Descriptor(
  name='AssetInfo',
  full_name='AssetInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='AssetInfo.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url_path', full_name='AssetInfo.url_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=104,
  serialized_end=146,
)


_TASKID = _descriptor.Descriptor(
  name='TaskId',
  full_name='TaskId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='TaskId.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=148,
  serialized_end=168,
)


_TASKSTATE = _descriptor.Descriptor(
  name='TaskState',
  full_name='TaskState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='TaskState.state', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=170,
  serialized_end=196,
)

DESCRIPTOR.message_types_by_name['Asset'] = _ASSET
DESCRIPTOR.message_types_by_name['AssetInfo'] = _ASSETINFO
DESCRIPTOR.message_types_by_name['TaskId'] = _TASKID
DESCRIPTOR.message_types_by_name['TaskState'] = _TASKSTATE

Asset = _reflection.GeneratedProtocolMessageType('Asset', (_message.Message,), dict(
  DESCRIPTOR = _ASSET,
  __module__ = 'opac_pb2'
  # @@protoc_insertion_point(class_scope:Asset)
  ))
_sym_db.RegisterMessage(Asset)

AssetInfo = _reflection.GeneratedProtocolMessageType('AssetInfo', (_message.Message,), dict(
  DESCRIPTOR = _ASSETINFO,
  __module__ = 'opac_pb2'
  # @@protoc_insertion_point(class_scope:AssetInfo)
  ))
_sym_db.RegisterMessage(AssetInfo)

TaskId = _reflection.GeneratedProtocolMessageType('TaskId', (_message.Message,), dict(
  DESCRIPTOR = _TASKID,
  __module__ = 'opac_pb2'
  # @@protoc_insertion_point(class_scope:TaskId)
  ))
_sym_db.RegisterMessage(TaskId)

TaskState = _reflection.GeneratedProtocolMessageType('TaskState', (_message.Message,), dict(
  DESCRIPTOR = _TASKSTATE,
  __module__ = 'opac_pb2'
  # @@protoc_insertion_point(class_scope:TaskState)
  ))
_sym_db.RegisterMessage(TaskState)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class AssetServiceStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.get_asset = channel.unary_unary(
          '/AssetService/get_asset',
          request_serializer=TaskId.SerializeToString,
          response_deserializer=Asset.FromString,
          )
      self.add_asset = channel.unary_unary(
          '/AssetService/add_asset',
          request_serializer=Asset.SerializeToString,
          response_deserializer=TaskId.FromString,
          )
      self.get_asset_info = channel.unary_unary(
          '/AssetService/get_asset_info',
          request_serializer=TaskId.SerializeToString,
          response_deserializer=AssetInfo.FromString,
          )
      self.get_task_state = channel.unary_unary(
          '/AssetService/get_task_state',
          request_serializer=TaskId.SerializeToString,
          response_deserializer=TaskState.FromString,
          )


  class AssetServiceServicer(object):

    def get_asset(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def add_asset(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def get_asset_info(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def get_task_state(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_AssetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'get_asset': grpc.unary_unary_rpc_method_handler(
            servicer.get_asset,
            request_deserializer=TaskId.FromString,
            response_serializer=Asset.SerializeToString,
        ),
        'add_asset': grpc.unary_unary_rpc_method_handler(
            servicer.add_asset,
            request_deserializer=Asset.FromString,
            response_serializer=TaskId.SerializeToString,
        ),
        'get_asset_info': grpc.unary_unary_rpc_method_handler(
            servicer.get_asset_info,
            request_deserializer=TaskId.FromString,
            response_serializer=AssetInfo.SerializeToString,
        ),
        'get_task_state': grpc.unary_unary_rpc_method_handler(
            servicer.get_task_state,
            request_deserializer=TaskId.FromString,
            response_serializer=TaskState.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'AssetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaAssetServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def get_asset(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def add_asset(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def get_asset_info(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def get_task_state(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaAssetServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def get_asset(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    get_asset.future = None
    def add_asset(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    add_asset.future = None
    def get_asset_info(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    get_asset_info.future = None
    def get_task_state(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    get_task_state.future = None


  def beta_create_AssetService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('AssetService', 'add_asset'): Asset.FromString,
      ('AssetService', 'get_asset'): TaskId.FromString,
      ('AssetService', 'get_asset_info'): TaskId.FromString,
      ('AssetService', 'get_task_state'): TaskId.FromString,
    }
    response_serializers = {
      ('AssetService', 'add_asset'): TaskId.SerializeToString,
      ('AssetService', 'get_asset'): Asset.SerializeToString,
      ('AssetService', 'get_asset_info'): AssetInfo.SerializeToString,
      ('AssetService', 'get_task_state'): TaskState.SerializeToString,
    }
    method_implementations = {
      ('AssetService', 'add_asset'): face_utilities.unary_unary_inline(servicer.add_asset),
      ('AssetService', 'get_asset'): face_utilities.unary_unary_inline(servicer.get_asset),
      ('AssetService', 'get_asset_info'): face_utilities.unary_unary_inline(servicer.get_asset_info),
      ('AssetService', 'get_task_state'): face_utilities.unary_unary_inline(servicer.get_task_state),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_AssetService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('AssetService', 'add_asset'): Asset.SerializeToString,
      ('AssetService', 'get_asset'): TaskId.SerializeToString,
      ('AssetService', 'get_asset_info'): TaskId.SerializeToString,
      ('AssetService', 'get_task_state'): TaskId.SerializeToString,
    }
    response_deserializers = {
      ('AssetService', 'add_asset'): TaskId.FromString,
      ('AssetService', 'get_asset'): Asset.FromString,
      ('AssetService', 'get_asset_info'): AssetInfo.FromString,
      ('AssetService', 'get_task_state'): TaskState.FromString,
    }
    cardinalities = {
      'add_asset': cardinality.Cardinality.UNARY_UNARY,
      'get_asset': cardinality.Cardinality.UNARY_UNARY,
      'get_asset_info': cardinality.Cardinality.UNARY_UNARY,
      'get_task_state': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'AssetService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
