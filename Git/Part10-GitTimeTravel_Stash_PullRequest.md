Part 10 

> Git Time tarvel 

Say u want to move to some previous commit 

So what i do is first i create a new branch say liteversion 
git checkout -b lite-version

git checkout 00bb7c88f1c6fb551fd495b4682e82b9c374cd01
Note: switching to '00bb7c88f1c6fb551fd495b4682e82b9c374cd01'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 00bb7c8 Resolved merge conflict in Part8-BranchInGit.md

> Git Stash 

What is git stash?

Say i am in the feature branch and we are building some ai feature. Since it is not ready i dont want to do any commit as its not complete . 
Say my manager comes in and says there is some error in the main branch 
Say if we shift directky to main branch, it would show error - local changes would be overwritten by checkot so pls commit changes or stash them 

We would atash and save those changes so next time we come back to the branch, we can come back with this 

git stash 

and now move to the main branch 

Example 
(base) ksamaarora@Ksamas-MacBook-Pro winterarc-solutions % git branch
  lite-version
* main
  test
(base) ksamaarora@Ksamas-MacBook-Pro winterarc-solutions % git switch test
error: Your local changes to the following files would be overwritten by checkout:
        Git/Part10-GitTimeTravel_Stash_PullRequest.md
Please commit your changes or stash them before you switch branches.
Aborting
(base) ksamaarora@Ksamas-MacBook-Pro winterarc-solutions % git stash
Saved working directory and index state WIP on main: 221f442 changes added
(base) ksamaarora@Ksamas-MacBook-Pro winterarc-solutions % git branch
  lite-version
* main
  test
(base) ksamaarora@Ksamas-MacBook-Pro winterarc-solutions % git stash apply
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   Git/Part10-GitTimeTravel_Stash_PullRequest.md

no changes added to commit (use "git add" and/or "git commit -a")
(base) ksamaarora@Ksamas-MacBook-Pro winterarc-solutions % 




