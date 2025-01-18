# Chatbot Project

This project implements a chatbot using FastAPI that simulates a commercial agent for Kavak. The bot can:

Provide information about Kavak's value propositions.

Search for cars based on a catalog.

Calculate financing options for cars, considering price, down payment, interest rate, and term length.

The system leverages LangChain for intent classification and knowledge retrieval, OpenAI for embeddings, and Chroma for a vector database to index data from a CSV file and web content.

Features

Natural Language Understanding: Handles user queries to classify intents and provide relevant responses.

Car Catalog Search: Searches a car database to find matches for user queries.

Financing Calculation: Computes monthly payments based on user input.

Knowledge Retrieval: Uses embeddings and a vector database to fetch relevant data from the catalog and web content.

Installation

Prerequisites

Python 3.9+

Virtual environment (recommended)

Required libraries listed in requirements.txt

Steps

Clone the repository:

```
git clone https://github.com/yourusername/fastapi-chatbot.git
cd fastapi-chatbot
```
Create and activate a virtual environment:
```
python3 -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate   # For Windows
```
Install dependencies:
```
pip install -r requirements.txt
```
Set your OpenAI API key:
```
export OPENAI_API_KEY="your_openai_api_key"  # Linux/Mac
set OPENAI_API_KEY="your_openai_api_key"    # Windows
```
Run the FastAPI server:
```
uvicorn app:app --relod
```

