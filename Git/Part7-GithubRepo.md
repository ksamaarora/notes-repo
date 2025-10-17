## Part 7 – GitHub Repository

To publish your local project on GitHub, first create a **new repository** on GitHub. It will give you a **unique link** — either HTTPS or SSH — that you’ll use to connect your local repository with the remote one.

Now you have two things: a **local repository** on your system and an **empty remote repository** on GitHub.

Open the terminal, create a new folder, and navigate into it:

```bash
mkdir myproject
cd myproject
```

To create a simple file in it (for example, a README), use:

```bash
echo "# My First Repo" > README.md
```

You can view its content with:

```bash
cat README.md
```

Next, initialize Git in this folder:

```bash
git init
```

This creates an empty Git repository.

* `ls` → shows visible files like `README.md`.
* `ls -a` → shows hidden items too, including the `.git` folder which Git creates internally.

If you run `git status`, it will show `README.md` as **untracked** — meaning it’s not yet staged for commit.
To stage it:

```bash
git add README.md
```

Then commit it:

```bash
git commit -m "Initial commit"
```

This saves your changes in the **local repository**.

By default, Git creates a branch named **master**, but we now use **main** as the standard branch name. To rename your branch:

```bash
git branch -M main
```

Next, connect your **local repository** to the **GitHub remote repository** using the link you copied:

```bash
git remote add origin https://github.com/username/repo-name.git
```

(You can use either the **HTTPS** or **SSH** link.)

Finally, push your local commits to GitHub:

```bash
git push -u origin main
```

Here, `-u` sets the **upstream**, which means your local `main` branch will stay linked with the remote `main` branch for future pushes and pulls.
