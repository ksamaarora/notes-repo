## Part 7 – Operators in Python

### Operator Categories

* **Arithmetic Operators**
* **Assignment Operators**
* **Relational (Comparison) Operators**
* **Logical Operators**
* **Unary Operators**
* **Bitwise Operators**

---

## 1️⃣ Arithmetic Operators

Used for basic math.

| Operator | Description         | Example  | Result    |
| -------- | ------------------- | -------- | --------- |
| `+`      | Addition            | `5 + 3`  | `8`       |
| `-`      | Subtraction         | `5 - 3`  | `2`       |
| `*`      | Multiplication      | `5 * 3`  | `15`      |
| `/`      | True Division       | `5 / 3`  | `1.6666…` |
| `//`     | Floor Division      | `5 // 3` | `1`       |
| `%`      | Modulus (remainder) | `5 % 3`  | `2`       |
| `**`     | Exponentiation      | `5 ** 3` | `125`     |

> Note: `/` always returns a `float` in Python 3.

### Quick Questions

**Q1.1**

```python
print(7 / 2)
print(7 // 2)
print(7 % 2)
```

**Answer:**

* `7 / 2` → `3.5` (true division)
* `7 // 2` → `3` (floor division)
* `7 % 2` → `1` (remainder)

---

**Q1.2**

```python
print(2 ** 3 ** 2)
```

**Answer:**

`**` is **right-associative**:

* `3 ** 2` → `9`
* `2 ** 9` → `512`

✅ Output: `512`

---

## 2️⃣ Assignment Operators

Used to assign and update values.

| Operator | Meaning                 | Example   | Equivalent to |
| -------- | ----------------------- | --------- | ------------- |
| `=`      | Assign                  | `x = 5`   | `x = 5`       |
| `+=`     | Add and assign          | `x += 3`  | `x = x + 3`   |
| `-=`     | Subtract and assign     | `x -= 3`  | `x = x - 3`   |
| `*=`     | Multiply and assign     | `x *= 3`  | `x = x * 3`   |
| `/=`     | Divide and assign       | `x /= 3`  | `x = x / 3`   |
| `%=`     | Modulus and assign      | `x %= 3`  | `x = x % 3`   |
| `//=`    | Floor divide and assign | `x //= 3` | `x = x // 3`  |
| `**=`    | Power and assign        | `x **= 3` | `x = x ** 3`  |

### Quick Question

**Q2.1**

```python
x = 5
x += 2
x *= 3
print(x)
```

**Answer:**

* Start: `x = 5`
* After `x += 2` → `7`
* After `x *= 3` → `21`

✅ Output: `21`

---

## 3️⃣ Relational (Comparison) Operators

Used to compare two values. Result is always a **boolean** (`True` or `False`).

| Operator | Description              | Example  | Result  |
| -------- | ------------------------ | -------- | ------- |
| `==`     | Equal to                 | `5 == 3` | `False` |
| `!=`     | Not equal to             | `5 != 3` | `True`  |
| `>`      | Greater than             | `5 > 3`  | `True`  |
| `<`      | Less than                | `5 < 3`  | `False` |
| `>=`     | Greater than or equal to | `5 >= 3` | `True`  |
| `<=`     | Less than or equal to    | `5 <= 3` | `False` |

Python also supports **chained comparisons**:

```python
1 < x < 5   # equivalent to (1 < x) and (x < 5)
```

### Quick Questions

**Q3.1**

```python
print(5 == 5.0)
print(5 is 5.0)
```

**Answer:**

* `5 == 5.0` → `True` (values equal)
* `5 is 5.0` → `False` (different objects/types)

---

**Q3.2**

```python
x = 3
print(1 < x < 5)
print(1 < x > 5)
```

**Answer:**

* `1 < x < 5` → `True` (3 is between 1 and 5)
* `1 < x > 5` → check: `1 < x` and `x > 5`
  → `1 < 3` is `True`, but `3 > 5` is `False` → overall `False`

✅ Output:

```text
True
False
```

---

## 4️⃣ Logical Operators

Used to combine boolean expressions.

| Operator | Description | Example               | Result  |
| -------- | ----------- | --------------------- | ------- |
| `and`    | Logical AND | `(5 > 3) and (2 < 4)` | `True`  |
| `or`     | Logical OR  | `(5 > 3) or (2 > 4)`  | `True`  |
| `not`    | Logical NOT | `not (5 > 3)`         | `False` |

Important: `and` / `or` **short-circuit** and in Python they actually return one of the operands, not always a strict boolean (we’ll use that in FAANG part).

### Quick Question

**Q4.1**

```python
a = 5
b = 2
print(a > 3 and b < 5)
print(a < 3 or b < 5)
print(not (a > b))
```

**Answer:**

* `a > 3 and b < 5` → `True and True` → `True`
* `a < 3 or b < 5` → `False or True` → `True`
* `not (a > b)` → `not (True)` → `False`

---

## 5️⃣ Unary Operators

Operate on a **single** operand.

| Operator | Description | Example | Result |
| -------- | ----------- | ------- | ------ |
| `+`      | Unary plus  | `+5`    | `5`    |
| `-`      | Unary minus | `-5`    | `-5`   |
| `~`      | Bitwise NOT | `~5`    | `-6`   |

Explanation of `~n`:

* `~n` = `-(n + 1)`
  e.g. `~5 = -(5 + 1) = -6`

### Quick Question

**Q5.1**

```python
print(~0)
print(~1)
print(~-1)
```

**Answer:**

Using `~n = -(n + 1)`:

* `~0` → `-(0 + 1)` → `-1`
* `~1` → `-(1 + 1)` → `-2`
* `~-1` → `-(-1 + 1)` → `-0` → `0`

✅ Output:

```text
-1
-2
0
```

---

## 6️⃣ Bitwise Operators

Operate at the **bit** level (on integers).

Let’s use `5` (`0101` in binary) and `3` (`0011` in binary).

| Operator | Description | Example  | Result | Binary Result |
| -------- | ----------- | -------- | ------ | ------------- |
| `&`      | Bitwise AND | `5 & 3`  | `1`    | `0001`        |
| `\|`     | Bitwise OR  | `5 \| 3` | `7`    | `0111`        |
| `^`      | Bitwise XOR | `5 ^ 3`  | `6`    | `0110`        |
| `<<`     | Left shift  | `5 << 1` | `10`   | `1010`        |
| `>>`     | Right shift | `5 >> 1` | `2`    | `0010`        |

* Left shift `n << k` → roughly `n * 2**k` for non-negative integers.
* Right shift `n >> k` → roughly `n // 2**k` for non-negative integers.

### Quick Question

**Q6.1**

```python
print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(8 >> 2)
print(3 << 3)
```

**Answer:**

* `5 & 3` → `1`
* `5 | 3` → `7`
* `5 ^ 3` → `6`
* `8 >> 2` → `8 // 4` → `2`
* `3 << 3` → `3 * 8` → `24`

✅ Output:

```text
1
7
6
2
24
```

---

## 🔥 FAANG / MAANG Favourite Questions on Operators

Now the spicier stuff that *actually* appears in interviews.

---

### 🧠 Q1 – Logical `and` / `or` Return Values (Not Just True/False)

```python
print(0 and 5)
print(5 and 0)
print(5 and 10)
print(0 or 5)
print(5 or 0)
print("" or "hello")
```

**Answer:**

Python’s `and` / `or` return **one of the operands**, not forced booleans.

* `A and B` → returns `A` if `A` is falsy else `B`
* `A or B` → returns `A` if `A` is truthy else `B`

So:

* `0 and 5` → `0` (first is falsy, so returned)
* `5 and 0` → `0` (first truthy → returns second)
* `5 and 10` → `10`
* `0 or 5` → `5` (0 is falsy, so returns second)
* `5 or 0` → `5` (first truthy)
* `"" or "hello"` → `"hello"`

✅ Output:

```text
0
0
10
5
5
hello
```

---

### 🧠 Q2 – Operator Precedence

```python
x = 5
y = 10
z = 0

print(x > 3 and y < 15 or z == 1)
print(x > 10 or y < 5 and z == 0)
```

**Answer:**

Precedence (high → low):
`not` > `and` > `or`

1. `x > 3 and y < 15 or z == 1`

   * `x > 3` → `True`
   * `y < 15` → `True`
   * So `True and True` → `True`
   * `z == 1` → `False`
   * `True or False` → `True`

2. `x > 10 or y < 5 and z == 0`

   * `y < 5 and z == 0` evaluated first:

     * `y < 5` → `False`
     * `False and z == 0` → `False`
   * `x > 10` → `False`
   * `False or False` → `False`

✅ Output:

```text
True
False
```

---

### 🧠 Q3 – Bitwise vs Logical Confusion

```python
a = 1   # 0001
b = 2   # 0010

print(a & b)
print(a and b)
```

**Answer:**

* `a & b` → bitwise AND:

  * `0001 & 0010` → `0000` → `0`
* `a and b` → logical `and`:

  * `a` is truthy, so `and` returns `b` → `2`

✅ Output:

```text
0
2
```

---

### 🧠 Q4 – `is` vs `==` with Operators

```python
a = 256
b = 256
c = 257
d = 257

print(a == b, a is b)
print(c == d, c is d)
```

**Answer:**

* `a == b` → `True`, `a is b` → often `True` (small-int caching)
* `c == d` → `True`, `c is d` → often `False`

Typical CPython output:

```text
True True
True False
```

Key interview line:

> Use `==` for equality. `is` is for identity (e.g. `is None`), and behaviour with numbers is implementation detail.

---

### 🧠 Q5 – Unary Minus & Bitwise NOT Together

```python
x = 5
print(-x)
print(~x)
print(~(-x))
```

**Answer:**

* `-x` → `-5`
* `~x` → `-(x + 1)` → `-(5 + 1)` → `-6`
* `~(-x)` → `~(-5)` → `-(-5 + 1)` → `-(-4)` → `4`

✅ Output:

```text
-5
-6
4
```

---

### 🧠 Q6 – Complex Expression with Bitwise & Shift

```python
x = 5   # 0101
y = 3   # 0011

res = (x & y) << 2 | (x ^ y)
print(res)
```

**Answer:**

* `x & y` → `0101 & 0011` → `0001` → `1`
* `(x & y) << 2` → `1 << 2` → `4` (`0100`)
* `x ^ y` → `0101 ^ 0011` → `0110` → `6`
* `4 | 6`:

  * `0100 | 0110` → `0110` → `6`

✅ Output: `6`

---

### 🧠 Q7 – Assignment vs Comparison Mistake (Conceptual)

In Python:

```python
# if (x = 5):    # ❌ this is invalid syntax in Python
#     print("Hello")
```

**Question:** Why is this invalid, and what should be used instead?

**Answer:**

* In Python, `=` is **only** for assignment, not allowed inside expressions like `if` conditions.
* For comparison, you must use `==`.
* Python also has the **walrus operator** `:=` (for assignment expressions), but that’s separate and more advanced.

Correct check:

```python
if x == 5:
    print("Hello")
```
