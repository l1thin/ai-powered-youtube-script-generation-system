from langchain_community.vectorstores import Qdrant
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def create_vectorstore(chunks):

    vectordb = Qdrant.from_texts(
        texts=chunks,
        embedding=embedding,
        location=":memory:",
        collection_name="youtube_scripts"
    )

    return vectordb