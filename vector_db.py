import pinecone

pinecone.init(api_key="YOUR_PINECONE_API_KEY", environment="us-west1-gcp")
index = pinecone.Index("website-chat")

index.upsert([(str(i), embedding) for i, embedding in enumerate(embeddings)])
