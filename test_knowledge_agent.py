
from agents.knowledge_agent import get_agricultural_guidance
question = "How can I manage water stress in my crop?"
assessment = "No specific satellite or weather assessment provided."

result = get_agricultural_guidance(question, assessment)

print("\nTopic:", result["topic"])
print("\nGuidance:\n")
print(result["guidance"])
