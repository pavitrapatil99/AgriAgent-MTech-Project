
from utils.knowledge_retriever import (
    build_knowledge_index,
    retrieve_knowledge
)

print("Building AgriAgent knowledge index...")

total = build_knowledge_index()
print("Knowledge passages indexed:", total)

question = "How can a farmer improve soil health before planting tomatoes?"

print("\nSearching for relevant knowledge...")
results = retrieve_knowledge(question)

for i, item in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("Source:", item["source"])
    print("Passage:", item["text"])
