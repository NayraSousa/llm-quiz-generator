from PyPDF2 import PdfReader
 
def loader(path):
    
    reader = PdfReader(path)
        
    text_load = ''.join(page.extract_text() for page in reader.pages)
        
    return text_load
    
    
load = loader("pdf/Learning LangChain-O'Reilly Media (2024).pdf")
        