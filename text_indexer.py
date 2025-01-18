from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.messages import HumanMessage, SystemMessage
from prompts import blog_prompt
from constants import OPENAI_KEY

#TODO: Implement chat history

llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=OPENAI_KEY, temperature=0)
embedder = OpenAIEmbeddings(openai_api_key=OPENAI_KEY)

db = Chroma(persist_directory="vectorstore\\blog", embedding_function=embedder)
retriever = db.as_retriever()


def augment_prompt(query: str):
    # get top 3 results from knowledge base
    results = db.similarity_search(query)
    # get the text from the results
    source_knowledge = "\n".join([x.page_content for x in results])
    # feed into an augmented prompt
    augmented_prompt = blog_prompt(query, source_knowledge)
    return augmented_prompt

# create a new user prompt
prompt = HumanMessage(
    content=augment_prompt("¿Qué beneficios ofrece Kavak?")
)
# add to messages
sysmessage = "Eres un asistente que responde preguntas sobre la empresa Kavak en mexico, si no sabes la respuesta, responde con 'No se'."

res = llm.invoke([HumanMessage(content=prompt.content), SystemMessage(content=sysmessage)])

print(res.content)