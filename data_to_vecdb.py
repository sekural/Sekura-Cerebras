import os
from cerebras.cloud.sdk import Cerebras
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb

def vec_db():
    DATA_PATH = r"data"
    CHROMA_PATH = r"chroma_db"
    
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    
    collection = chroma_client.get_or_create_collection(name="OWASP")
    
    # loading the document
    
    loader = PyPDFDirectoryLoader(DATA_PATH)
    
    raw_documents = loader.load()
    
    # splitting the document
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        is_separator_regex=False,
    )
    
    chunks = text_splitter.split_documents(raw_documents)
    
    # preparing to be added in chromadb
    
    documents = []
    metadata = []
    ids = []
    
    i = 0
    
    for chunk in chunks:
        documents.append(chunk.page_content)
        ids.append("ID"+str(i))
        metadata.append(chunk.metadata)    
        i += 1

 
    collection.upsert(
        documents=documents,
        metadatas=metadata,
        ids=ids
    )

if __name__ == "__main__":
    vec_db()
