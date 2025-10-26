### **Servlet**

A **Servlet** is basically a Java program that runs on a **server** and helps in building **dynamic web pages**.
Imagine you have a **client machine (browser)** and a **server**. The client sends a request to the server expecting a page in return.

Now, if it’s a **static page** — like a plain HTML file — the request simply goes to the server and the server responds with that page directly.
But if it’s a **dynamic page**, meaning the page needs to be **generated at runtime**, then the server doesn’t just send back a file. Instead, it asks a **helper application** called a **web container** (like **Tomcat** or **Jetty**) to handle it.

This web container is responsible for managing **Servlets**.
So, when the client sends a dynamic request, the **web container** receives it and passes it to the corresponding **servlet**.
The **servlet** then:

* Takes the request,
* Processes it (maybe fetches data from a database or another source),
* Builds the dynamic page (like HTML with data filled in), and
* Sends it back to the **server**, which finally returns it to the **client** as a **response**.

---

Inside your server, there’s a special file called **Deployment Descriptor** (`web.xml`).
This file contains details about all your servlets — for example, which servlet is mapped to which URL.

Here’s how it works step-by-step:

1. A request comes to the server.
2. The server checks **web.xml** to find which servlet corresponds to that requested URL.
3. The request is forwarded to that servlet.
4. The servlet **processes** the request and **sends back** the response.

---

Every servlet follows a **lifecycle**:

1. `init()` → called once when the servlet is first loaded (used for initialization).
2. `service()` → called every time a request comes in (main logic here).
3. `destroy()` → called when the servlet is being taken out of service (for cleanup).

The response that the servlet generates (usually HTML) is sent back to the client as part of the **response object**.

---

Earlier, we used the **web.xml** file to define servlet mappings (which servlet handles which URL), but now we can do it directly using **annotations**.

For example:

```java
@WebServlet("/url")
```

This annotation tells the web container that this particular servlet should handle requests that come to `/url`.

---

**In short:**
A servlet is the **bridge between the client’s request and the dynamic response** from the server.
The **web container** (like Tomcat) takes care of loading, mapping, and running servlets behind the scenes.
