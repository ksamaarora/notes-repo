## Part 10 – Git Time Travel, Stash, Fork & Pull Request

### Git Time Travel

Git allows you to **move through history** — to go back to any previous commit or version of your project.
Every commit in Git is like a snapshot in time, identified by a unique **commit hash (checksum)** such as `00bb7c88f1c6fb551fd495b4682e82b9c374cd01`.

If you want to explore or test an older version without disturbing your current code, first create a new branch:

```bash
git checkout -b lite-version
```

Then move (or “checkout”) to a specific commit:

```bash
git checkout 00bb7c88f1c6fb551fd495b4682e82b9c374cd01
```

Git will display a message saying you are in a **“detached HEAD” state**.

This means:

* You are not currently on any branch.
* You’re viewing the repository exactly as it was at that commit.
* You can look around or even make temporary changes.
* But if you make new commits here, they won’t belong to any branch unless you create one using:

  ```bash
  git switch -c new-branch-name
  ```

In simple words, **detached HEAD** lets you travel to the past, explore, or test something without affecting your main timeline. When done, return to your latest branch using:

```bash
git switch main
```

---

### Git Stash

Sometimes you’re in the middle of working on something (say an AI feature in your `feature` branch), and your manager asks you to fix an urgent bug in `main`.
If you try switching directly:

```bash
git switch main
```

Git will block you with:

```
error: Your local changes to the following files would be overwritten by checkout
```

because it doesn’t want to lose your uncommitted work.

To temporarily **save** those changes without committing, use:

```bash
git stash
```

This stores your uncommitted changes safely and restores your working directory to a clean state, allowing you to switch branches.

Now you can go fix things in the main branch.

Once done, return to your previous branch and bring back your saved work using:

```bash
git stash apply
```

or

```bash
git stash pop
```

(`pop` also removes it from stash after applying).

For example, from your terminal logs:

```
git stash
Saved working directory and index state WIP on main: 221f442 changes added
```

This means your changes were saved with a note referencing the last commit ID. Later you did:

```
git stash apply
```

and your modifications in `Part10-GitTimeTravel_Stash_PullRequest.md` were restored.

**In short:**

* `git stash` → save your incomplete work temporarily.
* `git stash apply` → reapply it later.
* `git stash pop` → reapply and remove from stash.
* `git stash list` → view all stashed items.

---

### Git Fork

When you want to contribute to someone else’s project (like an open-source repo), you don’t edit their repository directly.
Instead, you **fork** it — meaning GitHub creates a **copy** of their repo under your own account.
You can now work freely on your fork without affecting the original.

Steps after forking:

1. Clone your fork to your local system.
2. Make changes in your local repo.
3. Stage and commit your updates:

   ```bash
   git add .
   git commit -m "Added new feature"
   ```
4. Push them to your fork:

   ```bash
   git push origin main
   ```

---

### 🔹 Git Pull Request

Now your forked repository has your changes, but you want them to be merged into the **original** project.
This is where a **pull request (PR)** comes in.

A pull request is basically a **request to merge** your changes into someone else’s repository.

Steps:

1. Go to the **original GitHub repository** page.
2. Click **“Compare & Pull Request.”**
3. Review the differences and add a short title or description.
4. Submit the pull request.

The project owner will review your changes, comment if needed, and either merge or reject your PR.

---

### Example Recap

Imagine you’re building `feature-A` in your repo, but need to fix an urgent issue in `main`.
You:

* `git stash` → safely store unfinished feature work.
* `git switch main` → move to fix the issue.
* Make the fix → `git add .`, `git commit -m "fix issue"`, `git push`.
* `git switch feature-A` → return to your branch.
* `git stash apply` → get your previous unfinished work back.

This flow lets you handle interruptions **without losing progress**.

---

### Quick Summary

| Command                  | Purpose                                          |
| ------------------------ | ------------------------------------------------ |
| `git checkout <commit>`  | View a previous commit (time travel)             |
| `git stash`              | Temporarily save uncommitted work                |
| `git stash apply`        | Bring back stashed work                          |
| `git switch -c <branch>` | Create and switch to new branch                  |
| `git fork`               | Copy someone else’s repo into your account       |
| `git push origin main`   | Push local changes to your repo                  |
| **Pull Request**         | Ask to merge your changes into the original repo |
