from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_chroma import Chroma
from langchain_core.messages import HumanMessage, SystemMessage
from prompts import blog_prompt, catalog_prompt, financial_prompt

class QueryHandler:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key="your_openai_api_key", temperature=1)
        self.embedding = OpenAIEmbeddings(openai_api_key="your_openai_api_key")
    
    def load_vectorstore(self, persist_directory):
        db = Chroma(persist_directory=persist_directory, embedding_function=self.embedding)
        return db
    def search_car(self, user_query):
        car_catalog = self.load_vectorstore("vectorstore\\catalog")
        car_catalog.as_retriever()
        cars = car_catalog.similarity_search(user_query)
        prompt = PromptTemplate(template=catalog_prompt(user_query, car_catalog))
        query = prompt.format(query=user_query, catalog=cars)
        return self.llm(query).content
    
    def general_info(self, user_query):
        blog_info = self.load_vectorstore("vectorstore\\blog")
        blog_info.as_retriever()
        info = blog_info.similarity_search(user_query)
        source_knowledge = "\n".join([x.page_content for x in info])
        prompt = blog_prompt(user_query, source_knowledge)
        sysmessage = "Eres un asistente que responde preguntas sobre la empresa Kavak en mexico, si no sabes la respuesta, responde con 'No se'."
        response = self.llm.invoke([HumanMessage(content=prompt), SystemMessage(content=sysmessage)])
        print(response)
        return response.content

    def financial_info(self, user_query):
        prompt = PromptTemplate(template=financial_prompt(user_query))
        query = prompt.format(query= user_query)
        return self.llm(query).content
