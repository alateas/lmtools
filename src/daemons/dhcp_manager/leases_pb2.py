# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='leases.proto',
  package='dhcp_manager',
  serialized_pb='\n\x0cleases.proto\x12\x0c\x64hcp_manager\".\n\x05Lease\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\n\n\x02ip\x18\x02 \x02(\t\x12\x0b\n\x03mac\x18\x03 \x02(\t\"/\n\tLeasesSet\x12\"\n\x05lease\x18\x01 \x03(\x0b\x32\x13.dhcp_manager.Lease\"\x19\n\x06Status\x12\x0f\n\x07success\x18\x01 \x02(\x08')




_LEASE = descriptor.Descriptor(
  name='Lease',
  full_name='dhcp_manager.Lease',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='dhcp_manager.Lease.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ip', full_name='dhcp_manager.Lease.ip', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mac', full_name='dhcp_manager.Lease.mac', index=2,
      number=3, type=9, cpp_type=9, label=2,
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
  serialized_start=30,
  serialized_end=76,
)


_LEASESSET = descriptor.Descriptor(
  name='LeasesSet',
  full_name='dhcp_manager.LeasesSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='lease', full_name='dhcp_manager.LeasesSet.lease', index=0,
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
  extension_ranges=[],
  serialized_start=78,
  serialized_end=125,
)


_STATUS = descriptor.Descriptor(
  name='Status',
  full_name='dhcp_manager.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='success', full_name='dhcp_manager.Status.success', index=0,
      number=1, type=8, cpp_type=7, label=2,
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
  extension_ranges=[],
  serialized_start=127,
  serialized_end=152,
)

_LEASESSET.fields_by_name['lease'].message_type = _LEASE
DESCRIPTOR.message_types_by_name['Lease'] = _LEASE
DESCRIPTOR.message_types_by_name['LeasesSet'] = _LEASESSET
DESCRIPTOR.message_types_by_name['Status'] = _STATUS

class Lease(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LEASE
  
  # @@protoc_insertion_point(class_scope:dhcp_manager.Lease)

class LeasesSet(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LEASESSET
  
  # @@protoc_insertion_point(class_scope:dhcp_manager.LeasesSet)

class Status(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STATUS
  
  # @@protoc_insertion_point(class_scope:dhcp_manager.Status)

# @@protoc_insertion_point(module_scope)
