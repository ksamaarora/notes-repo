## Part 8 – `if / elif / else` in Python

### Basic Structure

```python
x = 7
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")
else:
    print("x is less than or equal to 5")
```

**Output:**

```text
x is greater than 5 but less than or equal to 10
```

Key points:

* Only **one** branch runs.
* Conditions are checked **top to bottom**:

  * First `if`,
  * then `elif`s,
  * finally `else` (optional).
* `elif` and `else` depend on the `if` directly above them (indentation matters).

### Quick Questions

**Q8.1**

```python
x = 3
if x > 5:
    print("A")
elif x == 3:
    print("B")
else:
    print("C")
```

**Answer:**

* `x > 5` → `False`
* `x == 3` → `True` → prints `"B"`

✅ Output:

```text
B
```

---

**Q8.2**

What will this print?

```python
x = 10
if x > 5:
    print("A")
if x > 8:
    print("B")
else:
    print("C")
```

**Answer:**

Important: the `else` here is paired with the **second** `if`, not the first.

* First `if x > 5` → `True` → print `"A"`
* Second `if x > 8` → `True` → print `"B"`
  (`else` is skipped because the `if` was True)

✅ Output:

```text
A
B
```

---

## 🧩 Part 9 – `while` Loops & Nested Loops

### Basic `while` Loop

```python
count = 0
while count < 5:
    print("Count is:", count)
    count += 1
```

**Output:**

```text
Count is: 0
Count is: 1
Count is: 2
Count is: 3
Count is: 4
```

Key points:

* `while <condition>` runs **as long as** condition is `True`.
* You must update something inside; otherwise, you may get an infinite loop.

---

### Nested Loops (`loop in loops`)

```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```

**Output:**

```text
i: 0, j: 0
i: 0, j: 1
i: 1, j: 0
i: 1, j: 1
i: 2, j: 0
i: 2, j: 1
```

Total iterations: `3 * 2 = 6`.

### Quick Questions

**Q9.1**

What does this print?

```python
count = 3
while count > 0:
    print(count)
    count -= 1
```

**Answer:**

* Start: `3`, then `2`, then `1` → stops at `0`.

✅ Output:

```text
3
2
1
```

---

**Q9.2**

Will this loop terminate?

```python
x = 0
while x < 5:
    print(x)
```

**Answer:**

No. `x` is never incremented, so `x < 5` is always `True`.
This is an **infinite loop** (until you manually stop it).

---

## 🧩 Part 10 – `for` Loops in Python

### Looping over a List

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Output:**

```text
apple
banana
cherry
```

---

### `for i in range(5)`

```python
for i in range(5):
    print(i)
```

**Output:**

```text
0
1
2
3
4
```

* `range(5)` → `0, 1, 2, 3, 4`

---

### `for i in range(start, stop, step)`

```python
for i in range(2, 10, 2):
    print(i)
```

**Output:**

```text
2
4
6
8
```

```python
for i in range(7, 2, -1):
    print(i)
```

**Output:**

```text
7
6
5
4
3
```

Key: `range(start, stop, step)` includes `start`, excludes `stop`.

### Quick Questions

**Q10.1**

What does this print?

```python
for i in range(3):
    print(i)
```

**Answer:**

`0, 1, 2`.

✅ Output:

```text
0
1
2
```

---

**Q10.2**

What does this print?

```python
for i in range(5, 0, -2):
    print(i)
```

**Answer:**

Sequence: 5, 3, 1 (stop is `0` *excluded*).

✅ Output:

```text
5
3
1
```

---

## 🧩 Part 11 – `break` and `continue`

### `break` Statement

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

**Output:**

```text
0
1
2
3
4
```

* Loop stops completely when `i == 5` (break exits the current loop).

---

### `continue` Statement

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

**Output:**

```text
1
3
5
7
9
```

* `continue` skips the rest of the current iteration and goes to the **next** one.
* Here, we skip even numbers (where `i % 2 == 0`).

### Quick Questions

**Q11.1**

What does this print?

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

**Answer:**

Skip `2`, print others.

✅ Output:

```text
0
1
3
4
```

---

**Q11.2**

What does this print?

```python
for i in range(5):
    if i == 2:
        break
    print(i)
```

**Answer:**

Break when `i == 2`.

✅ Output:

```text
0
1
```

---

## 🧩 Part 12 – `pass` Statement

### `pass` as a Placeholder

```python
for i in range(5):
    if i < 3:
        pass  # Placeholder for future code
    else:
        print(i)
```

**Output:**

```text
3
4
```

* `pass` does nothing – it’s used when syntactically a statement is required, but you don’t want to do anything yet.

Example:

```python
def todo_feature():
    pass  # TODO: implement later
```

---

### Quick Questions

**Q12.1**

What’s the difference between `pass` and `continue` inside a loop?

**Answer:**

* `pass` → does nothing. Execution continues normally to the next statement in the **same iteration**.
* `continue` → skips the rest of the current iteration and jumps to the **next iteration** of the loop.

---

**Q12.2**

What will this print?

```python
for i in range(3):
    pass
print("Done")
```

**Answer:**

The loop runs 3 times doing nothing, then prints `"Done"`.

✅ Output:

```text
Done
```

---

## 🔥 MAANG / FAANG All-Time Favourite Questions on `if` + Loops + break/continue/pass

Now the fun, tricky stuff they like to use to probe depth.

---

### 🧠 Q1 – `for-else` and `while-else` with `break`

**Q1.1**

```python
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Completed")
```

**Question:** What is the output?

**Answer:**

* Loop runs: `i = 0, 1, 2, 3`
* When `i == 3`, we `break`, so the loop exits **before** reaching `else`.
* `else` on a loop only runs if the loop **did not** break.

✅ Output:

```text
0
1
2
```

(`"Completed"` is **not** printed.)

---

**Q1.2**

```python
for i in range(5):
    if i == 10:
        break
    print(i)
else:
    print("Completed")
```

**Answer:**

* Condition `i == 10` is never true, so we never break.
* Loop finishes normally → `else` executes.

✅ Output:

```text
0
1
2
3
4
Completed
```

---

### 🧠 Q2 – `while-else` Behaviour

```python
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Done")
```

**Answer:**

No break, loop finishes normally → `else` runs.

✅ Output:

```text
0
1
2
Done
```

---

```python
count = 0
while count < 3:
    print(count)
    if count == 1:
        break
    count += 1
else:
    print("Done")
```

**Answer:**

* `count = 0`: print `0`, not break, then `count = 1`.
* `count = 1`: print `1`, then `break`.

Loop ends via `break` → `else` **does not** execute.

✅ Output:

```text
0
1
```

---

### 🧠 Q3 – Modifying Loop Variable Inside Loop

```python
for i in range(5):
    print(i)
    i = 100
```

**Question:** Does changing `i` affect the loop?

**Answer:**

No. The `for` loop gets the next value from `range(5)` each iteration. Manually assigning `i = 100` doesn’t change what `range(5)` will yield next.

✅ Output:

```text
0
1
2
3
4
```

---

### 🧠 Q4 – Nested Loops and Total Iterations

```python
count = 0
for i in range(3):
    for j in range(4):
        count += 1

print(count)
```

**Answer:**

* Outer loop: 3 times (`i = 0,1,2`)
* Inner loop: 4 times per outer iteration
* Total: `3 * 4 = 12`

✅ Output:

```text
12
```

---

### 🧠 Q5 – `continue` and `else`

```python
for i in range(5):
    if i % 2 == 0:
        continue
    print(i)
else:
    print("Done")
```

**Answer:**

* `continue` doesn’t stop the loop, just skips some iterations.
* Since we never `break`, the `else` will run.

Odd numbers printed, then `"Done"`.

✅ Output:

```text
1
3
Done
```

---

### 🧠 Q6 – `if` with Truthy / Falsy

```python
values = [0, 1, "", "hello", [], [1]]

for v in values:
    if v:
        print(f"{v!r} is truthy")
    else:
        print(f"{v!r} is falsy")
```

**Answer:**

* Falsy: `0`, `""`, `[]`
* Truthy: `1`, `"hello"`, `[1]`

✅ Output:

```text
0 is falsy
1 is truthy
'' is falsy
'hello' is truthy
[] is falsy
[1] is truthy
```

---

### 🧠 Q7 – `break` Inside Nested Loops

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
```

**Answer:**

* Inner loop breaks whenever `j == 1` → so for each `i`, we only print `j = 0`.

So:

* `i = 0` → `j = 0` printed, then `j = 1` → break inner loop.
* `i = 1` → same
* `i = 2` → same

✅ Output:

```text
0 0
1 0
2 0
```

---

### 🧠 Q8 – `pass` vs Empty Block Error

```python
if True:
    # TODO: implement later
    pass
```

**Question:** Why is `pass` useful here?

**Answer:**

* Python does **not** allow an empty block (you’ll get `IndentationError` or `SyntaxError`).
* `pass` is a **no-op statement** that keeps the syntax valid while doing nothing.
* It’s a way to mark “to be implemented later”.
