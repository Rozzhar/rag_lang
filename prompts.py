

def intention_prompt(query):
    custom_prompt = f"""
        Dado el siguiente mensaje del usuario: "{query}", determina cuál es su intención:
        - "buscar_auto" si el usuario busca información sobre un coche.
        - "calcular_financiamiento" si el usuario quiere calcular un plan de financiamiento.
        - "consultar_propuestas" si el usuario desea saber sobre las propuestas de valor.
        Responde solo con una de estas tres etiquetas: buscar_auto, calcular_financiamiento, consultar_propuestas.
        """
    return custom_prompt
def blog_prompt(query, source_knowledge):

    custom_prompt =f"""
        Eres un asistente que responde preguntas sobre la empresa Kavak en mexico. Usando la siguiente informacion contesta la pegunta de la persona.
        Si no sabes la respuesta, responde con "No se".Usa 4 oraciones máximas y se conciso.
        Pregunta: {query}
        Contexto:{source_knowledge}
        Answer:
        """

    return custom_prompt

def catalog_prompt(query, catalog):
    custom_prompt = f"""
        El usuario busca un auto. Encuentra en el catálogo el auto que más se asemeje a esta descripción: {query}.
        Catálogo:
        {catalog}
        Responde con un mensaje amable mostrando todas las marcas, modelos, años, kilómetros y precios de los autos que apliquen.
        """
    return custom_prompt

def financial_prompt(query):
    custom_prompt = f"""
        Calcula el financiamiento de un auto usando {query}, donde se solicite:
        el precio del auto,
        el monto del enganche en porcentaje o cantidad,
        el plazo del financiamiento, debe estar entre 3 y 6 años

        Si se proporcionan todos los datos, realiza el cálculo del financiamiento mensual con la fórmula estándar de pago de préstamos, con una tasa de interés del 10%.

        Muestra como resultado solo las cantidades finales de:
        El monto financiado, el pago mensual y el total pagado al final del plazo.

        Si faltan datos, solicita los necesarios para realizar el cálculo
        """
    return custom_prompt