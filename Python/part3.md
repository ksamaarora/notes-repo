## Tuples and Sets in Python

### 1️⃣ Lists vs Tuples – Core Difference

* **List** → ordered, **mutable**
* **Tuple** → ordered, **immutable**

> Mutable = can change elements (add, remove, update)
> Immutable = cannot change elements once created

---

## Lists (Quick Recap)

```python
# Creating a list
my_list = ["apple", "banana", "cherry"]
print(my_list)  
# Output: ['apple', 'banana', 'cherry']
```

* Uses **square brackets**: `[]`
* You **can** modify elements:

  ```python
  my_list[1] = "orange"
  # ['apple', 'orange', 'cherry']
  ```

---

## Tuples

### Definition

* Tuple is an **ordered**, **immutable** collection.
* Uses **round brackets**: `()`

```python
# Creating a tuple
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)  
# Output: ('apple', 'banana', 'cherry')
```

### Immutability

```python
my_tuple = ("apple", "banana", "cherry")
my_tuple[1] = "orange"   # ❌ TypeError
```

This raises:

```text
TypeError: 'tuple' object does not support item assignment
```

* You **cannot**:

  * Change elements
  * Add new elements
  * Remove elements

If you want a “modified” tuple, you create a **new** one:

```python
my_tuple = ("apple", "banana", "cherry")
new_tuple = (my_tuple[0], "orange", my_tuple[2])
print(new_tuple)  
# ('apple', 'orange', 'cherry')
```

### Small but important points (for interviews)

* Single-element tuple syntax:

  ```python
  t1 = (5)
  t2 = (5,)
  ```

  * `t1` is just an `int`
  * `t2` is a **tuple** with one element

* Tuple iteration is slightly **faster** than list iteration (because tuples are immutable → simpler internal structure).

---

## Sets

### Definition

* A **set** is:

  * **Unordered**
  * **Unindexed**
  * **Mutable** (you can add/remove elements)
  * Does **not** allow duplicates

* Uses **curly braces**: `{}`

```python
my_set = {"apple", "banana", "cherry"}
print(my_set)
# Output: {'banana', 'cherry', 'apple'} (order may vary)
```

* Order is **not guaranteed**.

### Duplicates Removed

```python
my_set_with_duplicates = {"apple", "banana", "cherry", "apple", "banana"}
print(my_set_with_duplicates)
# Output: {'banana', 'cherry', 'apple'}
```

* Duplicate `"apple"` and `"banana"` appear only once.
* Internally uses a **hash table**, which:

  * Makes membership tests (`x in set`) fast
  * Removes duplicates automatically
  * Loses ordering

### Indexing Not Allowed

```python
my_set = {"apple", "banana", "cherry"}
# my_set[0]  # ❌ TypeError: 'set' object is not subscriptable
```

* You **cannot** use indexing or slicing on sets because they are **unordered**.

### Mutability of Sets

> Can you change values in a set?

* You **cannot modify** an element itself (e.g., “change `'apple'` to `'orange'` directly”).
* But you **can** add or remove elements (set itself is mutable):

```python
my_set = {"apple", "banana", "cherry"}

my_set.add("orange")     # add element
my_set.remove("banana")  # remove element

print(my_set)
# e.g. {'apple', 'cherry', 'orange'}
```

---

## 🎯 Interview-Style Questions (With Answers)

### 📝 Q1. Basic Concept Check

**Q1.1**
Are lists and tuples mutable or immutable?

**Answer:**

* **List** → mutable (can modify contents)
* **Tuple** → immutable (cannot modify contents once created)

---

**Q1.2**
What will this print?

```python
my_list = ["apple", "banana", "cherry"]
my_list[1] = "orange"
print(my_list)
```

**Answer:**

We changed index `1` from `"banana"` to `"orange"`.

✅ Output:

```text
['apple', 'orange', 'cherry']
```

---

### 📝 Q2. Tuples – Output & Error

**Q2.1**

```python
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[1])
```

**Answer:**

Index `1` → `"banana"`.

✅ Output:

```text
banana
```

---

**Q2.2**

```python
my_tuple = ("apple", "banana", "cherry")
my_tuple[1] = "orange"
print(my_tuple)
```

**Answer:**

This will **not** work. Tuples are **immutable**.

Error:

```text
TypeError: 'tuple' object does not support item assignment
```

---

**Q2.3**
What is the type of each variable?

```python
a = (5)
b = (5,)
print(type(a))
print(type(b))
```

**Answer:**

* `a = (5)` → just `5` inside parentheses → **int**
* `b = (5,)` → comma makes it a tuple → **tuple**

✅ Output:

```text
<class 'int'>
<class 'tuple'>
```

---

### 📝 Q3. Sets – Output & Behaviour

**Q3.1**

```python
my_set = {"apple", "banana", "cherry", "apple", "banana"}
print(my_set)
```

**Answer:**

Duplicates are removed. Order is not guaranteed.

✅ Example Output:

```text
{'banana', 'cherry', 'apple'}
```

(Any order is fine: `{'apple', 'banana', 'cherry'}`, etc.)

---

**Q3.2**

```python
my_set = {"apple", "banana", "cherry"}
print("apple" in my_set)
print("orange" in my_set)
```

**Answer:**

* `"apple" in my_set` → `True`
* `"orange" in my_set` → `False`

✅ Output:

```text
True
False
```

---

**Q3.3**

```python
my_set = {"apple", "banana", "cherry"}
my_set.add("orange")
my_set.add("banana")
print(my_set)
```

**Answer:**

* `"orange"` added.
* `"banana"` already exists, adding again has no effect.

✅ Result (order may vary):

```text
{'apple', 'banana', 'cherry', 'orange'}
```

---

**Q3.4**

```python
my_set = {"apple", "banana", "cherry"}
# Trying to index
item = my_set[0]
print(item)
```

**Answer:**

This will raise:

```text
TypeError: 'set' object is not subscriptable
```

Because sets are **unordered** → no indexing.

---

### 📝 Q4. Conceptual – Short Answers

**Q4.1**
Why doesn’t a set allow duplicate values?

**Answer:**

Because a set is implemented using a **hash table** and it stores each value **based on its hash**. If the same value is inserted again, it maps to the same hash → it doesn’t create a new entry.

---

**Q4.2**
Are sets mutable or immutable? Can you “change” values?

**Answer:**

* Sets are **mutable** → you can add/remove elements.
* But elements themselves must be **immutable and hashable** (e.g., no lists inside a set).
* You cannot "change" an element directly, but you can:

  * Remove one value
  * Add another

---

**Q4.3**
When would you use:

* a **list**
* a **tuple**
* a **set**

**Answer (good interview-style line):**

* Use a **list** when:

  * You need an ordered collection
  * You might need to change elements frequently

* Use a **tuple** when:

  * Data should not change (fixed config, coordinates, etc.)
  * You want it to be hashable (e.g., as a dict key)

* Use a **set** when:

  * You need unique elements
  * You care about fast membership checks (`x in set`)
  * Order doesn’t matter
