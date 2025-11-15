## Part 6 – Data Types in Python

### 1️⃣ Built-in Core Data Types

Broad categories:

* `None`
* **Numeric** → `int`, `float`, `complex`, `bool`
* **Sequence types** → `list`, `tuple`, `str`, `range`
* **Set types** → `set`, `frozenset`
* **Mapping type** → `dict`

From your list:

* `None`
* Numeric: `int`, `float`, `complex`, `bool`
* `list`
* `tuple`
* `set`
* `str`
* `range`
* `dict`

---

### 2️⃣ `type()` Function

Use `type(obj)` to check the data type of an object.

```python
a = 10
print(type(a))   # <class 'int'>

a = 10.5
print(type(a))   # <class 'float'>

a = 1 + 2j
print(type(a))   # <class 'complex'>

a = True
print(type(a))   # <class 'bool'>

a = [1, 2, 3]
print(type(a))   # <class 'list'>

a = (1, 2, 3)
print(type(a))   # <class 'tuple'>

a = {1, 2, 3}
print(type(a))   # <class 'set'>

a = "Hello"
print(type(a))   # <class 'str'>

a = range(5)
print(type(a))   # <class 'range'>

a = {'key': 'value'}
print(type(a))   # <class 'dict'>
```

And:

```python
a = None
print(type(a))   # <class 'NoneType'>
```

> `None` is a special singleton object representing “no value” / “empty”.

---

### 3️⃣ Sequence Types

**Sequence types:** `list`, `tuple`, `str`, `range`.

* **List (`list`)**

  * Mutable, ordered collection of items.
  * Example:

    ```python
    a = [1, 2, 3]
    ```

* **Tuple (`tuple`)**

  * Immutable, ordered collection.
  * Example:

    ```python
    a = (1, 2, 3)
    ```

* **String (`str`)**

  * Immutable sequence of Unicode characters.
  * Example:

    ```python
    a = "Hello"
    ```

* **Range (`range`)**

  * Immutable sequence of numbers, commonly used in loops.
  * Example:

    ```python
    a = range(5)      # 0,1,2,3,4
    list(a)           # [0, 1, 2, 3, 4]
    ```

---

### 4️⃣ Mapping Type

* **Dictionary (`dict`)**

  * Mutable collection of key–value pairs.
  * Keys: hashable (immutable) types, usually `str`, `int`, `tuple`, etc.
  * Example:

    ```python
    a = {"key": "value", "age": 25}
    ```

---

### 5️⃣ Set Type

* **Set (`set`)**

  * Mutable, unordered collection of **unique** elements.
  * Example:

    ```python
    a = {1, 2, 3}
    ```

(And there is `frozenset` → immutable set, good to know for later.)

---

## 🎯 Interview-Style Questions (With Answers Inline)

### Q1 – Basic `type()` Checks

**Q1.1**

```python
a = 10
b = 10.5
c = 1 + 2j
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
```

**Answer:**

* `a` → `<class 'int'>`
* `b` → `<class 'float'>`
* `c` → `<class 'complex'>`
* `d` → `<class 'bool'>`

✅ Output:

```text
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'bool'>
```

---

**Q1.2**

```python
a = None
print(type(a))
```

**Answer:**

✅ Output:

```text
<class 'NoneType'>
```

---

### Q2 – Sequences vs Non-Sequences

**Q2.1**
Which of these are *sequence types*?

* `list`
* `tuple`
* `set`
* `str`
* `range`
* `dict`

**Answer:**

* Sequences: `list`, `tuple`, `str`, `range`
* Non-sequences: `set` (set type), `dict` (mapping type)

---

**Q2.2**

```python
a = range(5)
print(a)
print(list(a))
```

**Answer:**

* `a` is a `range` object: `range(0, 5)`
* Converting to list: `[0, 1, 2, 3, 4]`

✅ Output:

```text
range(0, 5)
[0, 1, 2, 3, 4]
```

---

### Q3 – Mutability Understanding

**Q3.1**
Which of the following are mutable?

* `int`
* `float`
* `str`
* `list`
* `tuple`
* `set`
* `dict`
* `range`

**Answer:**

* **Mutable**: `list`, `set`, `dict`
* **Immutable**: `int`, `float`, `str`, `tuple`, `range`, `bool`, `complex`

---

### Q4 – `bool` and `int` Relation

**Q4.1**

```python
print(isinstance(True, bool))
print(isinstance(True, int))
print(True + True)
print(True == 1)
```

**Answer:**

* `bool` is a subclass of `int` in Python.
* `True` behaves like `1`, `False` like `0`.

So:

* `isinstance(True, bool)` → `True`
* `isinstance(True, int)` → `True`
* `True + True` → `2`
* `True == 1` → `True`

✅ Output:

```text
True
True
2
True
```

---

### Q5 – `None` Usage

**Q5.1**
What is `None` typically used for in Python?

**Answer:**

Common uses:

* As a default value for function arguments.
* To represent “no value”, “not found”, or “nothing here”.
* As a placeholder or sentinel for uninitialized variables.

Example:

```python
def find_user(id):
    # return user object if found, else None
    ...
```

---

### Q6 – Simple Type Casting

**Q6.1**

```python
a = "10"
b = int(a)
c = float(a)

print(type(b), b)
print(type(c), c)
```

**Answer:**

* `int("10")` → `10` (`<class 'int'>`)
* `float("10")` → `10.0` (`<class 'float'>`)

✅ Output:

```text
<class 'int'> 10
<class 'float'> 10.0
```

---

## 🔥 MAANG / FAANG All-Time Favorite Questions on Data Types

Now the spicier ones they *actually* ask to probe your understanding.

---

### 🧠 Q1 – `bool` and `int` Gotcha

```python
print(True + False)
print(True * 10)
print(False * 10)
```

**Answer:**

* `True` behaves like `1`
* `False` behaves like `0`

So:

* `True + False` → `1 + 0` → `1`
* `True * 10` → `10`
* `False * 10` → `0`

✅ Output:

```text
1
10
0
```

---

### 🧠 Q2 – Truthy / Falsy Values

```python
values = [0, 1, "", "hello", [], [1], None, {}, {1: "a"}]

for v in values:
    if v:
        print(f"{v!r} is truthy")
    else:
        print(f"{v!r} is falsy")
```

**Answer:**

Falsy values in Python are:

* `0` (numeric 0)
* `0.0`
* `0j`
* `""` (empty string)
* `[]` (empty list)
* `()` (empty tuple)
* `{}` (empty dict)
* `set()` (empty set)
* `range(0)`
* `None`
* `False`

So:

* `0` → falsy
* `1` → truthy
* `""` → falsy
* `"hello"` → truthy
* `[]` → falsy
* `[1]` → truthy
* `None` → falsy
* `{}` → falsy
* `{1: "a"}` → truthy

---

### 🧠 Q3 – `range` vs List

```python
r = range(0, 10, 2)
print(r)
print(list(r))
print(type(r))
```

**Answer:**

* `r` is a `range` object (lazy, immutable sequence)
* `list(r)` forces evaluation into a list.

✅ Output:

```text
range(0, 10, 2)
[0, 2, 4, 6, 8]
<class 'range'>
```

Interview point:

> `range` is not a list; it’s a lightweight, immutable sequence object that generates numbers on demand.

---

### 🧠 Q4 – Complex Numbers

```python
z = 1 + 2j
print(type(z))
print(z.real, z.imag)
print(z.conjugate())
```

**Answer:**

* `type(z)` → `<class 'complex'>`
* `z.real` → `1.0`
* `z.imag` → `2.0`
* `z.conjugate()` → `1 - 2j`

✅ Output:

```text
<class 'complex'>
1.0 2.0
(1-2j)
```

---

### 🧠 Q5 – Identity vs Equality Again (With Types)

```python
a = 256
b = 256
c = 257
d = 257

print(a == b, a is b)
print(c == d, c is d)
```

**Answer:**

* `a == b` → `True`, `a is b` → often `True` (small int caching).
* `c == d` → `True`, `c is d` → often `False`.

Typical CPython output:

```text
True True
True False
```

But the *important* interview answer:

> Value equality and identity are different, and identity behaviour is an implementation detail.

---

### 🧠 Q6 – Mixed-Type Operations

```python
print(1 + 2.5)
print(1 + True)
print(3 + 4j + 2)
```

**Answer:**

* `1 + 2.5` → `3.5` (`int` + `float` → `float`)
* `1 + True` → `2` (`True` → 1)
* `3 + 4j + 2` → `(5 + 4j)` (`int` + `complex` → `complex`)

---

### 🧠 Q7 – `dict` Keys and Hashability

```python
d = {}
d[1] = "int"
d[1.0] = "float"
print(d)
print(len(d))
```

**Answer:**

* `1` and `1.0` have the **same hash** and compare equal (`1 == 1.0` → `True`).
* As dictionary keys, they collide → the later assignment overwrites the previous one.

So final dict:

```text
{1: 'float'}
1
```

✅ Output:

```text
{1: 'float'}
1
```

Interview takeaway:

> Dict keys must be hashable, and if two keys compare equal and have same hash, they are treated as the same key.

---

### 🧠 Q8 – Type of Literal and Converted Range

```python
r = range(3)
lst = list(r)

print(type(r))
print(type(lst))
print(r == lst)
```

**Answer:**

* `type(r)` → `<class 'range'>`
* `type(lst)` → `<class 'list'>`
* `r == lst` → `False` (different types; range vs list)

✅ Output:

```text
<class 'range'>
<class 'list'>
False
```
