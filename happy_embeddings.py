from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_voyageai import VoyageAIEmbeddings

voyageai = VoyageAIEmbeddings.model_validate(
    {
        "model": "voyage-4-large"
    }
)

vector_store = InMemoryVectorStore(embedding=voyageai)

# Load "Alice's Adventures in Wonderland" int separate lines (not as paragraphs)
lines = open("alice_in_wonderland.txt").read().splitlines()

# Sanitize lines by removing empty ones and give each line a unique ID.
lines = [line for line in lines if line.strip()]
line_ids = [str(i) for i in range(len(lines))]
lines_by_id = {line_id: line for line_id, line in zip(line_ids, lines)}

# Add each line as separate documents in the vector store and associate each document with its unique ID.
documents = [Document(page_content=line) for line_id, line in lines_by_id.items()]
documents_by_id = {line_id: doc for line_id, doc in zip(line_ids, documents)}

# Add em up...
vector_store.add_documents(documents=documents, ids=line_ids)

for result, score in vector_store.similarity_search_with_score("alice argues with a caterpillar", k=5):
    print(repr(result), score)
