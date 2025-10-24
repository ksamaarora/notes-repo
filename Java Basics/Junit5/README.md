# 🧪 **JUnit**

## ⚙️ **Testing vs Unit Testing**

**JUnit** is a **framework** used for writing and running tests in **Java**.
It is primarily used for **unit testing**, which involves testing **individual components or units of code** to ensure they work as expected.

**Unit Testing** is a **software testing technique** where **individual units or components** of a software application are **tested in isolation** from the rest of the application.
The goal of unit testing is to **validate that each unit of the software performs as designed.**

**Testing** comes under the **SDLC (Software Development Life Cycle)** and is a **broader term** that encompasses various types of testing, including **unit testing, integration testing, system testing, acceptance testing**, and more.
Testing can be performed at **different levels** of the software development process to ensure the **overall quality and functionality** of the application.

**Units**, in simple terms, can be understood as the **smallest testable parts** of an application, such as **functions, methods, or classes**.
**Unit testing** focuses on **verifying the correctness** of these individual units in isolation.

---

## 🧠 **JUnit 5 Architecture**

**JUnit 5** is composed of **three main modules:**

<img width="720" height="234" alt="image" src="https://github.com/user-attachments/assets/bc36077e-cc03-4a3f-860c-62532efe40e1" />

1. **Jupiter**:
   This module provides the **new programming model** and **extension model** for writing tests and extensions in JUnit 5.
   It includes **annotations, assertions, and other features** for creating and executing tests.

2. **Vintage**:
   This module provides support for running **JUnit 3 and JUnit 4 tests** on the JUnit 5 platform.
   It allows for **backward compatibility** with older versions of JUnit.

3. **Platform**:
   This module serves as the **foundation for launching testing frameworks** on the JUnit 5 platform.
   It provides the **infrastructure for discovering and executing tests.**

---

* 👉 [**Part 1 – JUnit Basics & Setup**](./Part1.md)
* 👉 [**Part 2 – Annotations, Assertions & Examples**](./Part2.md)