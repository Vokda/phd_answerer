from langchain.llms import Ollama
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import GPT4AllEmbeddings
from langchain.vectorstores import Chroma
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import RetrievalQA
import time
import os

# load pdf
print('load pdf, this might take a while...')
phd_thesis = "./Avhandling_Mattias_Sj_.pdf"
pop_sum_eng = './pop_sum_eng.pdf'
loader = PyPDFLoader(phd_thesis)
data = loader.load()
print('done!')

# split into smaller pieces
print('split into smaller chunks')
text_spliter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
splits = text_spliter.split_documents(data)

# vectorize
print('vectorize, this might also take a while...')
vectorstore = Chroma.from_documents(documents=splits, embedding=GPT4AllEmbeddings())
print('done!')


print('start ollama')
ollama = Ollama(
        model="phd_answerer", 
        #verbose=True,
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
        )


while(True):
    question = input('Enter a question: ')
    print('vectorstore search')
    docs = vectorstore.similarity_search(question) #?

    print('qachain retrieval, thinking...')
    qachain=RetrievalQA.from_chain_type(ollama, retriever=vectorstore.as_retriever())
    start_time = time.time()
    qachain({'query': question})
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('\n')
    print(f"Time required to think: {elapsed_time} seconds")

print('bye!')
