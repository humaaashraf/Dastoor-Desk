import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# 1. Setup Paths
DATA_PATH = "D:/dastoordesk/data"
DB_DIR = "D:/dastoordesk/dastoor_db"

# 2. Use the "Mini" model (Only 80MB! Much better for your RAM)
print("🧠 Loading Light Embedding Model...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def create_database():
    # Load Documents
    print("📂 Loading Legal Documents...")
    documents = []
    for file in os.listdir(DATA_PATH):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(DATA_PATH, file))
            documents.extend(loader.load())

    # Split into Chunks
    print("✂️ Splitting into Legal Chunks...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)

    # Create Database
    print(f"🧬 Generating Embeddings for {len(chunks)} chunks...")
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_DIR
    )
    print(f"✅ Success! Knowledge base created at: {DB_DIR}")

if __name__ == "__main__":
    create_database()