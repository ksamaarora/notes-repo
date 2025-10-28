# The Journey of a Request

Understanding how **MCP** works becomes clearer when we trace a **single request** from start to finish.

See the diagram below:

<img width="1456" height="1248" alt="image" src="https://github.com/user-attachments/assets/ce8644c6-009e-4c6a-b6b2-70d53db229b6" />

Let’s follow what happens when someone asks their AI assistant:
**“What’s our top-selling product?”**


* The journey begins when the **user types this question** into their **AI application**.

* The **AI model analyzes the question** and recognizes that it needs **current sales data** from the **company database** to provide an accurate answer. The AI cannot access this information from its **training data**, so it must retrieve it through **MCP**.

* The **host application activates its MCP client** for the **database server**. The client takes the AI’s request and **formats it as a JSON-RPC message**. This message contains a **method name** indicating it wants to execute a **database query tool**, the **query as a parameter**, and a **unique identifier** like `"request-789"` to track this specific request.
  Note that the query is **not a complete SQL query**. It is abstract, such as *“get top-selling product for last month.”*
  The formatted message looks like **structured text** that clearly specifies what action needs to be taken.

* The **transport layer** now takes over to **deliver this message**.
  If the **database MCP server** runs on the same computer, the message travels through **STDIO**, essentially passing from one program to another through the operating system.
  If the server runs on a **remote machine**, the message travels as an **HTTP request** across the network, with proper **authentication headers** to ensure security.

* The **MCP server receives this message** and begins its crucial **translation work**. It extracts the query from the MCP request, prepares an actual **SQL query** for the **PostgreSQL database**, and connects to the real database using **standard database protocols**.
  The server executes the query, which might look for products **sorted by sales volume**.
  This interaction with the database happens **entirely outside of MCP**, using **PostgreSQL’s native communication methods**.

* The **database processes the query** and returns results.
  For example, the query may return that **“Product A” led sales with $487,000 in revenue** last month.

* The **MCP server receives these raw database results** and **formats them into an MCP response message**.
  This response includes the same **request identifier** `"request-789"` and the data structured in a way that **MCP clients understand**.

* The **response travels back** through the **transport layer** to the waiting **MCP client**.
  The client matches the **response ID** to its **outstanding request**, extracts the **sales data**, and passes this information to the **host application**, which provides it to the **AI model** along with the original question.

* Finally, the **AI model crafts a natural language response**:
  *“Our top-selling product last month was Product A, which generated $487,000 in revenue, representing 30% of total sales.”*


This entire journey demonstrates **MCP’s modular design**.

Each component handles one specific task:

* The **AI** understands language.
* The **client** speaks the **MCP protocol**.
* The **server** translates into **database queries**.
* The **database** manages data.

No component needs to understand the others’ internal workings — that’s the power of **MCP’s clean, layered architecture**.
