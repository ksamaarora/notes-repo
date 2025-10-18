Part 9 

> Git Merge 

Say i want to merge the changes done in feature branch to main branch 
How will we do that?

Be in the main branch 
and do git merge branchname i.e. git merge feature 

Sometime u would get merge conflicts 
We will see about that later 

git pull origin main -> always do before merging if u are wokrign with collaborators and then do mergung 
after that do git push

> Merge Conflicts  

Why would u get merge conflicts?

Say u are working on the main branch and your friend works onf eature branch

both have made changes and now u want to merge them into main - u will have merge conflicts 

u are in main and u try to merge feature branch changes 
git merge feature 

u will get merge conflicts 
how to fix that now?

u can check the difference using git diff feature 
it will show what changes u have made 

<<<<<HEAD current chane 
change 2 in my database 

change in harsh database
>>>>>>> feature  (Incoming change from other branch )

So do the changes and commit the changes 