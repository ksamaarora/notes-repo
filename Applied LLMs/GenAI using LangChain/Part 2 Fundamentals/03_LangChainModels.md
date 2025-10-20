# LangChain Models

The **Model** component in LangChain is a crucial part of the framework, designed to facilitate interactions with various **language models** and **embedding models**.

It abstracts the complexity of working directly with different LLMs, chat models, and embedding models, providing a **uniform interface** to communicate with them. This makes it easier to build applications that rely on **AI-generated text**, **text embeddings** for similarity search, and **retrieval-augmented generation (RAG)**.

> *Diagram placeholder:* **image 1** (insert your visual here)

---

In LangChain, there are mainly **two types of models**:

* **Language Models (LLMs)** – take text as input and generate text as output (used to make chatbots and many other tasks).
* **Embedding Models** – take text as input and generate numerical vector embeddings (used for semantic search and similarity comparison; foundational for RAG).

---

## Contents

* [LLMs vs Chat Models](#llms-vs-chat-models)
* [Open-Source vs Closed-Source Models](#open-source-vs-closed-source-models)
* [Parameters: temperature, tokens](#parameters-temperature-tokens)
* [Embedding Models](#embedding-models)
* [Practical Demos (code)](#practical-demos-code)
* [Common Pitfalls & Fixes](#common-pitfalls--fixes)
* [FAQ](#faq)

---

## LLMs vs Chat Models

**LLMs** – General-purpose models used for raw text generation. They take a string (plain text) as input and return a string (plain text). These expose a classic, simpler interface.

**Chat Models** – Language models specialized for conversational tasks. They take a **sequence of messages** as input and return **chat messages** as output (with roles like `system`, `user`, `assistant`). These are commonly used today for multi-turn chat.

| **Feature**          | **LLMs (Base Models)**                                                         | **Chat Models (Instruction-Tuned)**                                          |
| -------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| **Purpose**          | Free-form text generation                                                      | Optimized for multi-turn conversations                                       |
| **Training Data**    | General text corpora (books, articles)                                         | Fine-tuned on chat datasets (dialogues, user–assistant conversations)        |
| **Memory & Context** | No built-in message structure                                                  | Supports structured conversation history                                     |
| **Role Awareness**   | No understanding of “user/assistant” roles                                     | Understands `system`, `user`, and `assistant` roles                          |
| **Example Models**   | GPT-3, Llama-2-7B, Mistral-7B, OPT-1.3B                                        | GPT-4, GPT-3.5-Turbo, Llama-2-Chat, Mistral-Instruct, Claude                 |
| **Use Cases**        | Text generation, summarization, translation, creative writing, code generation | Conversational AI, chatbots, virtual assistants, customer support, AI tutors |

---

## Open-Source vs Closed-Source Models

Open-source language models are freely available AI models that you can download, modify, fine-tune, and deploy on your own infrastructure. Unlike closed-source models such as OpenAI’s GPT-4, Anthropic’s Claude, or Google’s Gemini, open-source models allow full control and customization.

| **Feature**       | **Open-Source Models**                | **Closed-Source Models**          |
| ----------------- | ------------------------------------- | --------------------------------- |
| **Cost**          | Free to run (infra cost only)         | Pay per token/API                 |
| **Control**       | Full control, fine-tune, custom infra | Limited control, provider runtime |
| **Data Privacy**  | Can run entirely on-prem              | Data hits vendor servers          |
| **Customization** | Full fine-tuning freedom              | Often limited/managed fine-tuning |
| **Deployment**    | Self-host or any cloud                | Must use provider API             |

**Popular OSS models**

| **Model**          | **Developer** | **Params** | **Notes**                           |
| ------------------ | ------------- | ---------- | ----------------------------------- |
| LLaMA-2-7B/13B/70B | Meta          | 7B–70B     | General purpose                     |
| Mixtral-8x7B (MoE) | Mistral       | 8×7B       | Fast & efficient Mixture-of-Experts |
| Mistral-7B         | Mistral       | 7B         | Strong small model                  |
| Falcon-7B/40B      | TII           | 7B–40B     | High-speed inference                |
| BLOOM-176B         | BigScience    | 176B       | Multilingual                        |
| GPT-NeoX-20B       | EleutherAI    | 20B        | Large general-purpose               |
| StableLM           | Stability     | 3B–7B      | Compact chat                        |

**Where to find them?**
Hugging Face – the largest hub for open-source LLMs.

---

## Parameters: temperature, tokens

**`temperature`** controls the randomness/creativity of the output.

* Lower values (0.0–0.3) → more deterministic and predictable.
* Higher values (0.7–1.5) → more random, creative, and diverse.

| **Use Case**                                   | **Recommended Temperature** |
| ---------------------------------------------- | --------------------------- |
| Factual answers (math, code, facts)            | 0.0 – 0.3                   |
| Balanced response (general QA, explanations)   | 0.5 – 0.7                   |
| Creative writing, storytelling, jokes          | 0.9 – 1.2                   |
| Maximum randomness (wild ideas, brainstorming) | 1.5+                        |

**Tokens & lengths**

* **What’s a token?** A small chunk of text (sub-word pieces). Most providers count billing and limits in tokens rather than characters.
* **`max_new_tokens` (HF):** The **maximum number of tokens** the model is allowed to **generate in the response**. It does **not** count your prompt.
* **`max_completion_tokens` (OpenAI Chat):** Same idea as above for OpenAI chat models — caps the **generated** part only.
* **Context window (e.g., 8k/32k):** The **total capacity** of the model for **prompt + response together**. If your prompt is very long, you must lower the allowed output or shorten the prompt to fit within the window.

---

## Embedding Models

Embedding models convert text to **vectors** so you can do:

* **Semantic search** (nearest neighbors)
* **Similarity** (cosine similarity)
* **RAG** (retrieve relevant chunks first, then generate)

Common choices:

* **OpenAI**: `text-embedding-3-small`, `text-embedding-3-large`
* **Hugging Face**: `sentence-transformers/all-MiniLM-L6-v2` (great & fast baseline)

---

## Practical Demos (code)

> Use the relative links below from this README’s folder.

### 1) LLM (string in → string out)

**OpenAI LLM demo**
`[1.LLMs/1_llm_demo.py](1.LLMs/1_llm_demo.py)`

```python
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")
result = llm.invoke("What is the capital of India?")
print(result)  # returns a plain str
```

### 2) Chat Models (messages in → message out)

**OpenAI Chat demo**
`[2.ChatModels/1_chatmodel_openai.py](2.ChatModels/1_chatmodel_openai.py)`

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.3, max_completion_tokens=10)
result = model.invoke("Write a 5 line poem on monsoon in Mumbai.")
print(result.content)  # AIMessage.content
```

**DeepSeek-R1 via Hugging Face (conversational task)**
`[2.ChatModels/3_chatmodel_hf_api.py](2.ChatModels/3_chatmodel_hf_api.py)`

```python
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

chat = ChatHuggingFace(
    llm=HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-R1",
        task="conversational",      # IMPORTANT: this model is "conversational" on HF
        temperature=0.2,
        max_new_tokens=64,
    )
)

result = chat.invoke("What is the capital of India?")
print(result.content)
```

### 3) Embeddings (query + docs)

**OpenAI: embed a single query**
`[3.EmbeddedModels/1_embedding_openai_query.py](3.EmbeddedModels/1_embedding_openai_query.py)`

```python
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)
vec = embedding.embed_query("Delhi is the capital of India")
print(vec)  # list[float]
```

**OpenAI: embed multiple documents**
`[3.EmbeddedModels/2_embedding_openai_docs.py](3.EmbeddedModels/2_embedding_openai_docs.py)`

```python
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France",
]
doc_vecs = embedding.embed_documents(documents)
print(doc_vecs)
```

**Hugging Face (local embedding)**
`[3.EmbeddedModels/3_embedding_hf_local.py](3.EmbeddedModels/3_embedding_hf_local.py)`

```python
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France",
]
vecs = embedding.embed_documents(documents)
print(vecs)
```

**Document similarity with cosine**
`[3.EmbeddedModels/4_document_similarity.py](3.EmbeddedModels/4_document_similarity.py)`

```python
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers.",
]
query = "tell me about bumrah"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]
best_idx = max(enumerate(scores), key=lambda x: x[1])[0]

print("Query:", query)
print("Best match:", documents[best_idx])
print("Similarity:", scores[best_idx])
```
