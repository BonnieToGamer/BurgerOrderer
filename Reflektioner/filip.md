# A madmans logbook
Filip Holmgrens logbook.

## 23/09/2023
Docker, a tool most developers use. Which I have never used. So this was a first for me. And let me tell you, It was **NOT** a good experience. First of all. The CLI, I like many people don't like GUIs. They abstract a lot of the things away from the user. So I prefer using the CLI. This was not the greatest choice since almost every user uses the Docker desktop application. So I started watching a bunch of tutorials and learned some basic commands like `docker build` and `docker run`. I also learnt about tagging. In the end I built a two step docker file. The first "compiles" the code. I use the term compiler loosely since it technically is an installer but I digress. The second step runs the code and that's about it. It was definitely an interesting day to say the least.

## 24/09/24
Today I managed to set up a dev container today with vscode. It was easier than I thought. I also set up a basic flask server just to see if the port forwarding and python installation worked and surprisingly both worked. Hurray! I also switched from using the normal python docker file from docker hub to the `-alpine` version. This trimmed down the file size by almost a 100Mb which is nice.

## 4/10/24
Today I learned more about docker compose. I also started work on the kitchen view. I read that it was a requirement to have a database so I added mongodb. This wasn't planned so I'm having to redesign some.

## 6/10/24
I was trying to fix a bug where my websocket connection wasn't working and I somehow ended up reading the description of the project and it turns out I missed a bit. The kitchen view only needs to print out to std out.. Well i fixed it. So thats that. I also added mongo-express. So that we have a web ui for the database. For now it's just the default credentials and I don't see us changing it in the future. Next time I'm with the group we'll fix so that the client ui fetches from the database instead of just a json file :)

## 8/10/24
Today I helped Leo finnish up the backend. We setup mongodb, out database and made use of it inside the code. Nothing more, nothing less.

## 10/10/24
Today I merged the beautiful frontend that Mikko made. We also set it up to use the database so we get the actual burgers :). Next time I'm gonna set up some tests in Postman to debug the code. 

## 15/10/24
Today I started work on the unit tests. I sent the rest of the group to write documentation for all the functions. I also learned a lot more about docker. We decided on using pytest as the testing framework. It is one one of the simplest and greatest testing frameworks for python. Also, turns out monorepos don't work with dev containers :D. That was a fun learning moment.

## 16/10/24
I finished all the unit tests that we planned for. I also set up a Makefile for easier usage of the project.