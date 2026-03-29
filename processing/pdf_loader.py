import os
from langchain_community.document_loaders import PyPDFLoader

def load_all_laws(data_folder="data/"):
    # This list comes from your PDFS.docx [cite: 24]
    documents = []
    for file in os.listdir(data_folder):
        if file.endswith(".pdf"):
            print(f"Reading law document: {file}")
            loader = PyPDFLoader(os.path.join(data_folder, file))
            documents.extend(loader.load())
    return documents

if __name__ == "__main__":
    # Just a test to see if it reads your 'data' folder
    pages = load_all_laws()
    print(f"Successfully loaded {len(pages)} pages of legal text.")