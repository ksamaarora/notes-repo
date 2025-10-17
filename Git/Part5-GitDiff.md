## Part 5 – Git Diff

`git diff` is used to **compare changes** in your working directory and see exactly what has been modified since the last commit. It shows the differences line by line — what has been added, removed, or changed.

For example:
If you originally had the line

```
Hey whats up
```

and you changed it to

```
Hey whats u
```

then running `git diff` shows:

```bash
(base) ksamaarora@Ksamas-MacBook-Pro winterarc-solutions % git diff
diff --git a/Git/Part5-GitDiff.md b/Git/Part5-GitDiff.md
index 1ae36e5..2ed5613 100644
--- a/Git/Part5-GitDiff.md
+++ b/Git/Part5-GitDiff.md
@@ -1 +1 @@
-Hey whats up 
+Hey whats u
(base) ksamaarora@Ksamas-MacBook-Pro winterarc-solutions %
```

Here:

* The line starting with `---` shows the **original** version.
* The line starting with `+++` shows the **new** version.
* A **minus (-)** means content was removed.
* A **plus (+)** means new content was added.

By default, `git diff` compares the working directory with the **staging area** — showing changes that are not yet staged.

If you want to compare what’s already staged (added using `git add`) with the last commit, use:

```bash
git diff --staged
```

This shows the differences between the **staging area** and the **previous commit**.

So in short:

* `git diff` → shows unstaged changes (working directory vs staging area)
* `git diff --staged` → shows staged changes (staging area vs last commit)
