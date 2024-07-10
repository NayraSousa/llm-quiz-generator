from loader_pdf import loader
from splitter_txt import splitter
from embeddings import get_embeddings

import chromadb


PATH = "pdf/Learning LangChain-O'Reilly Media (2024).pdf"
CHUNK_SIZE=1150
CHUNK_OVERLAP=10

def run():
    
    client = chromadb.PersistentClient(path="chromadb")
    collection = client.get_or_create_collection(name="vector-langchain") 

    text_load = loader(PATH)
    text_split = splitter(text_load, CHUNK_SIZE, CHUNK_OVERLAP)
    
    get_embeddings(text_split, collection)
    
if __name__ == '__main__':
    run()