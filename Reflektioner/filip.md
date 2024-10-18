# Engineering journal - Filip Holmgren - (fihl24)
Filip Holmgrens logbook.

## Git commands I've used:
<code>git fetch</code> fetches the origin but doesn't add it to the tree </br>
<code>git pull</code> pulls the origin and adds it to the working tree </br>
<code>git add</code> add's files to the current stash </br>
<code>git commit</code> commit's the current stash </br>
<code>git push</code> pushes the local commits to the origin </br>
<code>git merge</code> merges two branches together </br>
<code>git status</code> get's the current status of the git project
<code>git switch</code> create and or switch to new branch </br>
<code>git branch</code> list all git branches </br>

## 23/09/2023
Docker, a tool most developers use. Which I have never used. So this was a first for me. I prefer using the CLI, because GUIs abstract a lot of functionality away. This was not the greatest choice since almost every user uses the Docker desktop application. So I started watching a bunch of tutorials and learned some basic commands like `docker build` and `docker run`. I also learnt about tagging. In the end I built a two step docker file. The first "compiles" the code. I use the term compiler loosely since it technically is an installer but I digress. The second step runs the code and that's about it. It was definitely an interesting day to say the least. Git commands used <code>git fetch</code> <code>git pull</code> <code>git add</code> <code>git commit</code> <code>git push</code> <code>git branch</code><code>git switch</code>

## 24/09/24
Today I managed to set up a dev container today with vscode. It was easier than I thought. I also set up a basic flask server just to see if the port forwarding and python installation worked and surprisingly both worked. Hurray! I also switched from using the normal python docker file from docker hub to the `-alpine` version. This trimmed down the file size by almost a 100Mb which is nice. Git commands used <code>git fetch</code> <code>git pull</code> <code>git add</code> <code>git commit</code> <code>git push</code>

## 4/10/24
Today I learned more about docker compose. I also started work on the kitchen view. I read that it was a requirement to have a database so I added mongodb. This wasn't planned so I'm having to redesign some. Git commands used <code>git fetch</code> <code>git pull</code> <code>git add</code> <code>git commit</code> <code>git push</code>

## 6/10/24
I was trying to fix a bug where my websocket connection wasn't working and I somehow ended up reading the description of the project and it turns out I missed a bit. The kitchen view only needs This will kentials and I don't see us changing it in the future. Next time I'm with the group we'll fix so that the client ui fetches from the database instead of just a json file :). Git commands used <code>git fetch</code> <code>git pull</code> <code>git add</code> <code>git commit</code> <code>git push</code>

## 8/10/24
Today I helped Leo finnish up the backend. We setup mongodb, out database and made use of it inside the code. Nothing more, nothing less. Git commands used <code>git fetch</code> <code>git pull</code> <code>git add</code> <code>git commit</code> <code>git push</code>

## 10/10/24
Today I merged the beautiful frontend that Mikko made. We also set it up to use the database so we get the actual burgers :). Next time I'm gonna set up some tests in Postman to debug the code. Git commands used <code>git fetch</code> <code>git pull</code> <code>git add</code> <code>git commit</code> <code>git push</code>

## 15/10/24
Today I started work on the unit tests. I sent the rest of the group to write documentation for all the functions. I also learned a lot more about docker. We decided on using pytest as the testing framework. It is one one of the simplest and greatest testing frameworks for python. Also, turns out monorepos don't work with dev containers :D. That was a fun learning moment. Git commands used <code>git fetch</code> <code>git pull</code><code>git add</code> <code>git commit</code> <code>git push</code>

## 16/10/24
I finished all the unit tests that we planned for. I also set up a Makefile for easier usage of the project. Git commands used <code>git fetch</code> <code>git pull</code> <code>git add</code> <code>git commit</code> <code>git push</code> <code>git merge</code> 

## 14/10/24
Debug session:
1. I choose to test the get_specials() method.
2. I find the file in Containers/burger_orderer/main.py and set my breakpoints on line 65 (at the time of writing).
3. The main buttons when debugging are as follows:
    * Continue: This continues executing the program until a breakpoint is hit.
    * Step over: This goes to next line in the same source file. If that isn't possible it steps out of the function.
    * Step into: If the current line calls a function, it goes into that function and stops at the first line.
    * Step out: This steps out of the current function.
    * Stop: Stops the program out right and quits debugging.
    * Restart: Restarts the program and debugging session.
    * Pause: Pauses the program at whichever line it is currently at.
4. I can inspect a variable in VSCode by simply hovering over it when paused at a breakpoint that has access to that variables scope, e.g. same function. But I can also look in the inspection menu to see all local scope variables and global scope variables. In this case when breaking on line 64 which is a variable declaration the variable `burger_name` will get the value of the URL parameter `burger`. In my case it was "Cheeseburger". I can also set up the variable to break on change, simply by right clicking on the variable in the inspector and selection "break on value change".
5. By breaking halfway through a GET request the client would simply not get a response from the server. This would break the client UI, while this isn't intended it is programmed that way. I repeated the request multiple time to tweak certain things during runtime, e.g. I changed the variable burger_name before the database request so that I got a different burger than I requested for, it was very easy to do so and I had no problems during my debugging session. Debugging is an extremely useful tool. It has helped me in the past fix so many problems. It is very helpful to see what values variables have and change them at runtime at will.