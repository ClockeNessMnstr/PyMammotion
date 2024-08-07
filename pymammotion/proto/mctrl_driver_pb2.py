# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pymammotion/proto/mctrl_driver.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$pymammotion/proto/mctrl_driver.proto\"@\n\rDrvMotionCtrl\x12\x16\n\x0esetLinearSpeed\x18\x01 \x01(\x05\x12\x17\n\x0fsetAngularSpeed\x18\x02 \x01(\x05\"%\n\x0e\x44rvKnifeHeight\x12\x13\n\x0bknifeHeight\x18\x01 \x01(\x05\"\'\n\nDrvSrSpeed\x12\n\n\x02rw\x18\x01 \x01(\x05\x12\r\n\x05speed\x18\x02 \x01(\x02\"&\n\x0e\x44rvKnifeStatus\x12\x14\n\x0cknife_status\x18\x01 \x01(\x05\"N\n\x14\x44rvKnifeChangeReport\x12\x10\n\x08is_start\x18\x01 \x01(\x05\x12\x12\n\nstart_high\x18\x02 \x01(\x05\x12\x10\n\x08\x65nd_high\x18\x03 \x01(\x05\"n\n\x10\x44rvMowCtrlByHand\x12\x11\n\tmain_ctrl\x18\x01 \x01(\x05\x12\x16\n\x0e\x63ut_knife_ctrl\x18\x02 \x01(\x05\x12\x18\n\x10\x63ut_knife_height\x18\x03 \x01(\x05\x12\x15\n\rmax_run_Speed\x18\x04 \x01(\x02\"4\n\rrtk_cfg_req_t\x12\x12\n\ncmd_length\x18\x01 \x01(\x05\x12\x0f\n\x07\x63md_req\x18\x02 \x01(\t\"=\n\x11rtk_cfg_req_ack_t\x12\x12\n\ncmd_length\x18\x01 \x01(\x05\x12\x14\n\x0c\x63md_response\x18\x02 \x01(\t\"*\n\x14rtk_sys_mask_query_t\x12\x12\n\nsat_system\x18\x01 \x01(\r\"H\n\x18rtk_sys_mask_query_ack_t\x12\x12\n\nsat_system\x18\x01 \x01(\r\x12\x18\n\x10system_mask_bits\x18\x02 \x03(\r\"\xc3\x04\n\nMctlDriver\x12.\n\x14todev_devmotion_ctrl\x18\x01 \x01(\x0b\x32\x0e.DrvMotionCtrlH\x00\x12\x31\n\x16todev_knife_height_set\x18\x02 \x01(\x0b\x32\x0f.DrvKnifeHeightH\x00\x12,\n\x15\x62idire_speed_read_set\x18\x03 \x01(\x0b\x32\x0b.DrvSrSpeedH\x00\x12\x35\n\x1a\x62idire_knife_height_report\x18\x04 \x01(\x0b\x32\x0f.DrvKnifeHeightH\x00\x12-\n\x12toapp_knife_status\x18\x05 \x01(\x0b\x32\x0f.DrvKnifeStatusH\x00\x12-\n\x10mow_ctrl_by_hand\x18\x06 \x01(\x0b\x32\x11.DrvMowCtrlByHandH\x00\x12%\n\x0brtk_cfg_req\x18\x07 \x01(\x0b\x32\x0e.rtk_cfg_req_tH\x00\x12-\n\x0frtk_cfg_req_ack\x18\x08 \x01(\x0b\x32\x12.rtk_cfg_req_ack_tH\x00\x12\x33\n\x12rtk_sys_mask_query\x18\t \x01(\x0b\x32\x15.rtk_sys_mask_query_tH\x00\x12;\n\x16rtk_sys_mask_query_ack\x18\n \x01(\x0b\x32\x19.rtk_sys_mask_query_ack_tH\x00\x12:\n\x19toapp_knife_status_change\x18\x0b \x01(\x0b\x32\x15.DrvKnifeChangeReportH\x00\x42\x0b\n\tSubDrvMsgb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pymammotion.proto.mctrl_driver_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DRVMOTIONCTRL._serialized_start=40
  _DRVMOTIONCTRL._serialized_end=104
  _DRVKNIFEHEIGHT._serialized_start=106
  _DRVKNIFEHEIGHT._serialized_end=143
  _DRVSRSPEED._serialized_start=145
  _DRVSRSPEED._serialized_end=184
  _DRVKNIFESTATUS._serialized_start=186
  _DRVKNIFESTATUS._serialized_end=224
  _DRVKNIFECHANGEREPORT._serialized_start=226
  _DRVKNIFECHANGEREPORT._serialized_end=304
  _DRVMOWCTRLBYHAND._serialized_start=306
  _DRVMOWCTRLBYHAND._serialized_end=416
  _RTK_CFG_REQ_T._serialized_start=418
  _RTK_CFG_REQ_T._serialized_end=470
  _RTK_CFG_REQ_ACK_T._serialized_start=472
  _RTK_CFG_REQ_ACK_T._serialized_end=533
  _RTK_SYS_MASK_QUERY_T._serialized_start=535
  _RTK_SYS_MASK_QUERY_T._serialized_end=577
  _RTK_SYS_MASK_QUERY_ACK_T._serialized_start=579
  _RTK_SYS_MASK_QUERY_ACK_T._serialized_end=651
  _MCTLDRIVER._serialized_start=654
  _MCTLDRIVER._serialized_end=1233
# @@protoc_insertion_point(module_scope)