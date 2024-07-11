import chromadb.utils.embedding_functions as embedding_functions
import ollama


def get_embeddings(documents, collection, metadata):
    
    for i, d in enumerate(documents):
        response = ollama.embeddings(model="mxbai-embed-large",
                                       prompt=d)
        
        collection.add(
                ids=[str(i)],
                embeddings=response['embedding'],
                documents=[d],
                metadatas=metadata[i]
    )
    
    return collection