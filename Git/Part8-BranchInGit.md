## Part 8 – Git Branch

### What is Branching?

Branching in Git means creating a separate line of development — a copy of your project where you can make changes without affecting the main code. Each branch has its own commits and history. By default, Git starts with a branch named **main** (earlier called **master**).

You can create a new branch directly from GitHub or using the terminal. If a branch already exists, you can switch to it using:

```bash
git checkout branchname
```

or

```bash
git switch branchname
```

If you want to **create and switch** to a new branch in one command, use:

```bash
git checkout -b branchname
```

To view all branches:

```bash
git branch
```

The branch marked with `*` is the one you are currently working on. Any changes, additions, or commits you make will belong only to that active branch.

If you modify files, add, and commit them inside a branch (say `feature`), those commits will stay within `feature`. When you switch back to `main`, it will have no idea of those changes — because main is still pointing to its older commit history.

---

### How Branching Works Internally

Every time you make a commit, Git takes a **snapshot** of your files and gives it a **unique checksum** (commit ID).
There’s also a **pointer** that keeps track of where you are.

Let’s say you have three commits — snapshots 1, 2, and 3 — with 3 being the latest.

At commit 3, **HEAD → main → snapshot 3**.
The **HEAD** always points to the branch you are currently on.

If you create a new branch called `test` at this point, Git will make:

```
HEAD → test → snapshot 3
```

Both `main` and `test` now point to the same commit (snapshot 3).

If you now make new changes and commit while inside `test`, Git creates **snapshot 4**, and the **test branch** moves ahead to point to this new commit. The **main branch** still points to snapshot 3, so it doesn’t see the new changes.

---

### Explanation Using Your Diagram

<img width="700" height="495" alt="Screenshot 2025-10-18 at 8 27 58 AM" src="https://github.com/user-attachments/assets/2d3700ef-81aa-4319-8a39-706e63da78d8" />


In your Git graph (from VS Code), you can see:

* The **blue line** represents the **main branch**.
* The **pink line** represents the **test branch**.
* Each dot is a **commit** (a snapshot of your project).
* The arrows (`→`) show how branches diverge and point to their latest commits.

Here’s what the diagram shows:

1. The main branch (`main`) has commits like *part 7*, *part 6*, etc.
2. At *part 7*, a new branch (`test`) was created.
3. The `test` branch has one extra commit — *part 8*.
4. The main branch has moved forward to a new commit (*changes*) that hasn’t been merged yet.
5. That’s why you see two diverging lines — one for **main** and one for **test** — representing different development paths.
6. The **HEAD** pointer moves depending on which branch you’re currently on (shown in blue or pink in your diagram).

---

### 🔁 Common Branch Commands

| Command                      | Description                                |
| ---------------------------- | ------------------------------------------ |
| `git branch`                 | Lists all branches                         |
| `git branch -M main`         | Renames current branch to main             |
| `git checkout -b feature1`   | Creates and switches to new branch         |
| `git switch feature1`        | Switches to an existing branch             |
| `git branch -`               | Switches back to the previous branch       |
| `git branch -d branchname`   | Deletes a local branch                     |
| `git push origin branchname` | Pushes a branch to the remote repo         |
| `git merge branchname`       | Merges another branch into the current one |

---

### Simple Analogy

Think of **branches** like different timelines in a video editor:

* `main` is your final timeline.
* `test` or `feature` branches are experimental tracks where you try new edits.
* Once happy with the changes, you merge them back into `main`.
