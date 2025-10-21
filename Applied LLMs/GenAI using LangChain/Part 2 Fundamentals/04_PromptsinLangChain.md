Prompts in Langchain 

Prompts are the input instructions or queries given to a model to guide its output. from langchain_openai import ChatOpenAT

from dotenv import load_dotenv
load_dotenv®
model = ChatOpenAI(model='gpt-4*, temperature=1.5, max_completion_tokens=10)
result = model.invoke("write a 5 line poem on cricket")
print(result.content)

This is the prompt - write a 5 line poem on cricket

Types:
1. Textual Prompt
2. Multimodel prompt 

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model=ChatOpenAI()

st.header('Research Tool')

user_input = st.text_input('Enter your prompt')

if st.button('Summarize'):
    result=model.invoke(user_input)
    st.write(result.content)

Above is s static prompt - static prompts are basically ...

Why static prompts may cause a problem? 

Its better u create a prompt template 

Example prompt template 
Please sunnarize the research paper titled "(paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: (length_input)
• 1. Mathematical Details:
Inctdue relevant mathenatical equations if present in the paper.
Explain the nathematical concepts usigg siuple, intuitive code snippets
where applicable.
2. Analogies
- Use relatable analogies to simplify complex ideas.
If certain information is not available in the paper, respond with: "Insufficient information available' instead of guessing,
Ensure the summary is clear, accurate, and aligned with the provided style and length.


---

A PromptTemplate in LangChain
A PromptTemplate in LangChain is a structured way to create prompts dynamically by inserting variables into a predefined template. Instead of hardcoding prompts, PromptTemplate allows you to define placeholders that can be filled in at runtime with different inputs.
This makes it reusable, flexible, and easy to manage — especially when working with dynamic user inputs or automated workflows.
Why use PromptTemplate over f-strings?
Default validation
Reusable
LangChain Ecosystem

---

prompt_ui.py
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model = ChatOpenAI()

st.header('Reasearch Tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')

if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.content)

prompt_generator.py
from langchain_core.prompts import PromptTemplate

# template
template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_variables=['paper_input', 'style_input','length_input'],
validate_template=True
)

template.save('template.json')

---

Lets make a small chatbot now 

