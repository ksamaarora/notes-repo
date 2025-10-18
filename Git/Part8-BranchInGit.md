Part 8 Git Branch 

What is branching?

Either create a branch from github directly or do using command line 

This works when u already have a branch called branchname
git checkout branchname 
OR
git switch branchname

But what if u waant to create one and switch ?
git checkout -b branchname

use gitbranch to check available branches 

* feature1
main 

* shows the current branch 

Whatever changes u do will be hapeeninf in the current branch

now if u make changes do git add and git commit 
Say u swicth to main branch, it would have no idea of those changes 
Only feature branch knows it 

Now if u do git log 
You will see the last commit with Head->feature
and second last commit origin/main, main

Now say you want to delete a branch 

git branch shows all branches 

If you want to move to the previous branch you came from use git branch - (shortcut)

git branch -d branchname 
In order to delete a branch 

To push a remote branch, use git push origin branchname

How branching works??

Whenever you do any commits, you do in a specific branch. By default it is the master branch, but we for say create main and test branches
Default for us is main branch

Everytime we do a commit, git takes a snapshot of your files and gives it a commit number checksum .
There is also a pointer 
So say u have 3 snapshots snapshot 1, 2, 3 with 3 being the latest

at snapshot 3 the head points to main which points to snapshot 3 

The head points to the branch u are currently in 

Say u create a new branch and u are in the new branch. It would point to snapshot 3 and the head pointing to the new branch 

Say u make some changes and push in the new branch, then a new snapshot would be created snapshot 4 with new branch pointing to updated snapshot and head pointing to it but the main points to the earlier snapshot only

