## Part 4 – Skipping the Staging Area

![Git Workflow](https://github.com/user-attachments/assets/d1bdab7b-eb0c-43c5-b9e1-a908179fcaf4)

* The diagram represents the **flow of files in Git** — from your local workspace to the remote repository.
* The **Working Directory** is where you create or edit files.
* The **Staging Area** temporarily holds the files you want to include in your next commit.
* The **Local Repository** is where committed versions are stored permanently on your machine.
* The **Remote Repository** (like GitHub) holds the shared version that others can access.
* `git add` → moves changes from Working Directory → Staging Area.
* `git commit` → saves staged changes from Staging Area → Local Repository.
* `git push` → sends commits from Local Repository → Remote Repository.
* `git pull` → fetches updates from Remote Repository → merges into Local.
* `git fetch` → only downloads updates from Remote without merging.
* `git stash` → temporarily saves unfinished changes so you can switch branches safely.
* `git stash apply` / `git stash pop` → restores those saved changes later.

---

After committing your changes, if you edit a file again and run `git status`, Git will show:

```
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
        modified:   example.java
```

This means the file is in the **modified** state — changes exist in the **working directory**, but they haven’t been staged yet.

Every file you create or edit first lives in the **working directory**. When you run `git add`, it moves into the **staging area**, and when you run `git commit`, it becomes part of the **local repository** (saved in the commit history).

In the Git workflow diagram, this flow is shown clearly:

* `git add` moves files from **Working Directory → Staging Area**
* `git commit` moves files from **Staging Area → Local Repository**
* `git push` then sends your commits from **Local Repository → Remote Repository**

When you see an **M** next to a filename in `git status`, it indicates that the file has been **modified** but not yet staged.

Now, if you want to **skip the staging area** and directly commit your changes, Git allows you to do that using the `-a` flag:

```bash
git commit -a -m "your message"
```

Here, the `-a` option tells Git to automatically stage all **modified and tracked files** before committing them. It skips the manual `git add` step and directly moves the changes from the **working directory** to the **local repository**.

However, note that `git commit -a` only affects files that Git is already tracking. New, untracked files still need to be added once using `git add` before this shortcut can work.

So, in short:

* `git add` → moves files to staging area
* `git commit` → saves staged files to repository
* `git commit -a -m "msg"` → skips staging and commits modified tracked files directly
