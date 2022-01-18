# coding=utf-8
# Copyright 2022 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data.proto
# pylint: disable=bad-continuation
# pylint: disable=protected-access

"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='data.proto',
    package='keypose',
    syntax='proto2',
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\ndata.proto\x12\x07keypose\"\x1c\n\tTransform\x12\x0f\n\x07\x65lement\x18\x01 \x03(\x02\"f\n\x06\x43\x61mera\x12\n\n\x02\x66x\x18\x01 \x01(\x02\x12\n\n\x02\x66y\x18\x02 \x01(\x02\x12\n\n\x02\x63x\x18\x03 \x01(\x02\x12\n\n\x02\x63y\x18\x04 \x01(\x02\x12\x10\n\x08\x62\x61seline\x18\x05 \x01(\x02\x12\x0c\n\x04resx\x18\x06 \x01(\x02\x12\x0c\n\x04resy\x18\x07 \x01(\x02\"\xd4\x01\n\x06Target\x12%\n\ttransform\x18\x01 \x01(\x0b\x32\x12.keypose.Transform\x12\x1f\n\x06\x63\x61mera\x18\x02 \x01(\x0b\x32\x0f.keypose.Camera\x12+\n\tkeypoints\x18\x03 \x03(\x0b\x32\x18.keypose.Target.KeyPoint\x1aU\n\x08KeyPoint\x12\t\n\x01u\x18\x01 \x01(\x02\x12\t\n\x01v\x18\x02 \x01(\x02\x12\t\n\x01x\x18\x03 \x01(\x02\x12\t\n\x01y\x18\x04 \x01(\x02\x12\t\n\x01z\x18\x05 \x01(\x02\x12\x12\n\x07visible\x18\x06 \x01(\x02:\x01\x31\"p\n\nKeyTargets\x12\"\n\tkp_target\x18\x01 \x01(\x0b\x32\x0f.keypose.Target\x12%\n\x0cproj_targets\x18\x02 \x03(\x0b\x32\x0f.keypose.Target\x12\x17\n\x08mirrored\x18\x03 \x01(\x08:\x05\x66\x61lse\"Y\n\nDataParams\x12\x0c\n\x04resx\x18\x01 \x01(\x05\x12\x0c\n\x04resy\x18\x02 \x01(\x05\x12\x0e\n\x06num_kp\x18\x03 \x01(\x05\x12\x1f\n\x06\x63\x61mera\x18\x04 \x01(\x0b\x32\x0f.keypose.Camera\"j\n\x05TfSet\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncommon_dir\x18\x02 \x01(\t\x12\r\n\x05train\x18\x03 \x03(\t\x12\x0b\n\x03val\x18\x04 \x03(\t\x12\x0f\n\x07\x65xclude\x18\x05 \x03(\t\x12\x12\n\nimage_size\x18\x06 \x01(\t'
)

_TRANSFORM = _descriptor.Descriptor(
    name='Transform',
    full_name='keypose.Transform',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='element',
            full_name='keypose.Transform.element',
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[],
    serialized_start=23,
    serialized_end=51,
)

_CAMERA = _descriptor.Descriptor(
    name='Camera',
    full_name='keypose.Camera',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='fx',
            full_name='keypose.Camera.fx',
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='fy',
            full_name='keypose.Camera.fy',
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='cx',
            full_name='keypose.Camera.cx',
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='cy',
            full_name='keypose.Camera.cy',
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='baseline',
            full_name='keypose.Camera.baseline',
            index=4,
            number=5,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='resx',
            full_name='keypose.Camera.resx',
            index=5,
            number=6,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='resy',
            full_name='keypose.Camera.resy',
            index=6,
            number=7,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[],
    serialized_start=53,
    serialized_end=155,
)

_TARGET_KEYPOINT = _descriptor.Descriptor(
    name='KeyPoint',
    full_name='keypose.Target.KeyPoint',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='u',
            full_name='keypose.Target.KeyPoint.u',
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='v',
            full_name='keypose.Target.KeyPoint.v',
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='x',
            full_name='keypose.Target.KeyPoint.x',
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='y',
            full_name='keypose.Target.KeyPoint.y',
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='z',
            full_name='keypose.Target.KeyPoint.z',
            index=4,
            number=5,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='visible',
            full_name='keypose.Target.KeyPoint.visible',
            index=5,
            number=6,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=True,
            default_value=float(1),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[],
    serialized_start=285,
    serialized_end=370,
)

_TARGET = _descriptor.Descriptor(
    name='Target',
    full_name='keypose.Target',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='transform',
            full_name='keypose.Target.transform',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='camera',
            full_name='keypose.Target.camera',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='keypoints',
            full_name='keypose.Target.keypoints',
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[
        _TARGET_KEYPOINT,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[],
    serialized_start=158,
    serialized_end=370,
)

_KEYTARGETS = _descriptor.Descriptor(
    name='KeyTargets',
    full_name='keypose.KeyTargets',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='kp_target',
            full_name='keypose.KeyTargets.kp_target',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='proj_targets',
            full_name='keypose.KeyTargets.proj_targets',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='mirrored',
            full_name='keypose.KeyTargets.mirrored',
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=True,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[],
    serialized_start=372,
    serialized_end=484,
)

_DATAPARAMS = _descriptor.Descriptor(
    name='DataParams',
    full_name='keypose.DataParams',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='resx',
            full_name='keypose.DataParams.resx',
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='resy',
            full_name='keypose.DataParams.resy',
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='num_kp',
            full_name='keypose.DataParams.num_kp',
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='camera',
            full_name='keypose.DataParams.camera',
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[],
    serialized_start=486,
    serialized_end=575,
)

_TFSET = _descriptor.Descriptor(
    name='TfSet',
    full_name='keypose.TfSet',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='name',
            full_name='keypose.TfSet.name',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b''.decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='common_dir',
            full_name='keypose.TfSet.common_dir',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b''.decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='train',
            full_name='keypose.TfSet.train',
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='val',
            full_name='keypose.TfSet.val',
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='exclude',
            full_name='keypose.TfSet.exclude',
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='image_size',
            full_name='keypose.TfSet.image_size',
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b''.decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[],
    serialized_start=577,
    serialized_end=683,
)

_TARGET_KEYPOINT.containing_type = _TARGET
_TARGET.fields_by_name['transform'].message_type = _TRANSFORM
_TARGET.fields_by_name['camera'].message_type = _CAMERA
_TARGET.fields_by_name['keypoints'].message_type = _TARGET_KEYPOINT
_KEYTARGETS.fields_by_name['kp_target'].message_type = _TARGET
_KEYTARGETS.fields_by_name['proj_targets'].message_type = _TARGET
_DATAPARAMS.fields_by_name['camera'].message_type = _CAMERA
DESCRIPTOR.message_types_by_name['Transform'] = _TRANSFORM
DESCRIPTOR.message_types_by_name['Camera'] = _CAMERA
DESCRIPTOR.message_types_by_name['Target'] = _TARGET
DESCRIPTOR.message_types_by_name['KeyTargets'] = _KEYTARGETS
DESCRIPTOR.message_types_by_name['DataParams'] = _DATAPARAMS
DESCRIPTOR.message_types_by_name['TfSet'] = _TFSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Transform = _reflection.GeneratedProtocolMessageType(
    'Transform',
    (_message.Message,),
    {
        'DESCRIPTOR': _TRANSFORM,
        '__module__': 'data_pb2'
        # @@protoc_insertion_point(class_scope:keypose.Transform)
    })
_sym_db.RegisterMessage(Transform)

Camera = _reflection.GeneratedProtocolMessageType(
    'Camera',
    (_message.Message,),
    {
        'DESCRIPTOR': _CAMERA,
        '__module__': 'data_pb2'
        # @@protoc_insertion_point(class_scope:keypose.Camera)
    })
_sym_db.RegisterMessage(Camera)

Target = _reflection.GeneratedProtocolMessageType(
    'Target',
    (_message.Message,),
    {
        'KeyPoint':
            _reflection.GeneratedProtocolMessageType(
                'KeyPoint',
                (_message.Message,),
                {
                    'DESCRIPTOR': _TARGET_KEYPOINT,
                    '__module__': 'data_pb2'
                    # @@protoc_insertion_point(class_scope:keypose.Target.KeyPoint)
                }),
        'DESCRIPTOR':
            _TARGET,
        '__module__': 'data_pb2'
        # @@protoc_insertion_point(class_scope:keypose.Target)
    })
_sym_db.RegisterMessage(Target)
_sym_db.RegisterMessage(Target.KeyPoint)

KeyTargets = _reflection.GeneratedProtocolMessageType(
    'KeyTargets',
    (_message.Message,),
    {
        'DESCRIPTOR': _KEYTARGETS,
        '__module__': 'data_pb2'
        # @@protoc_insertion_point(class_scope:keypose.KeyTargets)
    })
_sym_db.RegisterMessage(KeyTargets)

DataParams = _reflection.GeneratedProtocolMessageType(
    'DataParams',
    (_message.Message,),
    {
        'DESCRIPTOR': _DATAPARAMS,
        '__module__': 'data_pb2'
        # @@protoc_insertion_point(class_scope:keypose.DataParams)
    })
_sym_db.RegisterMessage(DataParams)

TfSet = _reflection.GeneratedProtocolMessageType(
    'TfSet',
    (_message.Message,),
    {
        'DESCRIPTOR': _TFSET,
        '__module__': 'data_pb2'
        # @@protoc_insertion_point(class_scope:keypose.TfSet)
    })
_sym_db.RegisterMessage(TfSet)

# @@protoc_insertion_point(module_scope)
