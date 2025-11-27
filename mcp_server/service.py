import json
import os
from sentence_transformers import SentenceTransformer

class RulesSearchService:

    def __init__(self):
        self.sentence_model = SentenceTransformer("all-MiniLM-L6-v2")

        with open("../data/core_rules.json", "r") as f:
            self.rules_data = json.load(f)
        
        self.rules_text = [r["text"] for r in self.rules_data]
        self.rules_embeddings = self.sentence_model.encode(self.rules_text, convert_to_tensor=True) 
    
    def search_rules(self, query: str, top_k: int = 5):
        query_emb = self.sentence_model.encode([query], convert_to_tensor=True)
        scores = (query_emb @ self.rules_embeddings.T).cpu().tolist()[0]
        ranked = sorted(zip(scores, self.rules_data), key=lambda x: x[0], reverse=True)[:top_k]

        return [{"title": r["title"], "text": r["text"]} for _, r in ranked]