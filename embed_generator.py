from sentence_transformers import SentenceTransformer

model = SentenceTransformer('multi-qa-mpnet-base-dot-v1')
embeddings = model.encode(chunks, batch_size=64)
