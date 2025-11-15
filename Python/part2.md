## Part 2: Lists in Python

### 1. What is a List?

* A **list** is:

  * **Ordered** → elements keep the order in which they’re added.
  * **Mutable** → you can change elements (add, remove, modify).
  * Can store **mixed data types**.

```python
nums = [10, 20, 30, 40]
print(nums[1])    # 20
print(nums[-1])   # 40
print(nums[1:3])  # [20, 30]

nums[2] = 35
print(nums)       # [10, 20, 35, 40]

values = [9.5, 'hello', 42, True]  # mixed types allowed
```

---

### 2. Nested Lists

You can have lists *inside* lists.

```python
nums = [10, 20, 35, 40]
values = [9.5, 'hello', 42, True]

mil = [nums, values]
print(mil)
# [[10, 20, 35, 40], [9.5, 'hello', 42, True]]
```

* `mil[0]` → `[10, 20, 35, 40]`
* `mil[1][1]` → `'hello'`

---

### 3. Common List Operations

Start with:

```python
nums = [10, 20, 30, 40]
```

#### 3.1 `append()` – Add at the End

```python
nums.append(50)
print(nums)   # [10, 20, 30, 40, 50]
```

* Adds a single element at the **end**.
* Returns `None` (modifies in place).

---

#### 3.2 `insert()` – Add at a Specific Index

```python
nums.insert(2, 25)
print(nums)   # [10, 20, 25, 30, 40, 50]
```

* Syntax: `list.insert(index, value)`
* Shifts elements right from that index.

**Difference:**

* `append(x)` → adds at the **end**.
* `insert(i, x)` → adds at **position i**.

---

#### 3.3 `remove()` – Remove by Value

```python
nums.remove(30)
print(nums)   # [10, 20, 25, 40, 50]
```

* Removes the **first occurrence** of the given value.
* Raises `ValueError` if the value is not present.

---

#### 3.4 `pop()` – Remove by Index (and Return It)

```python
popped_value = nums.pop(1)
print(popped_value)  # 20
print(nums)          # [10, 25, 40, 50]

nums.pop()           # removes last element
print(nums)          # [10, 25, 40]
```

* `pop(i)` → removes and returns element at index `i`.
* `pop()` → removes and returns the **last** element.
* Raises `IndexError` if index is out of range.

---

#### 3.5 `len()` – Length of List

```python
print(len(nums))    # 3
```

---

#### 3.6 `del` Keyword – Delete by Index

```python
del nums[0]
print(nums)         # [25, 40]
```

* `del` is a **keyword**, not a method.
* Deletes the element at a given index.
* You can also delete a slice.

---

#### 3.7 `extend()` – Add Multiple Elements

```python
nums.extend([60, 70])
print(nums)         # [25, 40, 60, 70]
```

* Adds each element from the iterable to the end of the list.
* Different from `append([60, 70])`, which would add the list itself as *one* element.

---

#### 3.8 `min()`, `max()`, `sum()`

```python
print(min(nums))   # 25
print(max(nums))   # 70
print(sum(nums))   # 25 + 40 + 60 + 70 = 195
```

* Work only if elements are comparable (e.g., all numbers).

---

#### 3.9 `sort()` – Sort the List

```python
nums.sort()
print(nums)        # [25, 40, 60, 70]
```

* Sorts the list **in place** (modifies the original).
* Returns `None` (common interview trap).
* By default, sorts in ascending order.

---

## 🎯 Interview-Style Questions (With Answers)

### 📝 Q1. Output Prediction

**Q1.1**

```python
nums = [10, 20, 30, 40]
print(nums[1])
print(nums[-1])
print(nums[1:3])
```

**Answer:**

* `nums[1]` → `20`
* `nums[-1]` → last element → `40`
* `nums[1:3]` → indices 1 and 2 → `[20, 30]`

✅ Output:

```text
20
40
[20, 30]
```

---

**Q1.2**

```python
nums = [10, 20, 30, 40]
nums[2] = 35
print(nums)
```

**Answer:**

We replace the element at index 2 (`30`) with `35`.

✅ Output:

```text
[10, 20, 35, 40]
```

---

**Q1.3**

```python
nums = [10, 20, 30]
nums.append(40)
nums.insert(1, 15)
print(nums)
```

**Answer:**

* Start: `[10, 20, 30]`
* After `append(40)` → `[10, 20, 30, 40]`
* After `insert(1, 15)` → insert `15` at index 1 → `[10, 15, 20, 30, 40]`

✅ Output:

```text
[10, 15, 20, 30, 40]
```

---

**Q1.4**

```python
nums = [10, 20, 30, 40, 50]
x = nums.pop(2)
print(x)
print(nums)
```

**Answer:**

* `nums.pop(2)` → removes and returns element at index 2 → `30`
* Remaining list → `[10, 20, 40, 50]`

✅ Output:

```text
30
[10, 20, 40, 50]
```

---

### 📝 Q2. Error-Finding / Tricky Questions

**Q2.1**

```python
nums = [10, 20, 30]
nums.remove(40)
print(nums)
```

**Question:** Will this run?

**Answer:**
No. `40` is not in the list, so:

```text
ValueError: list.remove(x): x not in list
```

---

**Q2.2**

```python
nums = [10, 20, 30]
val = nums.pop(5)
print(val)
```

**Answer:**
Index 5 does not exist (list size is 3), so:

```text
IndexError: pop index out of range
```

---

**Q2.3**

```python
nums = [25, 40, 10, 5]
sorted_nums = nums.sort()
print(sorted_nums)
```

**Question:** What gets printed?

**Answer:**

* `nums.sort()` sorts the list **in place** and returns `None`.
* So `sorted_nums` will be `None`.

✅ Output:

```text
None
```

But after this line, `nums` itself becomes `[5, 10, 25, 40]`.

Correct way to get a **new** sorted list:

```python
sorted_nums = sorted(nums)   # built-in function returns a new list
```

---

**Q2.4**

```python
nums = [10, 20]
nums.extend([30, 40])
nums.append([50, 60])
print(nums)
```

**Answer:**

* Start: `[10, 20]`
* After `extend([30, 40])` → `[10, 20, 30, 40]`
* After `append([50, 60])` → list `[50, 60]` is added as **one element**
  Final: `[10, 20, 30, 40, [50, 60]]`

✅ Output:

```text
[10, 20, 30, 40, [50, 60]]
```

---

### 📝 Q3. One-Liner Questions

**Q3.1**
Given:

```python
nums = [10, 20, 30, 40, 50]
```

Write one line to get a sublist `[20, 30, 40]`.

**Answer:**

```python
sub = nums[1:4]
```

---

**Q3.2**
Given:

```python
nums = [10, 20, 30]
```

Write one line to add `40` and `50` at the end.

**Answer:**

```python
nums.extend([40, 50])
```

---

**Q3.3**
Given:

```python
nums = [5, 2, 9, 1]
```

Write one line to sort this list in-place in ascending order.

**Answer:**

```python
nums.sort()
```

---

**Q3.4**
Given:

```python
nums = [10, 20, 30, 40]
```

Write one line to remove the last element **without** using `pop()`.

**Answer:**

```python
del nums[-1]
```

---

### 📝 Q4. Conceptual Questions

**Q4.1**
What is the difference between `append()` and `extend()`?

**Answer:**

* `append(x)` → adds `x` as a **single element** at the end.

  * If `x` is a list, the entire list becomes one element.
* `extend(iterable)` → takes each element from the iterable and adds them individually to the list.

Example:

```python
nums = [1, 2]
nums.append([3, 4])   # [1, 2, [3, 4]]

nums = [1, 2]
nums.extend([3, 4])   # [1, 2, 3, 4]
```

---

**Q4.2**
What is the difference between `remove()` and `pop()`?

**Answer:**

* `remove(value)`:

  * Removes the **first occurrence** of the value.
  * Does **not** return the removed value (returns `None`).
  * Raises `ValueError` if value not found.

* `pop(index=None)`:

  * Removes the element at the given index and **returns** it.
  * If index not given, removes and returns the **last** element.
  * Raises `IndexError` if index is out of range.

---

**Q4.3**
Are lists in Python mutable or immutable? What does that mean?

**Answer:**
Lists are **mutable** → you can change their contents in place:

* Add elements
* Remove elements
* Modify elements

Example:

```python
nums = [1, 2, 3]
nums[0] = 10       # allowed → [10, 2, 3]
```
