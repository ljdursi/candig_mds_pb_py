from __future__ import print_function
import grpc
import metadata_pb2_grpc_server as metadata
import metadata_pb2 as schema


def clie():
    channel = grpc.insecure_channel('localhost:50051')
    stub = metadata.MetadataServiceStub(channel)

    print("--put individuals--")
    ind1 = schema.Individual(id="", description="First", name="CANDIG_001")
    ind2 = schema.Individual(id="", description="Second", name="CANDIG_002")
    stub.PutIndividual(ind1)
    stub.PutIndividual(ind2)
    print("--put biosample--")
    bs1 = schema.Biosample(id="", description="First", name="CANDIG_001_SPL")
    stub.PutBiosample(bs1)

    dmy = schema.SearchIndividualsRequest()
    print(stub.SearchIndividuals(dmy))


if __name__ == "__main__":
    clie()
