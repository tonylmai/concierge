""" This is a micro-service that provides gRPC methods for recommending a complete
  itinerary based on user's input (list of locations and context from user's preferences)"""
from concurrent import futures
import sys
import grpc

sys.path.append('../')  # Need to traverse one level up before we could traverse down

from concierge_pb2 import (
    RecommendationResponse,
)

import concierge_pb2_grpc
import service as svc


class ConciergeService(concierge_pb2_grpc.ConciergeServicer):
    def Recommend(self, request, context):
        """Recommend a complete itinerary based on user's input (list of locations and context from user's preferences)"""
        if not request.question:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "question is empty")

        print(f"Recommendation request for user {request.user_id} with\nQuestion: {request.question}\nPreferences: {request.preferences}")
        dests = svc.recommend(ctx=request.ctx, question=request.question)
        return RecommendationResponse(destinations=dests)

def serve():
    """Bring up the server and begin serving"""
    host = "[::]"
    port = 50051
    print(f"Starting server at {host}:{port}...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    concierge_pb2_grpc.add_ConciergeServicer_to_server(
        ConciergeService(), server
    )
    server.add_insecure_port(f"{host}:{port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
