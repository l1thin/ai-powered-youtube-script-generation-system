from rag.retrievers.ingest_pipeline import ingest_data

vectordb = ingest_data()

retriever = vectordb.as_retriever(search_kwargs={"k": 5})

def retrieve(query):

    docs = retriever.invoke(query)

    return docs