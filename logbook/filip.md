# A madmans logbook
Filip Holmgrens logbook.

## 23/09/2023
Docker, a tool most developers use. Which I have never used. So this was a first for me. And let me tell you, It was **NOT** a good experience. First of all. The CLI, I like many people don't like GUIs. They abstract a lot of the things away from the user. So I prefer using the CLI. This was not the greatest choice since almost every ███████ user uses the Docker desktop application. Anyway so I watched a bunch of tutorials and learned some basic commands like `docker build` and `docker run`. I also learnt about tagging. In the end I built a two step docker file. The first "compiles" the code. I use the term compiler loosly since it technically is an installer but I digress. The second step runs the code and that's about it. It was definetly an interesting day to say the least.

Note: I wanna use NIX

## 24/09/24
Sooooo... Docker..... Yeahhh.... I don't really want to work with it but oh well. I managed to set up a dev container today with vscode. It was easier than I thought. I also set up a basic flask server just to see if the port forwarding and python installation worked and suprisingly both worked. Hurray! I also switched from using the normal python docker file from docker hub to the `-alpine` version. This trimmed down the file size by almost a 100Mb which is nice.

## 4/10/24
I've come around and accepted docker. It isn't as bad as I thought. Just needed to sleep on it for a bit. Anyway I learned more about docker compose. It's a really nice tool. I also started work on the kitchen view. I read that it was a requirement to have a database so I added mongodb. This wasn't planned so I'm having to redesign some. Overall it was a good day.

## 6/10/24
Well... this was an interesting day. I was trying to fix a bug where my websocket connection wasn't working and I somehow ended up reading the description of the project and it turns out I missed a bit. The kitchen view only needs to print out to std out.. Well i fixed it. So thats that. I also added mongo-express. So that we have a web ui for the database. For now it's just the default credentials and I don't see us changing it in the future. Next time I'm with the group we'll fix so that the client ui fetches from the database instead of just a json file :)


## 8/10/24
Today I helped Leo finnish up the backend. We setup mongodb, out database and made use of it inside the code. Nothing more, nothing less.

## 10/10/24
Today I merged the beautiful frontend that Mikko made. We also set it up to use the database so we get the actual burgers :). Next time I'm gonna set up some tests in Postman to debug the code. 