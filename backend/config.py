import os
from dotenv import load_dotenv

load_dotenv()

# Ollama Configuration
OLLAMA_BASE_URL = "http://localhost:11434"
LLM_MODEL = "llama3"  # Or "mistral" based on what you downloaded
EMBEDDING_MODEL = "nomic-embed-text"

# File Paths
DATA_PATH = "data/"
VECTORSTORE_PATH = "vectorstore/"