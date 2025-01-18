from fastapi import FastAPI, HTTPException
from query_handler import QueryHandler
from intention_classifier import IntentionClassifier
from pydantic import BaseModel

app = FastAPI()
class UserQuery(BaseModel):
    query: str

# Inicializa los manejadores y el clasificador
query_handler = QueryHandler()

intention_classifier = IntentionClassifier()

@app.post("/interact/")
def interact(user_query: UserQuery):
    try:
        # Clasificar la intención del usuario
        intent = intention_classifier.classify_intention(user_query.query)
        
        if intent == "buscar_auto":
            result = query_handler.search_car(user_query.query)
            return {"intent": "buscar_auto", "result": result}
        
        elif intent == "calcular_financiamiento":
            payment_info = query_handler.financial_info(user_query.query)
            return {"intent": "calcular_financiamiento", "payment_info": payment_info}
        
        elif intent == "consultar_propuestas":
            proposals = query_handler.general_info(user_query.query)
            return {"intent": "consultar_propuestas", "information": proposals}
        
        else:
            raise HTTPException(status_code=400, detail="No se pudo determinar la intención del usuario.")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))