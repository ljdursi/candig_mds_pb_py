# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='metadata.proto',
  package='metadata',
  syntax='proto3',
  serialized_pb=_b('\n\x0emetadata.proto\x12\x08metadata\x1a\x1cgoogle/api/annotations.proto\"(\n\x18SearchIndividualsRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"-\n\x14GetIndividualRequest\x12\x15\n\rindividual_id\x18\x01 \x01(\t\"4\n\x15PutIndividualResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\"3\n\x14PutBiosampleResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\"F\n\x19SearchIndividualsResponse\x12)\n\x0bindividuals\x18\x01 \x03(\x0b\x32\x14.metadata.Individual\">\n\x17SearchBiosamplesRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rindividual_id\x18\x02 \x01(\t\"+\n\x13GetBiosampleRequest\x12\x14\n\x0c\x62iosample_id\x18\x01 \x01(\t\"C\n\x18SearchBiosamplesResponse\x12\'\n\nbiosamples\x18\x01 \x03(\x0b\x32\x13.metadata.Biosample\"\xe9\x01\n\nIndividual\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0f\n\x07\x63reated\x18\x05 \x01(\t\x12\x0f\n\x07updated\x18\x06 \x01(\t\x12\'\n\x07species\x18\x07 \x01(\x0b\x32\x16.metadata.OntologyTerm\x12#\n\x03sex\x18\x08 \x01(\x0b\x32\x16.metadata.OntologyTerm\x12(\n\nattributes\x18\n \x01(\x0b\x32\x14.metadata.Attributes\"\x80\x02\n\tBiosample\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\'\n\x07\x64isease\x18\x05 \x01(\x0b\x32\x16.metadata.OntologyTerm\x12\x0f\n\x07\x63reated\x18\x06 \x01(\t\x12\x0f\n\x07updated\x18\x07 \x01(\t\x12\x15\n\rindividual_id\x18\x08 \x01(\t\x12(\n\nattributes\x18\n \x01(\x0b\x32\x14.metadata.Attributes\x12$\n\x1cindividual_age_at_collection\x18\x0b \x01(\t\"\xa2\x02\n\x0e\x41ttributeValue\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x12\x15\n\x0bint64_value\x18\x02 \x01(\x03H\x00\x12\x15\n\x0bint32_value\x18\x03 \x01(\x05H\x00\x12\x14\n\nbool_value\x18\x04 \x01(\x08H\x00\x12\x16\n\x0c\x64ouble_value\x18\x05 \x01(\x01H\x00\x12/\n\rontology_term\x18\x07 \x01(\x0b\x32\x16.metadata.OntologyTermH\x00\x12*\n\nattributes\x18\x0c \x01(\x0b\x32\x14.metadata.AttributesH\x00\x12\x36\n\x0e\x61ttribute_list\x18\r \x01(\x0b\x32\x1c.metadata.AttributeValueListH\x00\x42\x07\n\x05value\">\n\x12\x41ttributeValueList\x12(\n\x06values\x18\x01 \x03(\x0b\x32\x18.metadata.AttributeValue\"\x85\x01\n\nAttributes\x12,\n\x04\x61ttr\x18\x01 \x03(\x0b\x32\x1e.metadata.Attributes.AttrEntry\x1aI\n\tAttrEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.metadata.AttributeValueList:\x02\x38\x01\"-\n\x0cOntologyTerm\x12\x0f\n\x07term_id\x18\x01 \x01(\t\x12\x0c\n\x04term\x18\x02 \x01(\t2\x9f\x06\n\x0fMetadataService\x12\x93\x01\n\x11SearchIndividuals\x12\".metadata.SearchIndividualsRequest\x1a#.metadata.SearchIndividualsResponse\"5\x82\xd3\xe4\x93\x02/\"*/CanDIG/metadata/v0.1.0/individuals/search:\x01*\x12\x8f\x01\n\x10SearchBiosamples\x12!.metadata.SearchBiosamplesRequest\x1a\".metadata.SearchBiosamplesResponse\"4\x82\xd3\xe4\x93\x02.\")/CanDIG/metadata/v0.1.0/biosamples/search:\x01*\x12\x81\x01\n\rGetIndividual\x12\x1e.metadata.GetIndividualRequest\x1a\x14.metadata.Individual\":\x82\xd3\xe4\x93\x02\x34\x12\x32/CanDIG/metadata/v0.1.0/individual/{individual_id}\x12|\n\x0cGetBiosample\x12\x1d.metadata.GetBiosampleRequest\x1a\x13.metadata.Biosample\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/CanDIG/metadata/v0.1.0/biosample/{biosample_id}\x12r\n\rPutIndividual\x12\x14.metadata.Individual\x1a\x1f.metadata.PutIndividualResponse\"*\x82\xd3\xe4\x93\x02$\x1a\"/CanDIG/metadata/v0.1.0/individual\x12n\n\x0cPutBiosample\x12\x13.metadata.Biosample\x1a\x1e.metadata.PutBiosampleResponse\")\x82\xd3\xe4\x93\x02#\x1a!/CanDIG/metadata/v0.1.0/biosampleb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_SEARCHINDIVIDUALSREQUEST = _descriptor.Descriptor(
  name='SearchIndividualsRequest',
  full_name='metadata.SearchIndividualsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='metadata.SearchIndividualsRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=58,
  serialized_end=98,
)


_GETINDIVIDUALREQUEST = _descriptor.Descriptor(
  name='GetIndividualRequest',
  full_name='metadata.GetIndividualRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='individual_id', full_name='metadata.GetIndividualRequest.individual_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=100,
  serialized_end=145,
)


_PUTINDIVIDUALRESPONSE = _descriptor.Descriptor(
  name='PutIndividualResponse',
  full_name='metadata.PutIndividualResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='metadata.PutIndividualResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='success', full_name='metadata.PutIndividualResponse.success', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_end=199,
)


_PUTBIOSAMPLERESPONSE = _descriptor.Descriptor(
  name='PutBiosampleResponse',
  full_name='metadata.PutBiosampleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='metadata.PutBiosampleResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='success', full_name='metadata.PutBiosampleResponse.success', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=201,
  serialized_end=252,
)


_SEARCHINDIVIDUALSRESPONSE = _descriptor.Descriptor(
  name='SearchIndividualsResponse',
  full_name='metadata.SearchIndividualsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='individuals', full_name='metadata.SearchIndividualsResponse.individuals', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=254,
  serialized_end=324,
)


_SEARCHBIOSAMPLESREQUEST = _descriptor.Descriptor(
  name='SearchBiosamplesRequest',
  full_name='metadata.SearchBiosamplesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='metadata.SearchBiosamplesRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='individual_id', full_name='metadata.SearchBiosamplesRequest.individual_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=326,
  serialized_end=388,
)


_GETBIOSAMPLEREQUEST = _descriptor.Descriptor(
  name='GetBiosampleRequest',
  full_name='metadata.GetBiosampleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='biosample_id', full_name='metadata.GetBiosampleRequest.biosample_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=390,
  serialized_end=433,
)


_SEARCHBIOSAMPLESRESPONSE = _descriptor.Descriptor(
  name='SearchBiosamplesResponse',
  full_name='metadata.SearchBiosamplesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='biosamples', full_name='metadata.SearchBiosamplesResponse.biosamples', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=435,
  serialized_end=502,
)


_INDIVIDUAL = _descriptor.Descriptor(
  name='Individual',
  full_name='metadata.Individual',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='metadata.Individual.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='metadata.Individual.dataset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='metadata.Individual.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='metadata.Individual.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created', full_name='metadata.Individual.created', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated', full_name='metadata.Individual.updated', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='species', full_name='metadata.Individual.species', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sex', full_name='metadata.Individual.sex', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='metadata.Individual.attributes', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=505,
  serialized_end=738,
)


_BIOSAMPLE = _descriptor.Descriptor(
  name='Biosample',
  full_name='metadata.Biosample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='metadata.Biosample.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='metadata.Biosample.dataset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='metadata.Biosample.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='metadata.Biosample.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disease', full_name='metadata.Biosample.disease', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created', full_name='metadata.Biosample.created', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated', full_name='metadata.Biosample.updated', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='individual_id', full_name='metadata.Biosample.individual_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='metadata.Biosample.attributes', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='individual_age_at_collection', full_name='metadata.Biosample.individual_age_at_collection', index=9,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=741,
  serialized_end=997,
)


_ATTRIBUTEVALUE = _descriptor.Descriptor(
  name='AttributeValue',
  full_name='metadata.AttributeValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='string_value', full_name='metadata.AttributeValue.string_value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int64_value', full_name='metadata.AttributeValue.int64_value', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int32_value', full_name='metadata.AttributeValue.int32_value', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='metadata.AttributeValue.bool_value', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='metadata.AttributeValue.double_value', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ontology_term', full_name='metadata.AttributeValue.ontology_term', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='metadata.AttributeValue.attributes', index=6,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attribute_list', full_name='metadata.AttributeValue.attribute_list', index=7,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='value', full_name='metadata.AttributeValue.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1000,
  serialized_end=1290,
)


_ATTRIBUTEVALUELIST = _descriptor.Descriptor(
  name='AttributeValueList',
  full_name='metadata.AttributeValueList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='metadata.AttributeValueList.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1292,
  serialized_end=1354,
)


_ATTRIBUTES_ATTRENTRY = _descriptor.Descriptor(
  name='AttrEntry',
  full_name='metadata.Attributes.AttrEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='metadata.Attributes.AttrEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='metadata.Attributes.AttrEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1417,
  serialized_end=1490,
)

_ATTRIBUTES = _descriptor.Descriptor(
  name='Attributes',
  full_name='metadata.Attributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attr', full_name='metadata.Attributes.attr', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ATTRIBUTES_ATTRENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1357,
  serialized_end=1490,
)


_ONTOLOGYTERM = _descriptor.Descriptor(
  name='OntologyTerm',
  full_name='metadata.OntologyTerm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='term_id', full_name='metadata.OntologyTerm.term_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='term', full_name='metadata.OntologyTerm.term', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1492,
  serialized_end=1537,
)

_SEARCHINDIVIDUALSRESPONSE.fields_by_name['individuals'].message_type = _INDIVIDUAL
_SEARCHBIOSAMPLESRESPONSE.fields_by_name['biosamples'].message_type = _BIOSAMPLE
_INDIVIDUAL.fields_by_name['species'].message_type = _ONTOLOGYTERM
_INDIVIDUAL.fields_by_name['sex'].message_type = _ONTOLOGYTERM
_INDIVIDUAL.fields_by_name['attributes'].message_type = _ATTRIBUTES
_BIOSAMPLE.fields_by_name['disease'].message_type = _ONTOLOGYTERM
_BIOSAMPLE.fields_by_name['attributes'].message_type = _ATTRIBUTES
_ATTRIBUTEVALUE.fields_by_name['ontology_term'].message_type = _ONTOLOGYTERM
_ATTRIBUTEVALUE.fields_by_name['attributes'].message_type = _ATTRIBUTES
_ATTRIBUTEVALUE.fields_by_name['attribute_list'].message_type = _ATTRIBUTEVALUELIST
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['string_value'])
_ATTRIBUTEVALUE.fields_by_name['string_value'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['int64_value'])
_ATTRIBUTEVALUE.fields_by_name['int64_value'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['int32_value'])
_ATTRIBUTEVALUE.fields_by_name['int32_value'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['bool_value'])
_ATTRIBUTEVALUE.fields_by_name['bool_value'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['double_value'])
_ATTRIBUTEVALUE.fields_by_name['double_value'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['ontology_term'])
_ATTRIBUTEVALUE.fields_by_name['ontology_term'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['attributes'])
_ATTRIBUTEVALUE.fields_by_name['attributes'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['attribute_list'])
_ATTRIBUTEVALUE.fields_by_name['attribute_list'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUELIST.fields_by_name['values'].message_type = _ATTRIBUTEVALUE
_ATTRIBUTES_ATTRENTRY.fields_by_name['value'].message_type = _ATTRIBUTEVALUELIST
_ATTRIBUTES_ATTRENTRY.containing_type = _ATTRIBUTES
_ATTRIBUTES.fields_by_name['attr'].message_type = _ATTRIBUTES_ATTRENTRY
DESCRIPTOR.message_types_by_name['SearchIndividualsRequest'] = _SEARCHINDIVIDUALSREQUEST
DESCRIPTOR.message_types_by_name['GetIndividualRequest'] = _GETINDIVIDUALREQUEST
DESCRIPTOR.message_types_by_name['PutIndividualResponse'] = _PUTINDIVIDUALRESPONSE
DESCRIPTOR.message_types_by_name['PutBiosampleResponse'] = _PUTBIOSAMPLERESPONSE
DESCRIPTOR.message_types_by_name['SearchIndividualsResponse'] = _SEARCHINDIVIDUALSRESPONSE
DESCRIPTOR.message_types_by_name['SearchBiosamplesRequest'] = _SEARCHBIOSAMPLESREQUEST
DESCRIPTOR.message_types_by_name['GetBiosampleRequest'] = _GETBIOSAMPLEREQUEST
DESCRIPTOR.message_types_by_name['SearchBiosamplesResponse'] = _SEARCHBIOSAMPLESRESPONSE
DESCRIPTOR.message_types_by_name['Individual'] = _INDIVIDUAL
DESCRIPTOR.message_types_by_name['Biosample'] = _BIOSAMPLE
DESCRIPTOR.message_types_by_name['AttributeValue'] = _ATTRIBUTEVALUE
DESCRIPTOR.message_types_by_name['AttributeValueList'] = _ATTRIBUTEVALUELIST
DESCRIPTOR.message_types_by_name['Attributes'] = _ATTRIBUTES
DESCRIPTOR.message_types_by_name['OntologyTerm'] = _ONTOLOGYTERM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchIndividualsRequest = _reflection.GeneratedProtocolMessageType('SearchIndividualsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHINDIVIDUALSREQUEST,
  __module__ = 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:metadata.SearchIndividualsRequest)
  ))
_sym_db.RegisterMessage(SearchIndividualsRequest)

GetIndividualRequest = _reflection.GeneratedProtocolMessageType('GetIndividualRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETINDIVIDUALREQUEST,
  __module__ = 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:metadata.GetIndividualRequest)
  ))
_sym_db.RegisterMessage(GetIndividualRequest)

PutIndividualResponse = _reflection.GeneratedProtocolMessageType('PutIndividualResponse', (_message.Message,), dict(
  DESCRIPTOR = _PUTINDIVIDUALRESPONSE,
  __module__ = 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:metadata.PutIndividualResponse)
  ))
_sym_db.RegisterMessage(PutIndividualResponse)

PutBiosampleResponse = _reflection.GeneratedProtocolMessageType('PutBiosampleResponse', (_message.Message,), dict(
  DESCRIPTOR = _PUTBIOSAMPLERESPONSE,
  __module__ = 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:metadata.PutBiosampleResponse)
  ))
_sym_db.RegisterMessage(PutBiosampleResponse)

SearchIndividualsResponse = _reflection.GeneratedProtocolMessageType('SearchIndividualsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHINDIVIDUALSRESPONSE,
  __module__ = 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:metadata.SearchIndividualsResponse)
  ))
_sym_db.RegisterMessage(SearchIndividualsResponse)

SearchBiosamplesRequest = _reflection.GeneratedProtocolMessageType('SearchBiosamplesRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHBIOSAMPLESREQUEST,
  __module__ = 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:metadata.SearchBiosamplesRequest)
  ))
_sym_db.RegisterMessage(SearchBiosamplesRequest)

GetBiosampleRequest = _reflection.GeneratedProtocolMessageType('GetBiosampleRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBIOSAMPLEREQUEST,
  __module__ = 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:metadata.GetBiosampleRequest)
  ))
_sym_db.RegisterMessage(GetBiosampleRequest)

SearchBiosamplesResponse = _reflection.GeneratedProtocolMessageType('SearchBiosamplesResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHBIOSAMPLESRESPONSE,
  __module__ = 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:metadata.SearchBiosamplesResponse)
  ))
_sym_db.RegisterMessage(SearchBiosamplesResponse)

Individual = _reflection.GeneratedProtocolMessageType('Individual', (_message.Message,), dict(
  DESCRIPTOR = _INDIVIDUAL,
  __module__ = 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:metadata.Individual)
  ))
_sym_db.RegisterMessage(Individual)

Biosample = _reflection.GeneratedProtocolMessageType('Biosample', (_message.Message,), dict(
  DESCRIPTOR = _BIOSAMPLE,
  __module__ = 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:metadata.Biosample)
  ))
_sym_db.RegisterMessage(Biosample)

AttributeValue = _reflection.GeneratedProtocolMessageType('AttributeValue', (_message.Message,), dict(
  DESCRIPTOR = _ATTRIBUTEVALUE,
  __module__ = 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:metadata.AttributeValue)
  ))
_sym_db.RegisterMessage(AttributeValue)

AttributeValueList = _reflection.GeneratedProtocolMessageType('AttributeValueList', (_message.Message,), dict(
  DESCRIPTOR = _ATTRIBUTEVALUELIST,
  __module__ = 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:metadata.AttributeValueList)
  ))
_sym_db.RegisterMessage(AttributeValueList)

Attributes = _reflection.GeneratedProtocolMessageType('Attributes', (_message.Message,), dict(

  AttrEntry = _reflection.GeneratedProtocolMessageType('AttrEntry', (_message.Message,), dict(
    DESCRIPTOR = _ATTRIBUTES_ATTRENTRY,
    __module__ = 'metadata_pb2'
    # @@protoc_insertion_point(class_scope:metadata.Attributes.AttrEntry)
    ))
  ,
  DESCRIPTOR = _ATTRIBUTES,
  __module__ = 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:metadata.Attributes)
  ))
_sym_db.RegisterMessage(Attributes)
_sym_db.RegisterMessage(Attributes.AttrEntry)

OntologyTerm = _reflection.GeneratedProtocolMessageType('OntologyTerm', (_message.Message,), dict(
  DESCRIPTOR = _ONTOLOGYTERM,
  __module__ = 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:metadata.OntologyTerm)
  ))
_sym_db.RegisterMessage(OntologyTerm)


_ATTRIBUTES_ATTRENTRY.has_options = True
_ATTRIBUTES_ATTRENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))

_METADATASERVICE = _descriptor.ServiceDescriptor(
  name='MetadataService',
  full_name='metadata.MetadataService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1540,
  serialized_end=2339,
  methods=[
  _descriptor.MethodDescriptor(
    name='SearchIndividuals',
    full_name='metadata.MetadataService.SearchIndividuals',
    index=0,
    containing_service=None,
    input_type=_SEARCHINDIVIDUALSREQUEST,
    output_type=_SEARCHINDIVIDUALSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002/\"*/CanDIG/metadata/v0.1.0/individuals/search:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='SearchBiosamples',
    full_name='metadata.MetadataService.SearchBiosamples',
    index=1,
    containing_service=None,
    input_type=_SEARCHBIOSAMPLESREQUEST,
    output_type=_SEARCHBIOSAMPLESRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002.\")/CanDIG/metadata/v0.1.0/biosamples/search:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='GetIndividual',
    full_name='metadata.MetadataService.GetIndividual',
    index=2,
    containing_service=None,
    input_type=_GETINDIVIDUALREQUEST,
    output_type=_INDIVIDUAL,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0024\0222/CanDIG/metadata/v0.1.0/individual/{individual_id}')),
  ),
  _descriptor.MethodDescriptor(
    name='GetBiosample',
    full_name='metadata.MetadataService.GetBiosample',
    index=3,
    containing_service=None,
    input_type=_GETBIOSAMPLEREQUEST,
    output_type=_BIOSAMPLE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0022\0220/CanDIG/metadata/v0.1.0/biosample/{biosample_id}')),
  ),
  _descriptor.MethodDescriptor(
    name='PutIndividual',
    full_name='metadata.MetadataService.PutIndividual',
    index=4,
    containing_service=None,
    input_type=_INDIVIDUAL,
    output_type=_PUTINDIVIDUALRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002$\032\"/CanDIG/metadata/v0.1.0/individual')),
  ),
  _descriptor.MethodDescriptor(
    name='PutBiosample',
    full_name='metadata.MetadataService.PutBiosample',
    index=5,
    containing_service=None,
    input_type=_BIOSAMPLE,
    output_type=_PUTBIOSAMPLERESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002#\032!/CanDIG/metadata/v0.1.0/biosample')),
  ),
])
_sym_db.RegisterServiceDescriptor(_METADATASERVICE)

DESCRIPTOR.services_by_name['MetadataService'] = _METADATASERVICE

# @@protoc_insertion_point(module_scope)
