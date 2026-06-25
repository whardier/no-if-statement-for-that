from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_voyageai import VoyageAIEmbeddings

voyageai = VoyageAIEmbeddings.model_validate(
    {
        "model": "voyage-4-large"
    }
)

vector_store = InMemoryVectorStore(embedding=voyageai)

documents = [
    Document(page_content="See spot run."),
    Document(page_content="The quick brown fox jumps over the lazy dog."),
    Document(page_content="Jack and Jill went up the hill to fetch a pail of water."),
    Document(page_content="Humpty Dumpty sat on a wall, Humpty Dumpty had a great fall."),
    Document(page_content="Little Bo Peep has lost her sheep and doesn't know where to find them."),
    Document(page_content="Mary had a little lamb, its fleece was white as snow."),
    Document(page_content="Twinkle, twinkle, little star, how I wonder what you are."),
    Document(page_content="Baa, baa, black sheep, have you any wool?"),
]

vector_store.add_documents(documents=documents)

for result, score in vector_store.similarity_search_with_score("little star", k=2):
    print(result.page_content)
    print(score)
