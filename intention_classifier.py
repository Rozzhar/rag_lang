from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.prompts import PromptTemplate
from prompts import intention_prompt
import os
from constants import OPENAI_KEY

print(os.environ.get("OPENAI_API_KEY"))
class IntentionClassifier:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=OPENAI_KEY, temperature=0)

    def classify_intention(self, user_query):
        prompt = PromptTemplate(template=intention_prompt(user_query))
        query = prompt.format(query=user_query)
        response =self.llm.invoke([HumanMessage(content=query), SystemMessage(content="Responde solo con una de estas tres etiquetas: buscar_auto, calcular_financiamiento, consultar_propuestas.")])
        return response.content
