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


