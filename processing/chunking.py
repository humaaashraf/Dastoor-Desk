from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_legal_text(documents):
    """Breaks long laws into chunks so the AI can find specific sections."""
    # Legal text needs a larger overlap (200) so that Section numbers 
    # and context aren't cut off mid-sentence.
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        add_start_index=True,
    )
    
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} legal search chunks.")
    return chunks

