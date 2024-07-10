import ollama

def search_llm(collection):
    prompt = "O que é grafana?"

    response = ollama.embeddings(
        prompt=prompt,
        model="mxbai-embed-large"
    )

    results = collection.query(
        query_embeddings=[response["embedding"]],
        n_results=1
    )

    data = results['documents'][0][0]

    output = ollama.generate(
        model="llama2",
        prompt=f"You are a chatbot assistant that responds in Portuguese. Using this data: {data}. Respond to this prompt: {prompt}"
    )

    print(output['response'])