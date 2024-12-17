import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
context = " ".join(retrieved_chunks)
prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=300
)
print(response['choices'][0]['text'])
