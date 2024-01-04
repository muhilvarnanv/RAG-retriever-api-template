from langchain.vectorstores.pgvector import PGVector
from langchain.embeddings.vertexai import VertexAIEmbeddings

from src.config import get_database_connection_url

embeddings = VertexAIEmbeddings(model_name="textembedding-gecko@001")

store = PGVector(
    embedding_function=embeddings,
    collection_name="knowledge_base",
    connection_string=get_database_connection_url(),
)