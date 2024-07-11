from loader_pdf import loader
        
def splitter(text_load, chunk_size, chunk_overlap):
    
    text_split = []
    metadata=[]
        
    for i in range(0, len(text_load), chunk_size):
        start = i
        end = i + chunk_size
        if start != 0:
            start = start - chunk_overlap
            end =  end + chunk_overlap
        text_split.append(text_load[start:end])
        metadata.append({"name": "book-langchain", "partition": f"{i}"})
    
            
    return text_split, metadata

load = loader("pdf/Learning LangChain-O'Reilly Media (2024).pdf")
# print(splitter(load, 1150, 10))


                
        