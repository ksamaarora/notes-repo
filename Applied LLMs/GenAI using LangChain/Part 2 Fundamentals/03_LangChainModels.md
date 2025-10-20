LangCHain Models

The Model Component in LangChain is a crucial part of the framework, designed to facilitate interactions with various language models and embedding models.

It abstracts the complexity of working directly with different LLMs, chat models, and embedding models, providing a uniform interface to communicate with them. This makes it easier to build applications that rely on Al-generated text, text embeddings for similarity search, and retrieval-augmented generation (RAG).|

image 1

In LangChain, there are mainly **two types of models**:

* **Language Models (LLMs)** – take text as input and generate text as output (used to make chatbots)
* **Embedding Models** – take text as input and generate numerical vector embeddings (used for semantic search and similarity comparison to build say rag based applications).

---

Language models - closed source and open source models 

Embedding models - closed source and open source 

--- 

> ## Language models 

LLMs - General-purpose models that is used for raw text generation. They take a string(or plain text) as input and returns a string( plain text). These are traditionally older models and are not used much now.

Chat Models - Language models that are specialized for conversational tasks. They take a sequence of messages as inputs and return chat messages as outputs (as opposed to using plain text). These are traditionally newer models and used more in comparison to the LLMs.

| **Feature**          | **LLMs (Base Models)**                                                         | **Chat Models (Instruction-Tuned)**                                          |
| -------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| **Purpose**          | Free-form text generation                                                      | Optimized for multi-turn conversations                                       |
| **Training Data**    | General text corpora (books, articles)                                         | Fine-tuned on chat datasets (dialogues, user–assistant conversations)        |
| **Memory & Context** | No built-in memory                                                             | Supports structured conversation history                                     |
| **Role Awareness**   | No understanding of “user” and “assistant” roles                               | Understands “system”, “user”, and “assistant” roles                          |
| **Example Models**   | GPT-3, Llama-2-7B, Mistral-7B, OPT-1.3B                                        | GPT-4, GPT-3.5-Turbo, Llama-2-Chat, Mistral-Instruct, Claude                 |
| **Use Cases**        | Text generation, summarization, translation, creative writing, code generation | Conversational AI, chatbots, virtual assistants, customer support, AI tutors |


---

LLMs Models 

1. OpenAI
2. Anthropic
3. Google Gemini
4. HuggingFace

/Users/ksamaarora/Documents/Github/winterarc-solutions/Applied LLMs/GenAI using LangChain/Part 2 Fundamentals/LangChain Models/1.LLMs/1_llm_demo.py

from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result= llm.invoke("What is the capital on India?")

print(result)

---

/Users/ksamaarora/Documents/Github/winterarc-solutions/Applied LLMs/GenAI using LangChain/Part 2 Fundamentals/LangChain Models/2.ChatModels/1_chatmodel_openai.py

from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4')

result= model.invoke("What is the capital of India?")

print(result.content)


(venv) ksamaarora@Ksamas-MacBook-Pro LangChain Models % python 2.ChatModels/1_chatmodel_openai.py
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
content='The capital of India is New Delhi.' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 8, 'prompt_tokens': 14, 'total_tokens': 22, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_provider': 'openai', 'model_name': 'gpt-4-0613', 'system_fingerprint': None, 'id': 'chatcmpl-CSj7w04lVIOqgZooqtDGllUgo3LsK', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} id='lc_run--ce9b2281-a649-4b57-b11f-cca6526acd11-0' usage_metadata={'input_tokens': 14, 'output_tokens': 8, 'total_tokens': 22, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
(venv) ksamaarora@Ksamas-MacBook-Pro LangChain Models % python 2.ChatModels/1_chatmodel_openai.py
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
The capital of India is New Delhi.

---

temperature is a parameter that controls the randomness of a language model’s output.
It affects how creative or deterministic the responses are.
Lower values (0.0 – 0.3) → More deterministic and predictable.
Higher values (0.7 – 1.5) → More random, creative, and diverse.
| **Use Case**                                   | **Recommended Temperature** |
| ---------------------------------------------- | --------------------------- |
| Factual answers (math, code, facts)            | 0.0 – 0.3                   |
| Balanced response (general QA, explanations)   | 0.5 – 0.7                   |
| Creative writing, storytelling, jokes          | 0.9 – 1.2                   |
| Maximum randomness (wild ideas, brainstorming) | 1.5+                        |


max_completion_tokens are ..

What are tokens?

