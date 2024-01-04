from fastapi import FastAPI
from pydantic import BaseModel

from src.retriever import knowledge_retriever

app = FastAPI()


class RequestBody(BaseModel):
    query: str


@app.post("/run")
def run_query(request_body: RequestBody):
    query = request_body.query
    return {
     "answer": knowledge_retriever.run(query=query)
    }