from rag.retrievers.script_retriever import retrieve

query = "how to write a strong youtube hook"

results = retrieve(query)

for r in results:

    print("\n----- RESULT -----\n")
    print(r.page_content)