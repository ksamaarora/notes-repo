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

--- 

What is Tomcat?
**Apache Tomcat** is an open-source web server and servlet container developed by the Apache Software Foundation. It is designed to execute Java Servlets and render web pages that use Java Server Pages (JSP). Tomcat provides a "pure Java" HTTP web server environment for Java code to run in, making it a popular choice for hosting Java-based web applications. It implements several Java EE specifications, including Java Servlet, JSP, and WebSocket, allowing developers to build and deploy dynamic web applications efficiently.

---

Say we have a code to add 2 numbers in index.html 

```html
<!DOCTYPE html>
<html>
<head>
    <title>Add Two Numbers</title>
</head>
<body>
    <h1>Add Two Numbers</h1>
    <form action="AddServlet" method="post">
        <label for="num1">Number 1:</label>
        <input type="text" id="num1" name="num1" required><br><br>
        <label for="num2">Number 2:</label>
        <input type="text" id="num2" name="num2" required><br><br>
        <input type="submit" value="Add">
    </form>
</body>
</html>
```

We will use a servlet to process this form data and return the sum of the two numbers.
```javaimport java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
@WebServlet("/AddServlet")
public class AddServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Get the numbers from the request
        int num1 = Integer.parseInt(request.getParameter("num1"));
        int num2 = Integer.parseInt(request.getParameter("num2"));
        int sum = num1 + num2;

        // Set the response content type
        response.setContentType("text/html");

        // Get the writer
        PrintWriter out = response.getWriter();

        // Generate the HTML response
        out.println("<html><body>");
        out.println("<h1>Result</h1>");
        out.println("<p>The sum of " + num1 + " and " + num2 + " is " + sum + ".</p>");
        out.println("</body></html>");
    }
}
```

You will also need to configure your `web.xml` if you are not using annotations:
```xml
<servlet>
    <servlet-name>AddServlet</servlet-name>
    <servlet-class>com.example.AddServlet</servlet-class>
</servlet>
<servlet-mapping>
    <servlet-name>AddServlet</servlet-name>
    <url-pattern>/AddServlet</url-pattern>
</servlet-mapping>
```
