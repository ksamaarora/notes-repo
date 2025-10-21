# 🧩 Structured Output in LangChain

In **LangChain**, *structured output* refers to generating model responses in a **defined data format** (like JSON) instead of free-form text.
This allows for easier parsing, validation, and integration with other systems.

---

## 💬 Example Prompt

**Prompt:**

> Can you create a one-day travel itinerary for Paris?

### 🧾 LLM’s *Unstructured Response:*

```
Here's a suggested itinerary: 
Morning: Visit the Eiffel Tower.  
Afternoon: Walk through the Louvre Museum.  
Evening: Enjoy dinner at a Seine riverside café.
```

### ✅ JSON-Enforced Output:

```json
[
  {"time": "Morning", "activity": "Visit the Eiffel Tower"},
  {"time": "Afternoon", "activity": "Walk through the Louvre Museum"},
  {"time": "Evening", "activity": "Enjoy dinner at a Seine riverside café"}
]
```

---

## 🧠 Why Do We Need Structured Output?

### 1️⃣ Data Extraction

Imagine a **job portal** where users upload resumes.
You could extract structured data such as:

```json
{
  "name": "John Doe",
  "role": "Software Engineer",
  "experience": "5 years"
}
```

— ready for direct database storage or analytics.

---

### 2️⃣ APIs

For example, at **Amazon**, an LLM could process customer reviews and return structured product feedback data to be used in dashboards or automation workflows.

---

### 3️⃣ Agents

AI agents often need to communicate using structured formats — e.g., JSON or Pydantic objects — to ensure reliable data exchange between components.

---

## ⚙️ Ways to Get Structured Output

There are two major ways:

### **1️⃣ Using LLMs that natively support structured output**

LangChain provides:

```python
model.with_structured_output(schema)
```

You define the schema, and the model enforces that format automatically.

---

### **2️⃣ Using Output Parsers**

For LLMs that do *not* natively support structured output,
LangChain provides **OutputParser** utilities that parse text into structured formats after generation.

---

## 🧰 Method 1 — `with_structured_output`

Here, you tell the model *before* invocation what format you expect.

You can define schemas using:

* 🟢 **TypedDict**
* 🟣 **Pydantic**
* 🟡 **JSON Schema**

---

## 🧩 (a) TypedDict

`TypedDict` lets you define what keys and value types a dictionary should have.
It ensures consistency in structure (though it doesn’t validate data at runtime).

### ✅ Why Use TypedDict?

* It clearly defines expected keys and types.
* Helps with **type hints** for cleaner, safer code.
* Enhances **readability** and **IDE autocompletion**.

**Variations:**

* Simple `TypedDict`
* Annotated `TypedDict`
* Literal
* Complex (with pros & cons)

---

### 🧠 Example 1 — Simple TypedDict

```python
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {'name': 'Nitish', 'age': 35}
print(new_person)
```

---

## 📊 Problem Statement

We have a set of **phone reviews**.
We want to extract structured insights — specifically **summary** and **sentiment** — using LangChain.

---

### 🧠 Example 2 — Review Summarizer

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()
model = ChatOpenAI()

# schema
class Review(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
The hardware is great, but the software feels bloated.
There are too many pre-installed apps that I can't remove.
Also, the UI looks outdated compared to other brands.
Hoping for a software update to fix this.
""")

print(result)
print(result['summary'])
print(result['sentiment'])
```

---

### 🧩 How It Works

1. **TypedDict** defines the expected structure:

   ```python
   {'summary': str, 'sentiment': str}
   ```

2. **`with_structured_output()`** enforces this schema at runtime.

3. The model automatically converts the LLM response into this structured format.

---

### 💡 What Happens Behind the Scenes

LangChain internally generates a guiding system prompt like:

> You are an AI assistant that extracts structured insights from text.
> Given a product review, extract:
>
> * **Summary:** A brief overview of the main points.
> * **Sentiment:** Overall tone of the review (positive, neutral, negative).
>   Return the response in **JSON format**.

---

## 🧩 Example 3 — Annotated TypedDict

You can add *rich descriptions* and *Literal types* for more precise control.

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()
model = ChatOpenAI()

# schema
class Review(TypedDict):
    key_themes: Annotated[list[str], "List all key themes discussed in the review"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Sentiment (positive or negative)"]
    pros: Annotated[Optional[list[str]], "List of pros"]
    cons: Annotated[Optional[list[str]], "List of cons"]
    name: Annotated[Optional[str], "Reviewer name"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse!
The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos.
The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often.
What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light.
Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use.
Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides?
The $1,300 price tag is also a hard pill to swallow.

Pros:
- Insanely powerful processor (great for gaming and productivity)
- Stunning 200MP camera with incredible zoom
- Long battery life with fast charging
- S-Pen support is unique and useful

Review by Nitish Singh
""")

print(result['name'])
```

---

## 🧭 Summary

| Concept                      | Purpose                                               |
| ---------------------------- | ----------------------------------------------------- |
| **Structured Output**        | Enforces predictable JSON-like responses              |
| **TypedDict**                | Defines key-value structure                           |
| **with_structured_output()** | Enables schema enforcement at runtime                 |
| **Annotated + Literal**      | Adds clarity and control over expected data           |
| **Use Case**                 | Ideal for agents, APIs, and data extraction pipelines |
