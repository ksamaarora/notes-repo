# MCP Protocol Stack

**MCP’s technical architecture** consists of **three distinct layers**, each handling a specific aspect of **communication between AI systems and data sources**.

---

## **1. Transport Layer**

The **Transport Layer** handles the **actual transmission of messages** between the MCP client and server.

<img width="1456" height="806" alt="image" src="https://github.com/user-attachments/assets/80605e67-3774-4368-bf68-6c00459adefc" />

For **local connections**, MCP uses **STDIO (standard input/output)**, where messages flow as simple **text streams** between processes on the same computer. This approach works perfectly when an MCP server runs on the same machine as the AI application, allowing for **fast, lightweight communication** without requiring network overhead.

For **remote connections**, MCP employs **HTTP** for sending **requests** and **Server-Sent Events (SSE)** for receiving **responses**, enabling **secure and continuous communication** across networks and the internet. SSE allows the server to push updates or results back to the client in real time without requiring the client to repeatedly poll the server.

📊 *See the diagram below for a visual representation of the transport layer flow.*

---

## **2. Protocol Layer**

The **Protocol Layer** defines *how messages are structured and understood*.
MCP uses **JSON-RPC 2.0**, a lightweight standard for **remote procedure calls (RPC)**.

**JSON-RPC** was chosen because it’s simple, well-established, and familiar to most developers. Every message is formatted as plain **JSON text** with a clear structure:

* A **method name** (the function being called)
* **Parameters** (data inputs for that method)
* An **ID** (to track which response corresponds to which request)

This simplicity makes debugging easy, since messages are human-readable and transparent. Developers can directly inspect or log the JSON messages flowing between client and server to understand the full interaction.

---

## **3. Capability Layer**

The **Capability Layer** defines **what MCP can actually do** — the level where **real functionality** is exposed to the AI model.
It introduces **three core primitives**:

* **Tools** → Functions that the AI can execute to perform actions, such as sending emails, searching documents, or creating database entries.
* **Resources** → Provide **read-only access** to external data without altering it — for example, retrieving user records, fetching files, or reading from a knowledge base.
* **Prompts** → Act as **reusable templates or workflows** that help the AI combine multiple actions efficiently, similar to how macros or saved pipelines work in traditional software.

Together, these primitives form the **operational vocabulary** of MCP — describing what capabilities are available and how the AI can safely interact with them.
