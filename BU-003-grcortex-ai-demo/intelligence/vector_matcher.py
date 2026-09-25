'''
(Handles Layer 2: Vector Semantic Intelligence & Policy Mapping)
'''
import os
import platform

# Fix for Windows PyTorch DLL loading issue
if platform.system() == "Windows":
    import ctypes
    from importlib.util import find_spec
    try:
        if (spec := find_spec("torch")) and spec.origin and os.path.exists(
            dll_path := os.path.join(os.path.dirname(spec.origin), "lib", "c10.dll")
        ):
            ctypes.CDLL(os.path.normpath(dll_path))
    except Exception:
        pass
    
from typing import List
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

class VectorPolicyEngine:
    def __init__(self):
        # Lightweight embedding model suitable for local runs
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.policy_database = []
        self.policy_embeddings = None

    def register_internal_policies(self, policies: List[str]):
        self.policy_database = policies
        self.policy_embeddings = self.model.encode(policies)

    def find_matching_policy(self, regulatory_clause: str, threshold: float = 0.50) -> List[dict]:
        if not self.policy_database:
            return []
        
        query_embedding = self.model.encode([regulatory_clause])
        similarities = cosine_similarity(query_embedding, self.policy_embeddings)[0]
        
        matches = []
        for idx, score in enumerate(similarities):
            if score >= threshold:
                matches.append({
                    "policy": self.policy_database[idx],
                    "confidence_score": float(score)
                })
        return sorted(matches, key=lambda x: x["confidence_score"], reverse=True)