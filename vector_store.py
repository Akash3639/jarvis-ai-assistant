import os
import pinecone
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV")
)

index = pinecone.Index(os.getenv("PINECONE_INDEX"))
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def search_text(query):
    query_embedding = embedder.encode(query).tolist()
    result = index.query(vector=query_embedding, top_k=1, include_metadata=True)
    return result["matches"][0]["metadata"]["text"]
