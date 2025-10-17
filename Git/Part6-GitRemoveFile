## Part 6 – Git Remove File

When you have multiple files to add, you can stage them all at once using:

```bash
git add .
```

and then commit them together with:

```bash
git commit -m "your message"
```

Now, if you want to **remove a file**, deleting it directly from VS Code only removes it from your **working directory**, not from Git’s tracking system. Git still remembers that file from previous commits.

To remove the file from Git’s tracking as well, use:

```bash
git rm --cached yourfilename.txt
```

This command untracks the file while keeping it in your local directory. If you then delete it from VS Code afterward, it will also be removed from Git completely in the next commit.

Sometimes, when you delete a file in VS Code, Git automatically recognizes it as deleted and stages that change. This usually happens because your VS Code is **integrated with Git** (and possibly connected to GitHub). VS Code automatically detects file changes in the working directory and updates Git’s state accordingly.

In short:

* Deleting from VS Code → removes from working directory only.
* `git rm --cached <file>` → untracks it from Git.
* If VS Code auto-stages deletions, it’s because of its built-in **Git integration** or **GitHub sync**.
