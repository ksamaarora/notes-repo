## ⚙️ **JUnit Setup & First Test**

### 🧩 **1. What is Maven?**

**Maven** is a **build automation and dependency management tool** for Java projects.
It helps you easily manage external libraries (like JUnit), compile code, run tests, and package your application — all from one configuration file: `pom.xml`.

#### 📦 Maven Handles:

* **Dependencies:** Automatically downloads required libraries (e.g., JUnit, Spring, etc.)
* **Build Lifecycle:** Compiles, tests, and packages your project.
* **Project Structure:** Follows a standard directory format recognized by all IDEs.

#### 🗂️ **Standard Maven Folder Structure**

```
project-name/
 ├── src/
 │   ├── main/
 │   │   └── java/          → main source code
 │   └── test/
 │       └── java/          → test code
 ├── pom.xml                → project & dependency configuration
```

---

### ⚙️ **2. With Maven (Recommended Way)**

When using Maven, you just add JUnit dependency in `pom.xml`:

```xml
<dependencies>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-api</artifactId>
        <version>5.10.0</version>
        <scope>test</scope>
    </dependency>

    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-engine</artifactId>
        <version>5.10.0</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```

Then reload Maven in IntelliJ → **JUnit is ready to use!**

---

### 💻 **3. Without Maven**

If you’re not using Maven (or Gradle):

1. Manually download JUnit 5 `.jar` files from [https://junit.org/junit5/](https://junit.org/junit5/)
2. Add them to your **IntelliJ project’s classpath**:
   `File → Project Structure → Modules → Dependencies → + → JARs or directories`

You’ll need at least:

* `junit-jupiter-api-x.x.x.jar`
* `junit-jupiter-engine-x.x.x.jar`

But Maven handles this automatically — which is why it’s preferred.

---

### 🧠 **4. JUnit 5 Annotations Overview**

| **Annotation** | **Purpose**                                 |
| -------------- | ------------------------------------------- |
| `@Test`        | Marks a method as a test case.              |
| `@BeforeEach`  | Runs before each test (setup logic).        |
| `@AfterEach`   | Runs after each test (cleanup logic).       |
| `@BeforeAll`   | Runs once before all tests (static method). |
| `@AfterAll`    | Runs once after all tests (static method).  |
| `@DisplayName` | Custom name for test display.               |
| `@Disabled`    | Temporarily disables a test.                |

---

### 🧪 **5. Sample Project — Reverse a String**

#### ✅ Source File – `ReverseString.java`

```java
public class ReverseString {

    public String reverse(String input) {
        if (input == null) {
            throw new IllegalArgumentException("Input cannot be null");
        }
        return new StringBuilder(input).reverse().toString();
    }
}
```

#### 🧠 Explanation:

* If input is `null`, we throw an exception.
* Otherwise, we use `StringBuilder`’s built-in `reverse()` method.

---

#### ✅ Test File – `ReverseStringTest.java`

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ReverseStringTest {

    @Test
    void testNormalString() {
        ReverseString reverser = new ReverseString();
        String result = reverser.reverse("hello");
        assertEquals("olleh", result);
    }

    @Test
    void testEmptyString() {
        ReverseString reverser = new ReverseString();
        String result = reverser.reverse("");
        assertEquals("", result);
    }

    @Test
    void testNullInput() {
        ReverseString reverser = new ReverseString();
        assertThrows(IllegalArgumentException.class, () -> {
            reverser.reverse(null);
        });
    }
}
```

---

### 🧾 **6. How to Run**

* **In IntelliJ:** Right-click inside the test file → `Run 'ReverseStringTest'`
* **In Terminal (Maven command):**

  ```bash
  mvn test
  ```

  This automatically compiles code and runs all test cases under `src/test/java`.

---

### ✅ **7. Key Takeaways**

* JUnit 5 = modern, modular, annotation-based testing.
* Maven = dependency manager that makes JUnit setup effortless.
* Each test is independent and verifies one piece of logic.
* Assertions (`assertEquals`, `assertThrows`, etc.) are your validation checks.
* The green bar means **all tests passed!**
