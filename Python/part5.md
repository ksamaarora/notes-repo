## Part 5 – More on Variables & Objects in Python

### 1️⃣ What really happens in `num = 5`?

```python
num = 5
```

Behind the scenes, Python does:

1. **Object Creation**

   * Creates an `int` object with value `5` (or reuses an existing one if already created and interned).

2. **Memory Allocation**

   * That `int` object lives at some memory location (managed by Python’s runtime, not you).

3. **Name Binding (Reference Assignment)**

   * The *name* `num` is bound (assigned) to that object.
   * `num` is not a “box”, but a **label** pointing to an object.

You can see the object’s “identity” (implementation-specific memory-like address) using `id()`:

```python
num = 5
print(id(num))   # some integer representing the identity of the object 5
```

> Concept:
>
> * **Variable name** → label
> * **Object** → actual data (e.g., `5`)
> * `id(obj)` → a number representing the identity of that object.

---

### 2️⃣ Multiple Names, Same Object

```python
a = 10
b = a
```

Here:

* Python has **one** `int` object with value `10`.
* Two names: `a` and `b` → both reference the **same** object.

```python
print(id(a))
print(id(b))
# Both are the same
```

So:

* Number of *objects*: 1 (the integer `10`)
* Number of *names* pointing to it: 2 (`a`, `b`)

---

### 3️⃣ Same Value, Possibly Same Object

You wrote:

```python
x = 1000
y = 1000
print(id(x))
print(id(y))
```

Important clarification for interviews:

* In CPython, **small integers** (typically in range −5 to 256) are **interned** (reused), so they definitely share identity.
* For larger integers like `1000`, sometimes they **may** share identity (due to optimizations), sometimes not – it’s implementation-dependent.

So the **safe mental model** is:

> Names bind to objects.
> Objects store values.
> Python *may* reuse objects with the same value for optimization, especially small ints and some strings, but you should **not rely on this** in your logic.

However:

```python
print(id(1000))   # identity of the literal object 1000
```

This shows the identity of the `int` object for `1000` **in that expression**.

Key idea:

> **Address / identity belongs to the object (value instance), not to the variable name.**

---

### 4️⃣ Rebinding a Name

```python
a = 10
b = a        # both point to the same object 10

a = 20       # a is now rebound to a new int object 20
```

Now:

* `b` still points to the `int` object `10`.
* `a` points to a different `int` object `20`.

```python
print(id(a))   # identity of 20
print(id(b))   # identity of 10
```

If you do:

```python
k = a
print(id(k))   # same as id(a) because k and a refer to the same object (20)
```

---

### 5️⃣ What happens to old objects? (Garbage Collection)

```python
a = 10
b = a
a = 20
b = 8
```

* Initially: `10` is referenced by `a` and `b`.
* After `a = 20`:

  * `a` → 20
  * `b` → 10
* After `b = 8`:

  * `a` → 20
  * `b` → 8
  * Now **no name** points to `10`.

At this point:

> The `int` object `10` has **no references**.
> Python’s **garbage collector** can reclaim that memory at some point.

You **don’t** control when exactly, but logically it becomes **eligible for garbage collection**.

---

### 6️⃣ Checking Types

Use `type()` to see an object’s type:

```python
a = 20
print(type(a))     # <class 'int'>

name = "Alice"
print(type(name))  # <class 'str'>
```

---

## 🎯 Normal Interview-Style Questions (With Answers)

### Q1 – Identity and Rebinding

**Q1.1**

```python
a = 5
b = 5

print(a == b)
print(a is b)
```

**Answer:**

* `a == b` checks **value** → `5 == 5` → `True`
* `a is b` checks **identity** (same object).
  For small integers like 5, CPython **interns** them, so this is usually `True`.

Typical output:

```text
True
True
```

Interview line:

> Always use `==` for value comparison. `is` is for identity or checking `None`.

---

**Q1.2**

```python
a = 1000
b = 1000

print(a == b)
print(a is b)
```

**Answer:**

* `a == b` → `True` (values equal)
* `a is b` → **implementation dependent**.
  On many CPython builds, this may be `False`, because `1000` is not in the small-integer cache.

You should **not rely** on `is` for numeric equality.

---

### Q2 – Name Binding and Garbage Collection

**Q2.1**

```python
a = 10
b = a
a = 20

print(a)
print(b)
```

**Answer:**

* After `a = 10`, `b = a` → both refer to `10`.
* After `a = 20`, `a` is rebound to `20`. `b` still points to `10`.

✅ Output:

```text
20
10
```

---

**Q2.2**

Explain what happens conceptually here:

```python
x = 30
y = x
x = x + 5
```

**Answer:**

* `x = 30` → name `x` bound to object `30`.
* `y = x` → `y` also bound to object `30`.
* `x = x + 5`:

  * `x + 5` creates a **new** `int` object with value `35`.
  * `x` is rebound to that new object.
* `y` still refers to `30`.

---

### Q3 – `id()` and Types

**Q3.1**

```python
a = 5
print(type(a), id(a))

a = "hello"
print(type(a), id(a))
```

**Answer:**

* First line: `a` is `int` → `<class 'int'>`, some identity.
* After reassigning to `"hello"`:

  * `a` becomes `<class 'str'>`
  * `id(a)` changes → now it’s the identity of the string object.

Output example (identity will vary):

```text
<class 'int'> 140736516870368
<class 'str'> 140736516927600
```

---

### Q4 – Immutability vs “Changing a Variable”

**Q4.1**
If integers are immutable, how can we “change” `a` from 10 to 20?

```python
a = 10
a = 20
```

**Answer:**

We do **not** change the `int` object `10`.
We simply **rebind** the name `a` from the object `10` to a *new* object `20`.

Immutability is about the **object**, not the variable name.

---

## 🔥 MAANG / FAANG All-Time Favorite Questions on This Topic

These are the kind of subtle identity / mutability / binding questions they love.

---

### 🧠 Q1 – `is` vs `==` with Small and Big Integers

```python
a = 256
b = 256
c = 257
d = 257

print(a is b)
print(c is d)
```

**Answer:**

* For CPython:

  * Small integers (commonly −5 to 256) are interned → `a is b` → `True`.
  * Larger integers **may not be interned** → `c is d` is often `False`.

Typical CPython output:

```text
True
False
```

Interview takeaway:

> * `==` → value
> * `is` → identity
> * Don’t rely on interning for functional correctness.

---

### 🧠 Q2 – Strings and Interning

```python
s1 = "hello_world"
s2 = "hello_" + "world"
s3 = "".join(["hello_", "world"])

print(s1 == s2, s1 is s2)
print(s1 == s3, s1 is s3)
```

**Answer:**

* `"hello_" + "world"` is a constant expression → compiled into the same literal → `s1 is s2` often `True`.
* `"".join([...])` builds a string at runtime → may return **a different object** with the same value.

Typical:

```text
True True
True False
```

Key point: string interning is an optimization; **never** use `is` to compare string values in normal code.

---

### 🧠 Q3 – Function Parameters & Rebinding

```python
def modify(x, lst):
    x = x + 1
    lst.append(4)

a = 10
b = [1, 2, 3]

modify(a, b)
print(a)
print(b)
```

**Answer:**

* `x = x + 1` → creates a new int `11` and binds local name `x` to it. Does **not** affect `a`.
* `lst.append(4)` → mutates the list object that both `lst` and `b` refer to.

✅ Output:

```text
10
[1, 2, 3, 4]
```

Interview line:

> Python uses **pass-by-object-reference** (or “call by sharing”):
>
> * Rebinding a parameter name doesn’t affect the caller.
> * Mutating the object does.

---

### 🧠 Q4 – Subtle `is` with Booleans and Integers

```python
print(True == 1)
print(True is 1)
print(False == 0)
print(False is 0)
```

**Answer:**

* `bool` is a subclass of `int` in Python:

  * `True == 1` → `True`
  * `False == 0` → `True`
* But they are **not the same object**:

  * `True is 1` → `False`
  * `False is 0` → `False`

✅ Output:

```text
True
False
True
False
```

---

### 🧠 Q5 – Identity Across Reassignments

```python
x = 5
y = x
print(id(x), id(y))

x += 1
print(id(x), id(y))
```

**Answer:**

* Initially:

  * `x` and `y` both refer to `5` → same `id`.
* After `x += 1`:

  * For integers, `x += 1` is equivalent to `x = x + 1` → new object `6`.
  * `x` now refers to `6`, `y` still refers to `5`.
  * `id(x)` changes, `id(y)` remains the same.

✅ Behavior:

1st print: same ids
2nd print: different ids.

---

### 🧠 Q6 – Tricky: Variables in a Loop

```python
for i in range(3):
    x = 10
print(id(x))
```

**Question:**
How many times is the object `10` created here?

**Answer:**

* `10` is an interned small integer. The object for `10` is typically created **once**, and reused.
* `x = 10` inside the loop just keeps re-binding the name `x` to that same object.

Conceptual answer for interviews:

> Only one `int` object for value `10` is used; the variable `x` is repeatedly rebound to it.

---

### 🧠 Q7 – Identity of Literals

```python
print(id(5))
a = 5
print(id(a))
```

**Answer:**

In CPython, both refer to the **same interned `int` object**.

So both `id(5)` and `id(a)` will be the same.

This demonstrates again that:

> `a` is just a name; the object is the thing that has identity.
