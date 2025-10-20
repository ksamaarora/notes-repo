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

