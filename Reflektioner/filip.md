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


## 23/09/2023
Docker, a tool most developers use. Which I have never used. So this was a first for me. I prefer using the CLI, because GUIs abstract a lot of functionality away. This was not the greatest choice since almost every user uses the Docker desktop application. So I started watching a bunch of tutorials and learned some basic commands like `docker build` and `docker run`. I also learnt about tagging. In the end I built a two step docker file. The first "compiles" the code. I use the term compiler loosely since it technically is an installer but I digress. The second step runs the code and that's about it. It was definitely an interesting day to say the least. Git commands used <code>git fetch</code> <code>git pull</code> <code>git add</code> <code>git commit</code> <code>git push</code>

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