from processing.pdf_loader import load_laws
from processing.chunking import get_text_chunks
from langchain_openai import OpenAIEmbeddings # Or use OllamaEmbeddings
from langchain_community.vectorstores import Chroma

def create_knowledge_base():
    # 1. Load the Legal PDFs [cite: 16]
    raw_docs = load_laws("data/")
    
    # 2. Break them into chunks 
    text_chunks = get_text_chunks(raw_docs)
    
    # 3. Store in Vector Database
    vector_db = Chroma.from_documents(
        documents=text_chunks,
        embedding=OpenAIEmbeddings(), # We will switch this to Ollama later
        persist_directory="vectorstore/"
    )
    print("Vector Database created and saved in 'vectorstore/' folder!")
    return vector_db

if __name__ == "__main__":
    create_knowledge_base()