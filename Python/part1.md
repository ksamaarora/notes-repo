Here we go — I’ll turn your Part 1 notes into clean interview-oriented notes + practice questions. You can paste the next parts similarly and we’ll build a full Python sheet.

---

## 🧩 Part 1: Variables & Strings in Python

### 1. Variables and Reassignment

```python
x = 2
print(x + 3)   # 5

x = 9          # x is reassigned
print(x + 3)   # 12
```

* You don’t declare types in Python. The type is decided at runtime based on the value.
* A variable can be reassigned to another value (even to another type) at any time.

Example:

```python
x = 10        # int
x = "hello"   # now x is a string
```

---

### 2. Strings and Indexing

```python
name = "Alice"
print(name)        # Alice

print(name[0])     # 'A'   (first character, index starts at 0)
print(name[-1])    # 'e'   (last character, negative index = from the end)
```

* `name[0]` → first character
* `name[1]` → second character
* `name[-1]` → last character
* `name[-2]` → second last character

If index is out of range, Python raises:

```text
IndexError: string index out of range
```

---

### 3. String Slicing

```python
name = "Alice"

print(name[1:4])   # 'lic'   characters at index 1, 2, 3
print(name[:3])    # 'Ali'   from start (0) to index 2
print(name[2:])    # 'ice'   from index 2 to end
```

**Slice syntax:** `string[start:end]`

* `start` is inclusive
* `end` is exclusive (character at `end` index is NOT included)
* Any of `start` or `end` can be skipped:

  * `[:end]` → from beginning to `end-1`
  * `[start:]` → from `start` to end

---

### 4. Strings Are Immutable

```python
name = "Alice"
# name[0] = "a"   # ❌ This will give an error
```

You **cannot** change a single character of a string directly. This will raise:

```text
TypeError: 'str' object does not support item assignment
```

If you want a modified string, you create a **new** one:

```python
name = "Alice"
new_name = "a" + name[1:]   # 'alice'
print(new_name)
```

---

### 5. String Concatenation

```python
name = "Alice"
greeting = "Hello, " + name
print(greeting)      # Hello, Alice
```

* You can use `+` to join strings.
* All operands must be strings — concatenating string with int without conversion will throw an error.

Example (error):

```python
age = 20
msg = "Age: " + age    # ❌ TypeError
```

Correct version:

```python
age = 20
msg = "Age: " + str(age)   # ✅ "Age: 20"
```

---

### 6. Length of a String: `len()`

```python
name = "Alice"
print(len(name))   # 5
```

* `len(obj)` returns the number of characters in a string (or size of other containers like list, tuple, etc.)

---

## 🎯 Interview-Style Questions 

### 📝 Q1. Output Prediction

**Q1.1**

```python
x = 2
x = x + 3
x = x + 4
print(x)
```

**Answer:**

* Start: `x = 2`
* After `x = x + 3` → `x = 5`
* After `x = x + 4` → `x = 9`
  ✅ Output: `9`

---

**Q1.2**

```python
name = "Alice"
print(name[1:4])
print(name[-1])
print(name[:2])
```

**Answer:**

* `name[1:4]` → indices 1,2,3 → `"lic"`
* `name[-1]` → last character → `"e"`
* `name[:2]` → indices 0,1 → `"Al"`

✅ Output:

```text
lic
e
Al
```

---

**Q1.3**

```python
name = "Alice"
name = "Hi " + name
print(name)
print(len(name))
```

**Answer:**

* After concatenation, `name` becomes `"Hi Alice"`
* Characters: `H i _ A l i c e` → 9 characters

✅ Output:

```text
Hi Alice
9
```

---

### 📝 Q2. Error Finding

**Q2.1**

```python
name = "Alice"
name[0] = "a"
print(name)
```

**Question:** Will this run? If not, what error and why?

**Answer:**
No, it will not run. Python will raise:

```text
TypeError: 'str' object does not support item assignment
```

Because strings in Python are **immutable** — you cannot change a specific character in-place.

Correct way (create a new string):

```python
name = "Alice"
name = "a" + name[1:]
print(name)      # alice
```

---

**Q2.2**

```python
x = 5
result = "Value is " + x
print(result)
```

**Question:** Will this run? If not, how do you fix it in one line?

**Answer:**
This will raise:

```text
TypeError: can only concatenate str (not "int") to str
```

Because you can only concatenate strings with strings.

✅ One-line fix:

```python
result = "Value is " + str(x)
```

---

### 📝 Q3. One-Liner Questions

**Q3.1**
Given:

```python
name = "Alice"
```

Write one line to get the last character.

**Answer:**

```python
last_char = name[-1]   # 'e'
```

---

**Q3.2**
Given:

```python
name = "Alice"
```

Write one line to print `"lic"` using slicing.

**Answer:**

```python
print(name[1:4])   # lic
```

---

**Q3.3**
Given:

```python
name = "Alice"
```

Write one line to convert it to `"alice"` (first letter small) using slicing.

**Answer:**

```python
new_name = "a" + name[1:]
```

(Optional to print:)

```python
print(new_name)    # alice
```

---

**Q3.4**
Given:

```python
s = "HelloWorld"
```

Write one line to print the first 5 characters.

**Answer:**

```python
print(s[:5])    # Hello
```

---

### 📝 Q4. Conceptual

**Q4.1**
What does it mean when we say *“strings in Python are immutable”*?

**Answer:**
Once a string is created, its content cannot be changed. Any “modification” creates a **new** string instead of altering the original in-place.

---

**Q4.2**
What will `len("Hello, Alice")` return?

**Answer:**
Count the characters:
`H e l l o , _ A l i c e` → 12 characters.

✅ `len("Hello, Alice") == 12`

---

**Q4.3**
What is the difference between `name[0]` and `name[:1]`?

**Answer:**

* `name[0]` → indexing → returns the character at index 0
* `name[:1]` → slicing → returns a substring from index 0 up to (not including) 1

For `"Alice"`:

* `name[0]` → `"A"`
* `name[:1]` → `"A"`

They look the same here, but conceptually:

* Indexing → single character
* Slice → a (possibly longer) substring
