## Part 1 – Intro

Git is a **distributed version control system (DVCS)** used to track and manage changes in code.

In a **local version control system**, a developer maintains a local copy of files along with a small database that stores the version history. This works fine for personal projects but is not ideal for collaboration since everything stays on one system.

A **centralized version control system (CVCS)** uses a single central server that holds the main repository, while developers work on local copies. When they commit, the changes are pushed to the central server and become visible to everyone. However, if the server goes down, the entire version history and access are lost — which is a major drawback.

That’s where **Git** comes in. Being a **distributed version control system**, Git allows every developer to have a complete local copy of the repository, including its entire history. This means anyone can restore the full project even if the central server fails. Git is simple to use, fast, supports branching and merging, and enables true collaboration. “Fully distributed” means there is no single point of failure — every user’s local machine acts as both a client and a full backup of the repository.

To set up Git, first download it from [git-scm.com/downloads](https://git-scm.com/downloads). Then configure your username and email once using the following commands:

```bash
git config --global user.name "yourname"
git config --global user.email "youremail"
```