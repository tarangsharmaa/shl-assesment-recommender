from app.core.retriever import Retriever
from app.core.comparator import Comparator

retriever = Retriever()

documents = retriever.search("Java Developer")[:2]

comparator = Comparator()

response = comparator.compare(documents)

print(response)