from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

from vector_store import store


def run():
    loader = TextLoader("knowledge.txt")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    store.add_documents(docs)

run()