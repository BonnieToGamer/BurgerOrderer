# Grupp 20 Reflektioner - Filip, Leo and Mikko  

## Link to the project:
https://github.com/BonnieToGamer/BurgerOrderer

## Configuration management and collaboration
The group decided on the different tools and environments we should use for this project.
We also decided on what tasks each and one of us will be doing. 

### Configuration management
Configuration management is the process of keeping track of and control changes to software and its different components, such as the documentation, code and system settings. By having good configuration management, it will ensure that everyone in the group uses the correct versions of the components used in the project.

### Git and Github
To have control over the source code and configuration files we decided to use git and github. Git and Github allows us to collaborate and work on the project simultaneously through the use of branching. We created a branch for the UI/frontend and a branch for the backend using the command "git branch "branchname" " for each branch. By using branches we can work on different tasks and not worry about creating issues to the main branch. 
Git and Github also allows us to keep track of the commit history and makes it possible to see the changes made in the project. If any issues occur after a commit has been made, git allows us to go back to previous configurations if needed.

The most used git-commands are "git branch ", "git status","git add ", "git commit -m "message" "

### Docker
To keep consistency across different environments we decided to use docker. 
Docker will be used to package the application with all of the dependencies, libraries and configurations into a container. 
By doing this it will ensure that the project will work regardless of what environment we use.

### Group experiences of configuration management
The things that went well with the configuration management was the creation of the new repository and branches for the project. 
The things that went less well with configuration management was setting up the correct git client in the terminal for ease of use. If we only used git to push a new commit we had to use authentication tokens and or log in to github each time. But by using Github CLI we could authenticate our accounts and made it possible to push a commit to a remote branch without logging in each time. Filip ended up switching to SSH keys since it disrupted his workflow since Github's CLI was broken on his end.

We also encountered an issue where in the early stages we started making our own branches. We ended up making different ways of working and when the time came to merge it was near impossible since the files were structured in different ways. Filip sat down and manually merged every file by simply copy pasting. While this is the wrong way to do it. He felt it necessary to do so.
