# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/iap_item_display.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import iap_item_category_pb2 as pogoprotos_dot_enums_dot_iap__item__category__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/iap_item_display.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_pb=_b('\n1pogoprotos/settings/master/iap_item_display.proto\x12\x1apogoprotos.settings.master\x1a(pogoprotos/enums/iap_item_category.proto\"\xdd\x02\n\x0eIapItemDisplay\x12\x0b\n\x03sku\x18\x01 \x01(\t\x12\x37\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32%.pogoprotos.enums.HoloIapItemCategory\x12\x12\n\nsort_order\x18\x03 \x01(\x05\x12\x0e\n\x06hidden\x18\x06 \x01(\x08\x12\x0c\n\x04sale\x18\x07 \x01(\x08\x12\x11\n\tsprite_id\x18\x08 \x01(\t\x12\r\n\x05title\x18\t \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\n \x01(\t\x12\x17\n\x0fsku_enable_time\x18\x0b \x01(\t\x12\x18\n\x10sku_disable_time\x18\x0c \x01(\t\x12\x1e\n\x16sku_enable_time_utc_ms\x18\r \x01(\x03\x12\x1f\n\x17sku_disable_time_utc_ms\x18\x0e \x01(\x03\x12\x15\n\rsubcategories\x18\x0f \x03(\t\x12\x11\n\timage_url\x18\x10 \x01(\tb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_iap__item__category__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_IAPITEMDISPLAY = _descriptor.Descriptor(
  name='IapItemDisplay',
  full_name='pogoprotos.settings.master.IapItemDisplay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sku', full_name='pogoprotos.settings.master.IapItemDisplay.sku', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category', full_name='pogoprotos.settings.master.IapItemDisplay.category', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_order', full_name='pogoprotos.settings.master.IapItemDisplay.sort_order', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hidden', full_name='pogoprotos.settings.master.IapItemDisplay.hidden', index=3,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sale', full_name='pogoprotos.settings.master.IapItemDisplay.sale', index=4,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sprite_id', full_name='pogoprotos.settings.master.IapItemDisplay.sprite_id', index=5,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='pogoprotos.settings.master.IapItemDisplay.title', index=6,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='pogoprotos.settings.master.IapItemDisplay.description', index=7,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sku_enable_time', full_name='pogoprotos.settings.master.IapItemDisplay.sku_enable_time', index=8,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sku_disable_time', full_name='pogoprotos.settings.master.IapItemDisplay.sku_disable_time', index=9,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sku_enable_time_utc_ms', full_name='pogoprotos.settings.master.IapItemDisplay.sku_enable_time_utc_ms', index=10,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sku_disable_time_utc_ms', full_name='pogoprotos.settings.master.IapItemDisplay.sku_disable_time_utc_ms', index=11,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subcategories', full_name='pogoprotos.settings.master.IapItemDisplay.subcategories', index=12,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_url', full_name='pogoprotos.settings.master.IapItemDisplay.image_url', index=13,
      number=16, type=9, cpp_type=9, label=1,
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
  serialized_start=124,
  serialized_end=473,
)

_IAPITEMDISPLAY.fields_by_name['category'].enum_type = pogoprotos_dot_enums_dot_iap__item__category__pb2._HOLOIAPITEMCATEGORY
DESCRIPTOR.message_types_by_name['IapItemDisplay'] = _IAPITEMDISPLAY

IapItemDisplay = _reflection.GeneratedProtocolMessageType('IapItemDisplay', (_message.Message,), dict(
  DESCRIPTOR = _IAPITEMDISPLAY,
  __module__ = 'pogoprotos.settings.master.iap_item_display_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.IapItemDisplay)
  ))
_sym_db.RegisterMessage(IapItemDisplay)


# @@protoc_insertion_point(module_scope)