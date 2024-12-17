query = "What is Stanford known for?"
query_embedding = model.encode([query])

result = index.query(query_embedding, top_k=5, include_metadata=True)
retrieved_chunks = [match['metadata']['text'] for match in result['matches']]
