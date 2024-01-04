from langchain.chains import RetrievalQA
from src.llm import get_model
from src.vector_store import store

llm = get_model()

knowledge_retriever = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=store.as_retriever()
)

