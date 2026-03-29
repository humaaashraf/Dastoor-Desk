import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# --- LOCAL PATHS ---
DB_DIR = "D:/dastoordesk/dastoor_db" 

# 1. Load Local Embeddings (No API needed)
# This uses your CPU/RAM to turn text into numbers
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_db = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)

# 2. Initialize Local Ollama (No API needed)
llm = ChatOllama(
    model="tinyllama",
    temperature=0.1
)

# 3. Your Legal Assistant Prompt
template = """You are the Dastoor Desk Legal Assistant. 
Use the provided context to answer the user's question. 
If you don't know, say you don't know.

Context: {context}
Question: {query}

Helpful Answer:"""

DASTOOR_PROMPT = PromptTemplate.from_template(template)

# 4. The Local-Only Ask Function
def ask_dastoor(user_query):
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})
    
    rag_chain = (
        {"context": retriever, "query": RunnablePassthrough()}
        | DASTOOR_PROMPT
        | llm
        | StrOutputParser()
    )
    
    return rag_chain.invoke(user_query)