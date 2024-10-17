
## Git commands I have used:
git clone (repository): Creates a local clone of a remote repository.
git branch (name): Creates a new branch of the current version of the project. Changes made on this branch doesn't affect the main branch. (If the command is only "git branch", it lists the existing branches)
git checkout (branch): Lets you change branch and makes it so that the branch you switch to is based on the branch you are switching from.
git fetch: Downloads commits from the remote repository to your cloned one.
git pull: Downloads fetched commits from the cloned repository to your current branch.
git add: Adds changes to a commit.
git commit: Commits the added changes to the cloned repository along with a log message describing the changes made.
git push: Pushes the committed changes from the cloned repository to the original one.
git status: Lets you see which changes have and haven't been added to a commit. You can also see if there have been changes to the main branch that you don't currently have on your branch.
git switch: Lets you switch between branches.
git diff: Compares changes, commits and/or branches in the project.
git reset: Undoes previous commits.
git log: Lists commits in reverse chronological order (most recent first)
git restore: Discards any uncommitted changes, basically restoring the last commited state.
git stash: Saves uncommitted changes for later use.


## Date: 2024-09-24
Today I have started with the API for the BurgerOrderer project. First of all i cloned the project-repository and made my own branch. Thereafter I got Filip's help to install and learn how Postman works. After playing around with Postman I started working on the menu and coming up with names for burgers and what specials you could add/remove. I wrote these in a json file. I also made some basic functions that I used to test if you could retrieve the list of burgers and the list of specials from the json file through Postman.
git commands used: git clone, git branch, git checkout, git push

## Date: 2024-09-26
Today I finished writing the different burgers and specials in the json file. Along the way I used Postman to test that you could retrieve the list from the json file.
git commands used: git fetch, 

## Date: 2024-10-04
Today I commited all my changes so that Filip could start merging the frontend and the backend.
git commands used: git diff, git commit, git push, 

## Date: 2024-10-08
With a lot of help from Filip, I today set up MongoBD and changed (and furthered) the code so that it used the database instead of the json file. 
git commands used: git switch, git commit

## Date: 2024-10-16
Today I wrote docstrings for the functions in the burger_orderer container. I messed something up when trying to push my commit so Filip helped me restore my branch.
git commands used: git add, git commit, git push, git reset, git branch, git log, git restore

## Date: 2024-10-17
Today I updated the docstrings in the burger_orderer container, so they are now structured a lot better. I also tried debugging the main file in the kitchen_view container. I placed a breakpoint at the start of the handle_new_order function, so that I could follow the code from the start. I basically only use the step over button because there are only one statement per line, so I can't really step into the code. The first interesting thing I can see is where/when the order variable gets its values, such as the name of the burger and its requested specials. I can see this in the variables window in the top left when debugging. Next it goes through an if-statement that checked for multiple faults in the order variable and when I deliberately made the order faulty, I could see where/when it detected the fault and what happened after that. In this case the consequence of the if-statement was to print an error message. After that came a for-loop that checked if the specials were valid (basically if they are strings). I also deliberately tested what would happen if I used an invalid special and it resulted in an error message. Thereafter the print_order function is called with the order variable as the argument. It finally goes through multiple rows of printing the information that the kitchen sees, such as the name of the burger and the different specials.
git commands used: git fetch, git stash, git pull, git add, git commit, git push, git status
