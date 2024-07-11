import ollama

def search_llm(collection):
    prompt = "O que é langchain?"

    response = ollama.embeddings(
        prompt=prompt,
        model="mxbai-embed-large"
    )

    results = collection.query(
        query_embeddings=[response["embedding"]],
        n_results=3,
        where={"name": "book-langchain"}
    )
    
    distance = results['distances']
    print(distance)

    data = results['documents']
    print(data)

    output = ollama.generate(
        model="llama2",
        prompt=f"You are a chatbot assistant that responds in Portuguese. Using this data: {data}. Respond to this prompt: {prompt}"
    )

    print(output['response'])