# 🧠 Prompts in LangChain

Prompts are the **input instructions or queries** given to a model to guide its output.
They tell the model *what to do*, *how to respond*, and *in what tone or style*.

---

## 🧩 Basic Prompt Example

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=1.5, max_completion_tokens=10)
result = model.invoke("Write a 5-line poem on cricket")
print(result.content)
```

**Prompt used:**

> “Write a 5-line poem on cricket”

---

## 🧠 Types of Prompts

1. **Textual Prompt** – pure text instructions (e.g., “Summarize this article”)
2. **Multimodal Prompt** – instructions that include text + image/audio/video (requires multimodal models)

---

## 💻 Streamlit Demo — Static Prompt Example

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model = ChatOpenAI()

st.header("Research Tool")
user_input = st.text_input("Enter your prompt")

if st.button("Summarize"):
    result = model.invoke(user_input)
    st.write(result.content)
```

### 🧾 What’s happening here?

* The **prompt** (entered by user) is static.
* The model executes it directly — without structure or reusability.

---

## ⚠️ Why Static Prompts Cause Problems

* Hardcoded instructions can’t adapt to new inputs easily.
* Maintaining or modifying them becomes difficult.
* Dynamic user inputs (like different topics, tones, or lengths) require re-writing the code.

---

## 🧠 Solution — Use a Prompt Template

Instead of fixed text, we can use **placeholders** and fill them dynamically at runtime.

### Example Template

```
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}

1. Mathematical Details:
   - Include relevant mathematical equations if present in the paper.
   - Explain the concepts using simple, intuitive code snippets.

2. Analogies:
   - Use relatable analogies to simplify complex ideas.

If information is missing, respond with: "Insufficient information available."
Ensure clarity, accuracy, and alignment with the given style and length.
```

---

## 🧱 What Is a PromptTemplate?

A **PromptTemplate** in LangChain:

* lets you define a **reusable structured prompt** with variables,
* supports **validation** and **runtime formatting**,
* integrates seamlessly with the LangChain ecosystem.

### ✅ Benefits Over f-Strings

* Built-in validation
* Reusable across chains or UIs
* Compatible with all LangChain tools

---

## ⚙️ prompt_ui.py (Interactive App Example)

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()
model = ChatOpenAI()

st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper",
    ["Attention Is All You Need",
     "BERT: Pre-training of Deep Bidirectional Transformers",
     "GPT-3: Language Models are Few-Shot Learners",
     "Diffusion Models Beat GANs on Image Synthesis"]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (Detailed)"]
)

template = load_prompt("template.json")

if st.button("Summarize"):
    chain = template | model
    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })
    st.write(result.content)
```

---

## 🧩 prompt_generator.py — Creating the Template

```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}

1. Mathematical Details:
   - Include relevant mathematical equations if present in the paper.
   - Explain the mathematical concepts using simple, intuitive code snippets.

2. Analogies:
   - Use relatable analogies to simplify complex ideas.

If certain information is not available, respond with "Insufficient information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True
)

template.save("template.json")
```

---

## 💬 Simple Chatbot Example

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

chat_history = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    result = model.invoke(user_input)
    print("AI:", result.content)
```

---

## 🧠 Why Chat History Matters

If you ask:

> “Who is the CEO of OpenAI?”
> then follow with
> “Where did he study?”

the second question loses context because previous history isn’t passed.

---

## 💾 Adding Chat History

```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()
chat_history = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(chat_history)
    chat_history.append(result)
    print("AI:", result.content)

print(chat_history)
```

---

## ⚠️ Problem — Unclear Roles

Here, all messages are stored, but there’s no clarity on:

* who said what
* how to differentiate system / user / AI roles

---

## 💡 Fix — Use Message Classes

LangChain provides **structured message classes**:

* `SystemMessage` → instructions or context
* `HumanMessage` → user inputs
* `AIMessage` → model outputs

```python
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about LangChain.")
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)
```

---

## 🧩 Message Placeholders

A **MessagesPlaceholder** in LangChain is used inside a `ChatPromptTemplate` to dynamically insert **chat history** or a **list of messages** at runtime.

### message_placeholder.py

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful customer support agent."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

chat_history = []
with open("chat_history.txt") as f:
    chat_history.extend(f.readlines())

prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "Where is my refund?"
})

print(prompt)
```

---

## ✅ Summary

| Concept                 | Purpose                                    |
| ----------------------- | ------------------------------------------ |
| **Prompt**              | Instruction to the model                   |
| **PromptTemplate**      | Dynamic, reusable prompt with placeholders |
| **Chat History**        | Keeps multi-turn context                   |
| **Message Classes**     | Define roles in chat                       |
| **MessagesPlaceholder** | Insert conversation history dynamically    |
