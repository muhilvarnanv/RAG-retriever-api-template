# RAG Retriever API 
A template code to build RAG retriever API quickly. 

## Requirement
- Python 3.8+
- pipenv
- postgres 15+
- pgvector

## Environment Variables
- DATABASE_URL
- OPENAI_API_KEY

## Setup 
- pipenv install
- source .env
- python inject_data.py #for onetime of data into vector store
- uvicorn main:app --reload

## DB setup in local
 - install postgres.app - https://postgresapp.com/downloads.html
 - download postgres15+
 - start a postgres server version 15+
 - Run the sql command in sql query interface(postgres client of your choice - pgadmin, postico)
   - `CREATE EXTENSION vector`
 
