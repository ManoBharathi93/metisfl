# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metisfl/proto/learner.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from metisfl.proto import metis_pb2 as metisfl_dot_proto_dot_metis__pb2
from metisfl.proto import model_pb2 as metisfl_dot_proto_dot_model__pb2
from metisfl.proto import service_common_pb2 as metisfl_dot_proto_dot_service__common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bmetisfl/proto/learner.proto\x12\x07metisfl\x1a\x19metisfl/proto/metis.proto\x1a\x19metisfl/proto/model.proto\x1a\"metisfl/proto/service_common.proto\"\xaa\x02\n\x14\x45valuateModelRequest\x12$\n\x05model\x18\x01 \x01(\x0b\x32\x0e.metisfl.ModelR\x05model\x12\x1d\n\nbatch_size\x18\x02 \x01(\rR\tbatchSize\x12\\\n\x12\x65valuation_dataset\x18\x03 \x03(\x0e\x32-.metisfl.EvaluateModelRequest.dataset_to_evalR\x11\x65valuationDataset\x12\x34\n\x07metrics\x18\x04 \x01(\x0b\x32\x1a.metisfl.EvaluationMetricsR\x07metrics\"9\n\x0f\x64\x61taset_to_eval\x12\x0c\n\x08TRAINING\x10\x00\x12\x08\n\x04TEST\x10\x01\x12\x0e\n\nVALIDATION\x10\x02\"T\n\x15\x45valuateModelResponse\x12;\n\x0b\x65valuations\x18\x01 \x01(\x0b\x32\x19.metisfl.ModelEvaluationsR\x0b\x65valuations\"\xc1\x01\n\x0eRunTaskRequest\x12@\n\x0f\x66\x65\x64\x65rated_model\x18\x01 \x01(\x0b\x32\x17.metisfl.FederatedModelR\x0e\x66\x65\x64\x65ratedModel\x12)\n\x04task\x18\x02 \x01(\x0b\x32\x15.metisfl.LearningTaskR\x04task\x12\x42\n\x0fhyperparameters\x18\x03 \x01(\x0b\x32\x18.metisfl.HyperparametersR\x0fhyperparameters\"1\n\x0fRunTaskResponse\x12\x1e\n\x03\x61\x63k\x18\x01 \x01(\x0b\x32\x0c.metisfl.AckR\x03\x61\x63k2\xd5\x02\n\x0eLearnerService\x12P\n\rEvaluateModel\x12\x1d.metisfl.EvaluateModelRequest\x1a\x1e.metisfl.EvaluateModelResponse\"\x00\x12n\n\x17GetServicesHealthStatus\x12\'.metisfl.GetServicesHealthStatusRequest\x1a(.metisfl.GetServicesHealthStatusResponse\"\x00\x12>\n\x07RunTask\x12\x17.metisfl.RunTaskRequest\x1a\x18.metisfl.RunTaskResponse\"\x00\x12\x41\n\x08ShutDown\x12\x18.metisfl.ShutDownRequest\x1a\x19.metisfl.ShutDownResponse\"\x00\x62\x06proto3')



_EVALUATEMODELREQUEST = DESCRIPTOR.message_types_by_name['EvaluateModelRequest']
_EVALUATEMODELRESPONSE = DESCRIPTOR.message_types_by_name['EvaluateModelResponse']
_RUNTASKREQUEST = DESCRIPTOR.message_types_by_name['RunTaskRequest']
_RUNTASKRESPONSE = DESCRIPTOR.message_types_by_name['RunTaskResponse']
_EVALUATEMODELREQUEST_DATASET_TO_EVAL = _EVALUATEMODELREQUEST.enum_types_by_name['dataset_to_eval']
EvaluateModelRequest = _reflection.GeneratedProtocolMessageType('EvaluateModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _EVALUATEMODELREQUEST,
  '__module__' : 'metisfl.proto.learner_pb2'
  # @@protoc_insertion_point(class_scope:metisfl.EvaluateModelRequest)
  })
_sym_db.RegisterMessage(EvaluateModelRequest)

EvaluateModelResponse = _reflection.GeneratedProtocolMessageType('EvaluateModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _EVALUATEMODELRESPONSE,
  '__module__' : 'metisfl.proto.learner_pb2'
  # @@protoc_insertion_point(class_scope:metisfl.EvaluateModelResponse)
  })
_sym_db.RegisterMessage(EvaluateModelResponse)

RunTaskRequest = _reflection.GeneratedProtocolMessageType('RunTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNTASKREQUEST,
  '__module__' : 'metisfl.proto.learner_pb2'
  # @@protoc_insertion_point(class_scope:metisfl.RunTaskRequest)
  })
_sym_db.RegisterMessage(RunTaskRequest)

RunTaskResponse = _reflection.GeneratedProtocolMessageType('RunTaskResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNTASKRESPONSE,
  '__module__' : 'metisfl.proto.learner_pb2'
  # @@protoc_insertion_point(class_scope:metisfl.RunTaskResponse)
  })
_sym_db.RegisterMessage(RunTaskResponse)

_LEARNERSERVICE = DESCRIPTOR.services_by_name['LearnerService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EVALUATEMODELREQUEST._serialized_start=131
  _EVALUATEMODELREQUEST._serialized_end=429
  _EVALUATEMODELREQUEST_DATASET_TO_EVAL._serialized_start=372
  _EVALUATEMODELREQUEST_DATASET_TO_EVAL._serialized_end=429
  _EVALUATEMODELRESPONSE._serialized_start=431
  _EVALUATEMODELRESPONSE._serialized_end=515
  _RUNTASKREQUEST._serialized_start=518
  _RUNTASKREQUEST._serialized_end=711
  _RUNTASKRESPONSE._serialized_start=713
  _RUNTASKRESPONSE._serialized_end=762
  _LEARNERSERVICE._serialized_start=765
  _LEARNERSERVICE._serialized_end=1106
# @@protoc_insertion_point(module_scope)
