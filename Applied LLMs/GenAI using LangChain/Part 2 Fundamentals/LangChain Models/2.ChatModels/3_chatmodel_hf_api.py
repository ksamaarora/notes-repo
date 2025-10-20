from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

chat = ChatHuggingFace(
    llm=HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-R1",
        task="conversational",   # <-- important
        temperature=0.2,
        max_new_tokens=64,
    )
)

result = chat.invoke("What is the capital of India?")
print(result.content)  # Chat models return an AIMessage; use .content
