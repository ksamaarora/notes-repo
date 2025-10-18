## Part 9 – Git Merge and Merge Conflicts

### Git Merge

When you want to combine the work done in another branch (say `feature` or `test`) into your main branch, you use **merge**.

First, make sure you are **on the branch that will receive the changes** — in this case `main`:

```bash
git switch main
```

Always pull the latest version before merging (especially if you collaborate):

```bash
git pull origin main
```

Then merge the branch you want to bring changes from:

```bash
git merge feature
```

If everything merges cleanly, Git automatically combines both histories and creates a **merge commit**.
Finally, push the updated main branch:

```bash
git push origin main
```

---

### 🔹 Why Merge Conflicts Occur

A merge conflict happens when **the same file** (or sometimes the same line inside a file) has been changed in **both branches** that you are trying to merge.

Example:

* You edited `Git/Part8-BranchInGit.md` in `main`.
* You also edited the **same file** in `test`.

Now, when you run

```bash
git merge test
```

Git detects that both branches touched the same file differently and can’t decide whose change to keep, so it marks the file as **conflicted** and pauses the merge.

---

### 🔹 How to Recognize a Conflict

Git adds special **conflict markers** inside the file:

```text
<<<<<<< HEAD
change from main branch
=======
change from test branch
>>>>>>> test
```

* The section between `<<<<<<< HEAD` and `=======` is your current branch (main).
* The section between `=======` and `>>>>>>> test` is the incoming change from the branch being merged.

You must manually edit the file to keep the correct or combined content, and then delete the conflict markers.

---

### 🔹 How to Fix and Finish the Merge

After editing and saving the resolved file:

```bash
git add <file>
git commit -m "Resolved merge conflict in <file>"
```

Now your merge is complete and Git records a **merge commit** connecting both branch histories.

If you want to abandon the merge instead:

```bash
git merge --abort
```

---

### 🧠 Example – Relating to Your Merge

In your case:

* **Main** branch had `part 9 changes`.
* **Test** branch had `part 8 changes test branch`.
  Both edited `Part8-BranchInGit.md`.

When you merged `test` into `main`, Git threw:

```
CONFLICT (add/add): Merge conflict in Git/Part8-BranchInGit.md
```

You opened the file, chose the correct content, staged, and committed:

```bash
git add .
git commit -m "Resolved merge conflict in Part8-BranchInGit.md"
```

This created a merge commit (`00bb7c88`) that joined both histories.

---

### 🔁 Quick Checklist for Safe Merging

1. `git switch main` → move to the branch that will receive changes.
2. `git pull origin main` → make sure you’re up to date.
3. `git merge feature` → bring in another branch.
4. If conflict appears → open file → edit → save → `git add .` → `git commit`.
5. `git push origin main` → upload merged result.

---

### 💡 Extra Concepts

* **Auto Merge:** Git merges automatically when changes are in different files or non-overlapping lines.
* **Manual Merge:** Needed when both branches changed the same part of a file.
* **Merge Commit:** A special commit that has **two parents** (one from each branch).
* **Pull Before Merge:** Avoids remote conflicts when collaborators pushed new commits you don’t yet have.

---

### 🪞 Analogy

Think of two people editing the same paragraph in a Google Doc offline. When they both upload their versions, Google asks which version to keep — that’s exactly what a **merge conflict** is. You decide the final paragraph, save, and sync — that’s your **merge commit**.
