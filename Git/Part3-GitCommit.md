## Part 3 – Git Commit

When you make any changes in your project, those modifications exist only in your **working directory**. Git doesn’t track them automatically until you explicitly add them to the **staging area**.

The **staging area** (also called the *index*) is like a waiting room — it holds the exact versions of files that you want to include in your next commit. You can stage some files and leave others out, giving you control over what changes get recorded together.

To move a file from the working directory to the staging area, you use:

```bash
git add <filename>
```

Once added, Git marks that file as staged. If you run `git status`, you might see output like this:

```bash
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   Git/Part3.md

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   Git/Part3.md
```

This means you’re currently on the **main branch**, your branch is synced with the remote (`origin/main`), and the new file `Git/Part3.md` has been staged — ready to be saved in the next commit.

If you decide not to keep it staged, you can unstage it using:

```bash
git rm --cached <filename>
```

Once you’re satisfied with what’s staged, you record it permanently in the local repository using:

```bash
git commit -m "your message"
```

After the commit, you can view your project’s history with:

```bash
git log
```

A typical log entry looks like this:

```bash
commit a3f9c2e1b4a1d4b58e7d9b9c2eab27dfb0a1a234 (HEAD -> main)
Author: Ksama Arora <ksama2004.arora@gmail.com>
Date:   Fri Oct 17 09:22:47 2025 +0530

    Added Git commit section notes
```

Each commit has a unique **checksum** generated using **SHA-1**, a 40-character hexadecimal string (only the first 7 characters are usually shown). Even a one-character change in your code will produce a completely different checksum, ensuring data integrity.

Here, `HEAD -> main` means the **HEAD pointer** (which represents your current working state) is pointing to the **latest commit** on the **main branch**.
