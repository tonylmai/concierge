from concierge_pb2 import (
    Destination
)

import mocked as rag

def recommend(question: str, preferences: str) -> list[Destination]:
    """Return a list of destinations recommended by the Concierge (Reco) Engine"""
    result = rag.recommend(question=question, preferences=preferences)
    return result