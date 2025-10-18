Part 10 Git Time tarvel 

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


