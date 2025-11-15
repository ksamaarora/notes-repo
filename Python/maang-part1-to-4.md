# MAANG-Style Python Questions – On Current Topics

---

## A. Variables & Strings

### Q1 – `==` vs `is` (Very Common Trap)

```python
a = "hello"
b = "hello"
c = a

print(a == b)
print(a is b)
print(a is c)
```

**Answer:**

* `a == b` → compares **values** → `"hello" == "hello"` → `True`
* `a is b` → compares **object identity** (same memory object)
  For small strings, Python may intern them, so this is often `True` in CPython, but you **must never rely on it in production logic**.
* `a is c` → `c` is assigned directly from `a`, so they are the **same object** → `True`

Typical CPython output:

```text
True
True
True
```

👉 Interview line:
Use `==` for value comparison, `is` for identity checks (`None`, singletons).

---

### Q2 – String Slicing & Negative Index

```python
s = "MAANG"
print(s[1:-1])
print(s[-3:-1])
print(s[::-1])
```

**Answer:**

* `s[1:-1]` → from index 1 to second last → `"AAN"`
* `s[-3:-1]` → third from end up to (but not including) last → `"AN"`
* `s[::-1]` → full string reversed → `"GNAAM"`

✅ Output:

```text
AAN
AN
GNAAM
```

---

### Q3 – Immutability & Concatenation

```python
s = "a"
for i in range(3):
    s = s + "b"
print(s)
```

**Answer:**

Loop:

* Start: `"a"`
* Iter1: `"ab"`
* Iter2: `"abb"`
* Iter3: `"abbb"`

✅ Output:

```text
abbb
```

Interview note: this is **O(n²)** if done in big loops; better use list + `''.join(...)`.

---

## B. Lists – MAANG-Level Patterns

### Q4 – Aliasing (Same Object Reference)

```python
nums = [1, 2, 3]
alias = nums
alias.append(4)

print(nums)
print(alias)
```

**Answer:**

`alias` and `nums` point to the **same list object**.

* After `alias.append(4)`, both see `[1, 2, 3, 4]`.

✅ Output:

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

---

### Q5 – Shallow Copy vs Alias

```python
a = [1, 2, 3]
b = a[:]         # shallow copy using slicing
b.append(4)

print(a)
print(b)
```

**Answer:**

* `b` is a **new list**.
* Modifying `b` does not affect `a`.

✅ Output:

```text
[1, 2, 3]
[1, 2, 3, 4]
```

---

### Q6 – Nested Lists + Multiplication

```python
row = [0] * 3
grid = [row] * 3

grid[0][0] = 1

print(grid)
```

**Answer:**

`[row] * 3` creates **three references to the same list**, not three independent lists.

* Changing `grid[0][0]` also changes `grid[1][0]` and `grid[2][0]`.

All rows share the same underlying list.

✅ Output:

```text
[[1, 0, 0],
 [1, 0, 0],
 [1, 0, 0]]
```

👉 Correct way to create independent rows:

```python
grid = [[0] * 3 for _ in range(3)]
```

---

### Q7 – List Slice Assignment

```python
nums = [10, 20, 30, 40, 50]
nums[1:4] = [99, 100]
print(nums)
```

**Answer:**

* Slice `[1:4]` → elements at indices 1,2,3 → `[20, 30, 40]`
* Replace those with `[99, 100]` → list shrinks.

Final list: `[10, 99, 100, 50]`

✅ Output:

```text
[10, 99, 100, 50]
```

---

### Q8 – Default Mutable Argument (Classic MAANG Trap)

```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))
print(add_item(2))
print(add_item(3, []))
print(add_item(4))
```

**Answer:**

* Default `lst=[]` is evaluated **once at function definition time**, and reused.
* Calls:

  1. `add_item(1)` → default list becomes `[1]`
  2. `add_item(2)` → reuses same list → `[1, 2]`
  3. `add_item(3, [])` → uses **new empty list passed in** → `[3]`
  4. `add_item(4)` → uses default list again → `[1, 2, 4]`

✅ Output:

```text
[1]
[1, 2]
[3]
[1, 2, 4]
```

👉 Fix pattern:

```python
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

---

## C. Tuples & Sets – Deeper Questions

### Q9 – Tuple Containing a List

```python
t = (1, 2, [3, 4])
t[2].append(5)
print(t)
```

**Answer:**

* `t` is immutable, but it contains a **mutable list** at index 2.
* You cannot reassign `t[2]`, but you can mutate the list inside it.

✅ Output:

```text
(1, 2, [3, 4, 5])
```

---

### Q10 – Set Behavior & Duplicates

```python
s = {1, 2, 3, 2, 1}
s.add(3)
s.add(4)
print(s)
```

**Answer:**

* Duplicates are ignored.
* Set ends up containing `{1, 2, 3, 4}` (order unspecified).

Example output:

```text
{1, 2, 3, 4}
```

---

### Q11 – Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)
print(a | b)
print(a - b)
print(b - a)
```

**Answer:**

* `a & b` → intersection → `{3}`
* `a | b` → union → `{1, 2, 3, 4, 5}`
* `a - b` → in `a` not in `b` → `{1, 2}`
* `b - a` → in `b` not in `a` → `{4, 5}`

✅ Output:

```text
{3}
{1, 2, 3, 4, 5}
{1, 2}
{4, 5}
```

---

### Q12 – Unhashable Types in Sets

```python
s = {1, 2, [3, 4]}
```

**Answer:**

This will raise:

```text
TypeError: unhashable type: 'list'
```

Because:

* Elements in a set must be **hashable & immutable**.
* `list` is mutable → unhashable → cannot be a set element.

---

## D. Dictionaries – MAANG-Level Traps

### Q13 – Key Overwrite

```python
d = {"a": 1, "b": 2, "a": 3}
print(d)
```

**Answer:**

* Keys must be unique. If the same key appears multiple times in a literal, the **last value wins**.
* `"a": 1` gets overwritten by `"a": 3`.

✅ Output:

```text
{'a': 3, 'b': 2}
```

---

### Q14 – `in` on Dictionary

```python
d = {"a": 1, "b": 2}
print("a" in d)
print(1 in d)
print(2 in d.values())
```

**Answer:**

* `"a" in d` → checks **keys** → `True`
* `1 in d` → checks **keys**, not values → `False`
* `2 in d.values()` → checks in values → `True`

✅ Output:

```text
True
False
True
```

---

### Q15 – Mutating During Iteration (Classic Bug)

```python
d = {"a": 1, "b": 2, "c": 3}

for k in d:
    if k == "b":
        del d[k]

print(d)
```

**Answer:**

This is **unsafe**: modifying a dict while iterating over it can raise:

```text
RuntimeError: dictionary changed size during iteration
```

Correct pattern:

```python
for k in list(d.keys()):
    if k == "b":
        del d[k]
```

---

### Q16 – Dict with Tuple Keys

```python
point_map = {}
point_map[(0, 0)] = "origin"
point_map[(1, 2)] = "point A"

print(point_map[(1, 2)])
```

**Answer:**

* Tuples are immutable & hashable → can be used as keys.

✅ Output:

```text
point A
```

---

### Q17 – Using `get()` for Safe Access

```python
config = {"timeout": 30, "retries": 3}

print(config.get("timeout", 10))
print(config.get("delay", 5))
```

**Answer:**

* `"timeout"` exists → returns `30`
* `"delay"` doesn’t exist → returns default `5`

✅ Output:

```text
30
5
```

---

### Q18 – Dictionary Comprehension with Condition

```python
nums = [1, 2, 3, 4, 5]
d = {x: x*x for x in nums if x % 2 == 0}
print(d)
```

**Answer:**

* Take even numbers only → `2, 4`
* Map to their squares → `{2: 4, 4: 16}`

✅ Output:

```text
{2: 4, 4: 16}
```

---

## How to Use This for MAANG Prep

For each block above, practice:

1. **Close your eyes / hide answers**, predict output.
2. Then explain **why** in 1–2 sentences like you would to an interviewer.
3. Try to generalize:

   * "What rule does this demonstrate?"
   * "Where can this bug appear in real systems?"
