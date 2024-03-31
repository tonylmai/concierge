import sys
import grpc

sys.path.append('../')  # Need to traverse one level up before we could traverse down

from concierge.concierge_pb2 import (
    ConciergeRequest,
)

from concierge.concierge_pb2_grpc import ConceirgeStub

channel = grpc.insecure_channel("localhost:50051")
client = ConceirgeStub(channel)
request = ConciergeRequest(question="What are things to do in San Francisco", 
                           preferences={"location": "San Francisco",
                            "start_date": "03/31/2024",
                            "end_date": "04/04/2024"})
response = client.Recommend(request)
print("\n".join(response.destinations))

