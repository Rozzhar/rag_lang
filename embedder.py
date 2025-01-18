import os, bs4
from langchain_community.document_loaders import CSVLoader, PyPDFLoader, TextLoader, WebBaseLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from constants import OPENAI_KEY

class Embedder:
    def __init__(self):
        self.PATH = "vectorstore"
        self.createEmbeddingsDir()

    def createEmbeddingsDir(self):
        """
        Creates a directory to store the embeddings vectors
        """
        if not os.path.exists(self.PATH):
            os.mkdir(self.PATH)


    def storeDocEmbeds(self, file, original_filename):
        def get_file_extension(uploaded_file):
            file_extension =  os.path.splitext(uploaded_file)[1].lower()
            
            return file_extension
        
        text_splitter = RecursiveCharacterTextSplitter(
                chunk_size = 2000,
                chunk_overlap  = 100,
                length_function = len,
            )
        
        file_extension = get_file_extension(original_filename)

        if file_extension == ".csv":
            loader = CSVLoader(file_path=original_filename, encoding="utf-8")
            data = loader.load()
            persist_directory = self.PATH + "\\" + "catalog"

        elif file_extension == ".pdf":
            loader = PyPDFLoader(file_path=original_filename)  
            data = loader.load_and_split(text_splitter)
            persist_directory = self.PATH + "\\" + "pdf"
        
        elif file_extension == ".txt":
            loader = TextLoader(file_path=original_filename, encoding="utf-8")
            data = loader.load_and_split(text_splitter)
            persist_directory = self.PATH + "\\" + "text"
        
        elif original_filename.find("www") != -1 or original_filename.find("http") != -1 or original_filename.find("https") != -1 or original_filename.find(".com") != -1: 
            loader = WebBaseLoader(
                    web_paths=("https://www.kavak.com/mx/blog/sedes-de-kavak-en-mexico",),
                    bs_kwargs=dict(
                    parse_only=bs4.SoupStrainer(
                    class_=("post-content", "post-title", "post-header")
                                                )
                        ),
                    )
            data = loader.load()

        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_KEY)

        db  = Chroma.from_documents(data, embeddings, persist_directory=persist_directory)