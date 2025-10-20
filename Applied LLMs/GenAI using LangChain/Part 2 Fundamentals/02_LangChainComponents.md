# **LangChain Components**

LangChain helps build applications that use large language models (LLMs) more efficiently. It has six key components — **Models, Prompts, Chains, Indexes, Memory, and Agents** — each solving a core problem when working with AI systems.

<img width="568" height="296" alt="image" src="https://github.com/user-attachments/assets/f0771250-7f03-48c4-be28-aaf24bb0f861" />

---

## **1) Models**

In LangChain, **models** are the main interfaces through which we interact with AI.

Earlier, building NLP chatbots was difficult because understanding natural language and generating context-aware responses required complex logic. LLMs changed this by being trained on massive internet-scale data, allowing them to understand and generate text naturally. However, these models are extremely large, so companies host them on servers and provide access through APIs.

If an application developer wants to use two different models (say **OpenAI** and **Anthropic**), each has a different API format.
LangChain solves this by providing a **standard interface** that allows developers to talk to any model using the same syntax.

---

### **Example: Without LangChain**

**OpenAI Example**

```python
from openai import OpenAI
client = OpenAI()

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Write a haiku about recursion in programming."}
]

completion = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
print(completion.choices[0].message)
```

**Anthropic Example**

```python
import anthropic
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-3-5-sonnet-20240229",
    max_tokens=1000,
    temperature=0,
    system="You are a world-class poet. Respond only with short poems.",
    messages=[
        {"role": "user", "content": [{"type": "text", "text": "Why is the ocean salty?"}]}
    ]
)

print(message.content)
```

Each model uses different syntax and parameters — LangChain solves this problem through a **unified interface**.

---

### **Example: With LangChain**

**OpenAI (via LangChain)**

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0)
result = model.invoke("Now divide the result by 1.5")
print(result.content)
```

**Anthropic (via LangChain)**

```python
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-3-opus-20240229")
result = model.invoke("Hi, who are you?")
print(result.content)
```

---

In LangChain, there are mainly **two types of models**:

* **Language Models (LLMs)** – take text as input and generate text as output.
* **Embedding Models** – take text as input and generate numerical vector embeddings (used for semantic search and similarity comparison).

---

## **2) Prompts**

A **prompt** is the input we provide to an LLM. The quality and clarity of the prompt directly influence the output.

For example:

* “Explain LLMs in a theoretical way.”
* “Explain LLMs in a funny way.”
  Both will produce very different responses.

LangChain offers flexibility in creating reusable and structured prompts.

---

### **Types of Prompts**

#### **a) Dynamic Prompts**

They use placeholders, so one prompt can adapt to multiple situations.
Example:

```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template("Summarize {topic} in a {tone} tone.")
print(prompt.format(topic="Cricket", tone="fun"))
```

---

#### **b) Role-based Prompts**

Define roles such as system and user messages.

```python
from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Hi, you are an experienced {profession}."),
    ("user", "Tell me about {topic}."),
])

formatted_messages = chat_prompt.format_messages(profession="Doctor", topic="Viral Fever")
```

---

#### **c) Few-shot Prompts**

These teach the model through examples, improving accuracy in classification or reasoning tasks.

```python
examples = [
    {"input": "I was charged twice for my subscription this month.", "output": "Billing Issue"},
    {"input": "The app crashes every time I try to log in.", "output": "Technical Problem"},
    {"input": "Can you explain how to upgrade my plan?", "output": "General Inquiry"},
    {"input": "I need a refund for a payment I didn’t authorize.", "output": "Billing Issue"},
]
```

```python
example_template = """
Ticket: {input}
Category: {output}
"""
```

```python
from langchain.prompts import PromptTemplate, FewShotPromptTemplate

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=PromptTemplate(
        input_variables=["input", "output"],
        template=example_template,
    ),
    prefix=(
        "Classify the following customer support tickets into one of the categories: "
        "'Billing Issue', 'Technical Problem', or 'General Inquiry'.\n\n"
    ),
    suffix="\nTicket: {user_input}\nCategory:",
    input_variables=["user_input"],
)
```

```python
print(few_shot_prompt.format(user_input="I am unable to connect to the internet using your service."))
```

```text
Classify the following customer support tickets into one of the categories: 
'Billing Issue', 'Technical Problem', or 'General Inquiry'.

Ticket: I was charged twice for my subscription this month.
Category: Billing Issue

Ticket: The app crashes every time I try to log in.
Category: Technical Problem

Ticket: Can you explain how to upgrade my plan?
Category: General Inquiry

Ticket: I need a refund for a payment I didn’t authorize.
Category: Billing Issue

Ticket: I am unable to connect to the internet using your service.
Category:
```

---

## **3) Chains**

LangChain is named after this component.

**Chains** create pipelines where the output of one step becomes the input of the next — automating multi-step logic.

Example:
If a user inputs a long English text and wants a Hindi summary (under 100 words):

1. The text is first translated to Hindi.
2. The translated text is summarized.

Without chains, you’d have to manually pass each output to the next model.
Chains automate this flow.

**Types of Chains:**

* **Sequential Chains** – Steps occur one after another.
* **Parallel Chains** – Multiple models run simultaneously, and their outputs are merged.
* **Conditional Chains** – Flow changes based on conditions (e.g., responding differently to positive/negative feedback).

---

## **4) Indexes**

**Indexes** connect an LLM to external knowledge sources like PDFs, websites, or databases.
LLMs by default don’t know private data, so LangChain builds retrieval systems using:

* **Document Loaders** – Load data from files/websites.
* **Text Splitters** – Break documents into smaller chunks.
* **Embedding Models** – Convert text into numeric vectors.
* **Vector Stores** – Store embeddings for semantic search.
* **Retrievers** – Fetch relevant data for a query.

Example:
To make ChatGPT answer company-specific questions, load company PDFs → split into chunks → embed → store in a vector DB.
When a user asks a question, the retriever finds relevant chunks and sends them to the LLM for a context-rich response.

---

## **5) Memory**

By default, LLM API calls are **stateless** — each request is independent and doesn’t remember past interactions.

<img width="668" height="176" alt="image" src="https://github.com/user-attachments/assets/08156467-1da8-4323-b10d-a7f329368b4e" />

For example:
If you first ask, “Who is Narendra Modi?” and then “How old is he?”, the model won’t know who “he” is.

LangChain adds **memory** to solve this, allowing the model to retain context across multiple turns.

### **Common Types of Memory:**

* **ConversationBufferMemory** – Stores recent messages; useful for short chats.
* **ConversationBufferWindowMemory** – Keeps only the last *N* interactions to manage token usage.
* **Summarizer-Based Memory** – Summarizes older parts to save space.
* **Custom Memory** – Stores user-specific data like preferences or key facts.

---

## **6) Agents**

An **agent** is like a chatbot with superpowers.
While a normal chatbot only generates text, an agent can **reason** and **perform actions** using tools or APIs.

Example:
If you ask a travel chatbot, “Find me the cheapest flight on 24th Jan,”
a normal chatbot just replies textually —
but an **agent** can actually **call a flight API**, fetch real-time data, and even book the ticket.

Agents combine **reasoning ability** + **tools**.

Suppose an agent has two tools — a calculator and a weather API.
If a user asks, “Multiply today’s temperature in Delhi by 3,”
the agent will:

1. Call the weather API to get the temperature.
2. Use the calculator tool to multiply it.
3. Return the result.

This reasoning process is powered by methods like **Chain-of-Thought prompting** and **ReAct (Reason + Act)** frameworks.

---

## **Summary**

LangChain provides an end-to-end framework for building powerful AI applications:

1. **Models** – Connect to LLMs or embedding models.
2. **Prompts** – Shape how we communicate with LLMs.
3. **Chains** – Link multiple models or steps.
4. **Indexes** – Connect LLMs to external/private data.
5. **Memory** – Maintain context across conversations.
6. **Agents** – Enable reasoning and real-world action.

Together, these components transform static chatbots into **intelligent, dynamic, and context-aware AI systems**.
