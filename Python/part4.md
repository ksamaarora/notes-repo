## Part 4: Dictionaries in Python

### 1️⃣ What is a Dictionary?

* A **dictionary** is a collection of **key–value pairs**.
* It is:

  * **Mutable** → you can add, change, remove keys and values.
  * **(Logically) Unordered mapping** → conceptually a mapping, not a sequence.
    (In modern Python, insertion order is preserved, but you still treat it as a mapping.)
* Keys:

  * Must be **unique**
  * Must be **immutable** types (e.g., strings, numbers, tuples)
* Values:

  * Can be of **any type** and can be duplicated.

---

### 2️⃣ Creating and Accessing a Dictionary

```python
# Creating a dictionary
my_dict = {"key1": "value1", "key2": "value2"}
print(my_dict)

# Output:
# {'key1': 'value1', 'key2': 'value2'}
```

#### Accessing values

```python
print(my_dict["key1"])       # Access by key
# Output: value1

print(my_dict.get("key2"))   # Using get()
# Output: value2
```

* `my_dict["key1"]`:

  * Raises `KeyError` if key doesn’t exist.
* `my_dict.get("key2")`:

  * Returns `None` if key doesn’t exist (by default).

```python
print(my_dict.get("key3", "NOT FOUND"))
# Output: NOT FOUND
```

* `dict.get(key, default)` → returns `default` if key is missing.

---

### 3️⃣ Adding, Updating, Deleting

#### Add a new key–value pair

```python
my_dict["key3"] = "value3"
print(my_dict)
# {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
```

#### Modify an existing value

```python
my_dict["key1"] = "new_value1"
print(my_dict)
# {'key1': 'new_value1', 'key2': 'value2', 'key3': 'value3'}
```

* If the key **already exists**, assignment **updates** its value.
* If it doesn’t exist, assignment **creates** a new key–value pair.

#### Delete a key–value pair

```python
del my_dict["key2"]
print(my_dict)
# {'key1': 'new_value1', 'key3': 'value3'}
```

* `del my_dict["missing_key"]` → raises `KeyError`.

*(There is also `my_dict.pop("key")`, which returns the removed value — nice to know.)*

---

### 4️⃣ Common Dictionary Methods

```python
my_dict = {"a": 1, "b": 2, "c": 3}

print(my_dict.keys())      # all keys
# dict_keys(['a', 'b', 'c'])

print(my_dict.values())    # all values
# dict_values([1, 2, 3])

print(my_dict.items())     # key–value pairs
# dict_items([('a', 1), ('b', 2), ('c', 3)])
```

These return **view objects** (`dict_keys`, `dict_values`, `dict_items`) which can be iterated over:

```python
for k, v in my_dict.items():
    print(k, v)
```

---

### 5️⃣ Building Dictionaries from Lists (zip + dict)

You can build a dict from two lists: one of keys, one of values.

```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]

data = dict(zip(keys, values))
print(data)
# {'a': 1, 'b': 2, 'c': 3}

del data['b']
print(data)
# {'a': 1, 'c': 3}
```

* `zip(keys, values)` pairs them as:

  * `[('a', 1), ('b', 2), ('c', 3)]`
* `dict(...)` converts that into a dictionary.

---

### 6️⃣ Dictionary Comprehension (Real One)

Dictionary comprehension is a **compact** way to create dictionaries:

```python
squares = {x: x*x for x in range(1, 4)}
print(squares)
# {1: 1, 2: 4, 3: 9}
```

Or using `zip`:

```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]

data = {k: v for k, v in zip(keys, values)}
```

---

## 🎯 Interview-Style Questions (With Answers Inline)

### 📝 Q1. Basic Output

**Q1.1**

```python
my_dict = {"key1": "value1", "key2": "value2"}
print(my_dict["key1"])
print(my_dict.get("key2"))
```

**Answer:**

* `my_dict["key1"]` → `"value1"`
* `my_dict.get("key2")` → `"value2"`

✅ Output:

```text
value1
value2
```

---

**Q1.2**

```python
my_dict = {"a": 1, "b": 2}
my_dict["c"] = 3
my_dict["a"] = 10
print(my_dict)
```

**Answer:**

* Add `"c": 3` → `{"a": 1, "b": 2, "c": 3}`
* Update `"a"` to `10` → `{"a": 10, "b": 2, "c": 3}`

✅ Output:

```text
{'a': 10, 'b': 2, 'c': 3}
```

---

### 📝 Q2. `get()` vs `[]` Behaviour

**Q2.1**

```python
my_dict = {"a": 1, "b": 2}

print(my_dict.get("c"))
print(my_dict.get("c", 0))
print(my_dict["c"])
```

**Answer:**

* `my_dict.get("c")` → key `"c"` not present → returns `None`
* `my_dict.get("c", 0)` → key `"c"` not present → returns default `0`
* `my_dict["c"]` → raises `KeyError: 'c'`

So:

```text
None
0
# then KeyError: 'c'
```

---

### 📝 Q3. Deletion & Errors

**Q3.1**

```python
my_dict = {"a": 1, "b": 2, "c": 3}
del my_dict["b"]
print(my_dict)
```

**Answer:**

Key `"b"` is removed.

✅ Output:

```text
{'a': 1, 'c': 3}
```

---

**Q3.2**

```python
my_dict = {"a": 1, "b": 2}
del my_dict["c"]
print(my_dict)
```

**Answer:**

Key `"c"` doesn’t exist → raises:

```text
KeyError: 'c'
```

---

### 📝 Q4. Methods: keys(), values(), items()

**Q4.1**

```python
my_dict = {"a": 1, "b": 2, "c": 3}
print(list(my_dict.keys()))
print(list(my_dict.values()))
print(list(my_dict.items()))
```

**Answer:**

* `keys()` → `['a', 'b', 'c']`
* `values()` → `[1, 2, 3]`
* `items()` → `[('a', 1), ('b', 2), ('c', 3)]`

✅ Output:

```text
['a', 'b', 'c']
[1, 2, 3]
[('a', 1), ('b', 2), ('c', 3)]
```

*(Order will follow insertion order.)*

---

**Q4.2**
What does this print?

```python
my_dict = {"a": 1, "b": 2}
for key, value in my_dict.items():
    print(key, value)
```

**Answer:**

Iterates over key–value pairs.

✅ Output:

```text
a 1
b 2
```

(Exact order: `"a"` then `"b"`.)

---

### 📝 Q5. Building Dicts from Lists

**Q5.1**

```python
keys = ['x', 'y', 'z']
values = [10, 20, 30]

data = dict(zip(keys, values))
print(data)
```

**Answer:**

`zip(keys, values)` → `[('x', 10), ('y', 20), ('z', 30)]`
`dict(...)` → `{'x': 10, 'y': 20, 'z': 30}`

✅ Output:

```text
{'x': 10, 'y': 20, 'z': 30}
```

---

**Q5.2 – Dict Comprehension**

What will this print?

```python
squares = {n: n*n for n in range(1, 4)}
print(squares)
```

**Answer:**

* For `n = 1, 2, 3`:

  * `{1: 1, 2: 4, 3: 9}`

✅ Output:

```text
{1: 1, 2: 4, 3: 9}
```

---

### 📝 Q6. Conceptual Questions

**Q6.1**
What types can be used as dictionary keys? Why?

**Answer:**

Keys must be **hashable and immutable**. Common key types:

* `str`
* `int`, `float`
* `tuple` (if its contents are also immutable)

You **cannot** use `list` or `dict` as keys because they are mutable and not hashable.

---

**Q6.2**
Are dictionaries mutable? What does that mean?

**Answer:**

Yes, dictionaries are **mutable**:

* You can add, update, or delete key–value pairs **without** creating a new dictionary.

Example:

```python
d = {"a": 1}
d["b"] = 2      # modifies d
d["a"] = 10     # modifies d
del d["b"]      # modifies d
```

---

**Q6.3**
How is a dictionary different from a list?

**Answer (good interview line):**

* **List** → ordered collection of values, accessed by **index** (`list[0]`)
* **Dictionary** → collection of key–value pairs, accessed by **key** (`dict['key']`)

Use a dictionary when:

* You want **fast lookups** by a meaningful key (like IDs, names, etc.)
* Order is less important than the **mapping** relationship.
