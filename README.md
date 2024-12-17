# Chat with Website Using RAG Pipeline

This project implements a Retrieval-Augmented Generation (RAG) pipeline to enable a chatbot that answers user queries based on content scraped from websites. The chatbot combines website data with a Large Language Model (LLM) to generate precise and context-aware responses.

---

## **Features**
- **Web Scraping**: Extracts content from static and dynamic websites.
- **Semantic Chunking**: Splits website content into meaningful chunks for embedding generation.
- **Embeddings Generation**: Uses Sentence Transformers to encode chunks into vector representations.
- **Vector Search**: Utilizes Pinecone as a vector database for efficient similarity search.
- **Query Handling**: Processes user queries and retrieves relevant website content.
- **Response Generation**: Uses OpenAI GPT models to generate context-aware responses.
- **API Integration**: Provides a FastAPI-based backend for query and response handling.

---

## **Technology Stack**
- **Python**: Core programming language.
- **Scrapy & Selenium**: For web scraping.
- **Sentence Transformers**: For embedding generation.
- **Pinecone**: For vector database management.
- **OpenAI GPT**: For generating natural language responses.
- **FastAPI**: Backend framework.
- **Docker**: For containerization and deployment.

---