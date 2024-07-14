# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pymammotion/proto/luba_mul.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n pymammotion/proto/luba_mul.proto\"V\n\x0bMulSetAudio\x12\x13\n\tat_switch\x18\x01 \x01(\x05H\x00\x12$\n\x0b\x61u_language\x18\x02 \x01(\x0e\x32\r.MUL_LANGUAGEH\x00\x42\x0c\n\nAudioCfg_u\"H\n\x0bMulSetVideo\x12&\n\x08position\x18\x01 \x01(\x0e\x32\x14.MUL_CAMERA_POSITION\x12\x11\n\tvi_switch\x18\x02 \x01(\x05\";\n\x0eMulSetVideoAck\x12)\n\nerror_code\x18\x01 \x01(\x0e\x32\x15.MUL_VIDEO_ERROR_CODE\"D\n\x0bMulAudioCfg\x12\x11\n\tau_switch\x18\x01 \x01(\x05\x12\"\n\x0b\x61u_language\x18\x02 \x01(\x0e\x32\r.MUL_LANGUAGE\"\x1c\n\x0bMulSetWiper\x12\r\n\x05round\x18\x01 \x01(\x05\";\n\x0eMulSetWiperAck\x12)\n\nerror_code\x18\x01 \x01(\x0e\x32\x15.MUL_WIPER_ERROR_CODE\"\xf2\x01\n\x06SocMul\x12!\n\tset_audio\x18\x01 \x01(\x0b\x32\x0c.MulSetAudioH\x00\x12!\n\taudio_cfg\x18\x02 \x01(\x0b\x32\x0c.MulAudioCfgH\x00\x12!\n\tset_video\x18\x03 \x01(\x0b\x32\x0c.MulSetVideoH\x00\x12(\n\rset_video_ack\x18\x04 \x01(\x0b\x32\x0f.MulSetVideoAckH\x00\x12!\n\tset_wiper\x18\x05 \x01(\x0b\x32\x0c.MulSetWiperH\x00\x12(\n\rset_wiper_ack\x18\x06 \x01(\x0b\x32\x0f.MulSetWiperAckH\x00\x42\x08\n\x06SubMul*\'\n\x0cMUL_LANGUAGE\x12\x0b\n\x07\x45NGLISH\x10\x00\x12\n\n\x06GERMAN\x10\x01*=\n\x13MUL_CAMERA_POSITION\x12\x08\n\x04LEFT\x10\x00\x12\t\n\x05RIGHT\x10\x01\x12\x08\n\x04REAR\x10\x02\x12\x07\n\x03\x41LL\x10\x03*\x9d\x01\n\x14MUL_VIDEO_ERROR_CODE\x12\x0b\n\x07SUCCESS\x10\x00\x12\x15\n\x11\x41\x43TIVATION_FAILED\x10\x01\x12\x19\n\x15NETWORK_NOT_AVAILABLE\x10\x02\x12\x19\n\x15\x43REATE_CHANNEL_FAILED\x10\x03\x12\x11\n\rPARAM_INVAILD\x10\x04\x12\x18\n\x14\x43\x45LLULAR_RESTRICTION\x10\x05*Q\n\x14MUL_WIPER_ERROR_CODE\x12\x0f\n\x0bSET_SUCCESS\x10\x00\x12\x0c\n\x08HW_ERROR\x10\x01\x12\x1a\n\x16NAVIGATION_WORK_FORBID\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pymammotion.proto.luba_mul_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MUL_LANGUAGE._serialized_start=665
  _MUL_LANGUAGE._serialized_end=704
  _MUL_CAMERA_POSITION._serialized_start=706
  _MUL_CAMERA_POSITION._serialized_end=767
  _MUL_VIDEO_ERROR_CODE._serialized_start=770
  _MUL_VIDEO_ERROR_CODE._serialized_end=927
  _MUL_WIPER_ERROR_CODE._serialized_start=929
  _MUL_WIPER_ERROR_CODE._serialized_end=1010
  _MULSETAUDIO._serialized_start=36
  _MULSETAUDIO._serialized_end=122
  _MULSETVIDEO._serialized_start=124
  _MULSETVIDEO._serialized_end=196
  _MULSETVIDEOACK._serialized_start=198
  _MULSETVIDEOACK._serialized_end=257
  _MULAUDIOCFG._serialized_start=259
  _MULAUDIOCFG._serialized_end=327
  _MULSETWIPER._serialized_start=329
  _MULSETWIPER._serialized_end=357
  _MULSETWIPERACK._serialized_start=359
  _MULSETWIPERACK._serialized_end=418
  _SOCMUL._serialized_start=421
  _SOCMUL._serialized_end=663
# @@protoc_insertion_point(module_scope)
