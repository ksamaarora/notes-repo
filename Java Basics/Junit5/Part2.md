# 🧪 JUnit 5 — Testing in Java

## 📘 Overview

**JUnit** is a widely used **testing framework** in Java that allows developers to write and execute automated tests.
It’s primarily used for **unit testing** — verifying that individual parts (units) of code work as expected, in isolation.

JUnit 5 consists of three main modules:

* **Jupiter** – the new testing and extension model (JUnit 5 API)
* **Platform** – the engine that discovers and runs tests
* **Vintage** – backward compatibility for JUnit 3 & 4 tests

---

## 🧩 The `@Test` Annotation

The `@Test` annotation is used to denote that a method is a **test method**.
JUnit automatically executes all methods annotated with `@Test` when tests are run.

### 🔹 Syntax

```java
@Test
void testMethodName() {
    // test logic here
}
```

### 🧠 Key Points

* In JUnit 5, test methods can have **any visibility** (`public`, `protected`, or default).
* By default, a test is **considered passed** if it executes **without throwing an exception**.
* If an exception is thrown during test execution, the test **fails**.

### ✅ Example

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class SampleTest {

    @Test
    void testAddition() {
        assertEquals(2, 1 + 1);
    }
}
```

---

## ⚖️ Assertions — Expectations vs. Reality

Assertions validate the **expected outcome** of a test.
If the **expected value equals the actual value**, the test passes; otherwise, it fails.

If expected value == Actual value → Test Passes
If expected value != Actual value → Test Fails

Assertions are used to validate the expected outcomes of tests. JUnit provides a variety of assertion methods in the Assertions class, such as assertEquals, assertTrue, assertFalse, assertNull, assertNotNull, and assertThrows.

JUnit provides a variety of assertion methods in the `Assertions` class:

---

1. **`assertEquals(expected, actual)`**:
   Checks if the **expected value** is **equal** to the **actual value**.
   👉 If they are equal, the **test passes**; otherwise, it **fails**.

2. **`assertNotEquals(expected, actual)`**:
   Checks if the **expected value** is **not equal** to the **actual value**.
   👉 If they are not equal, the **test passes**; otherwise, it **fails**.

3. **`assertTrue(condition)`**:
   Checks if the given **condition is true**.
   👉 If it is true, the **test passes**; otherwise, it **fails**.

4. **`assertFalse(condition)`**:
   Checks if the given **condition is false**.
   👉 If it is false, the **test passes**; otherwise, it **fails**.

5. **`assertNull(object)`**:
   Checks if the given **object is null**.
   👉 If it is null, the **test passes**; otherwise, it **fails**.

6. **`assertNotNull(object)`**:
   Checks if the given **object is not null**.
   👉 If it is not null, the **test passes**; otherwise, it **fails**.

7. **`assertThrows(expectedType, executable)`**:
   Checks if the provided **executable** (usually a **lambda expression**)
   **throws an exception** of the **expected type**.
   👉 If the exception is thrown, the **test passes**; otherwise, it **fails**.

---

## 🧠 Example: Multiple Test Cases

A single test class can contain multiple test methods, each annotated with `@Test`.
JUnit automatically runs **all test methods** in the class.

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

## 🧱 JUnit + Maven Integration

If you’re using **Maven**, add JUnit dependencies in your `pom.xml`:

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

### Run Tests

* In IntelliJ → Right-click test class → **Run ‘TestName’**
* Or via command line:

  ```bash
  mvn test
  ```

---

## ⚙️ Testing Lifecycle Annotations (Later)

| **Annotation** | **Purpose**                          |
| -------------- | ------------------------------------ |
| `@BeforeEach`  | Runs before each test (setup logic)  |
| `@AfterEach`   | Runs after each test (cleanup logic) |
| `@BeforeAll`   | Runs once before all tests (static)  |
| `@AfterAll`    | Runs once after all tests (static)   |
| `@DisplayName` | Custom name for test display         |
| `@Disabled`    | Temporarily disables a test          |

These lifecycle methods are useful when writing **integration tests** in Spring Boot or larger applications.

---

## 💡 Why Unit Testing Matters

* Detects bugs early
* Ensures code reliability and reusability
* Enables safe refactoring
* Forms the foundation for CI/CD pipelines
* Encourages modular, maintainable design