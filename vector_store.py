from langchain.vectorstores.pgvector import PGVector
from langchain.embeddings.vertexai import VertexAIEmbeddings

from config import get_database_connection_url, get_collection_name

embeddings = VertexAIEmbeddings(model_name="textembedding-gecko@001")

store = PGVector(
    embedding_function=embeddings,
    collection_name=get_collection_name(),
    connection_string=get_database_connection_url(),
)