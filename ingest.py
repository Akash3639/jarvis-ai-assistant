from vector_store import index, embedder

with open("data/sample_docs.txt") as f:
    text = f.read()

embedding = embedder.encode(text).tolist()
index.upsert([("doc1", embedding, {"text": text})])

print("Data indexed successfully")
