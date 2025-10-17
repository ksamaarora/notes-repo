## Part 2 – Git Init

Git works with three main areas — the **working directory**, the **staging area**, and the **repository**. The working directory is where you create and modify files. Once you’re ready to save changes, you move them to the staging area, which acts as a middle space before committing. When you commit, the changes are permanently recorded in the repository as part of the commit history.

The files you create in your local folder are part of the **local repository**. If you want to share or collaborate on them, you connect your project to a **remote repository** (like GitHub or GitLab).

To check if Git is installed, use:

```bash
git --version
```

To start tracking a project with Git, initialize a new repository using:

```bash
git init
```

This command creates an empty Git repository in the current directory.

By default, Git initializes the repository on a branch named **master**. However, the convention now is to use **main** as the default branch. To do this directly while initializing, run:

```bash
git init -b main
```
