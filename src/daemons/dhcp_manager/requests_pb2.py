# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='requests.proto',
  package='dhcp_manager',
  serialized_pb='\n\x0erequests.proto\x12\x0c\x64hcp_manager\"*\n\x07Request\x12\x0f\n\x07\x63ommand\x18\x01 \x02(\t\x12\x0e\n\x06params\x18\x02 \x03(\t\"*\n\x0eIpRangeRequest\x12\x0b\n\x03ip1\x18\x01 \x02(\t\x12\x0b\n\x03ip2\x18\x02 \x02(\t')




_REQUEST = descriptor.Descriptor(
  name='Request',
  full_name='dhcp_manager.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='command', full_name='dhcp_manager.Request.command', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='params', full_name='dhcp_manager.Request.params', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  extension_ranges=[],
  serialized_start=32,
  serialized_end=74,
)


_IPRANGEREQUEST = descriptor.Descriptor(
  name='IpRangeRequest',
  full_name='dhcp_manager.IpRangeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ip1', full_name='dhcp_manager.IpRangeRequest.ip1', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ip2', full_name='dhcp_manager.IpRangeRequest.ip2', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=76,
  serialized_end=118,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['IpRangeRequest'] = _IPRANGEREQUEST

class Request(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUEST
  
  # @@protoc_insertion_point(class_scope:dhcp_manager.Request)

class IpRangeRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _IPRANGEREQUEST
  
  # @@protoc_insertion_point(class_scope:dhcp_manager.IpRangeRequest)

# @@protoc_insertion_point(module_scope)
