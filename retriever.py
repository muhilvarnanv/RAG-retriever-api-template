from langchain.chains import RetrievalQA
from llm import get_model
from vector_store import store

llm = get_model()

knowledge_retriever = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=store.as_retriever()
)

