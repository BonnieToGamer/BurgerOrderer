# Engineering journal - Mikko Onttonen - (MiOn21)

## Week 1
We created a group of three people for this project.
The group decided on what different tools and environments to use and what tasks each and one of us should focus on to make our product as high-quality and efficient as possible.
For the code environment we decided to use Visual studio Code. In this project we will use Python, HTML, CSS, JavaScript and JSON. The framework we decided to use is Flask.
The git-server we decided to use for our project is Github. 
To make the configuration management easier, each of us created a branch of our own to start working on.
I used "git branch ui-design" to create the branch "ui-design" branch locally, and started to make a plan on how the UI should look and what the functionality would be.
To push the branch up to the git-server, I created a useless file with "touch nothing.html" this created a useless html file that I could commit and push. I used "git switch ui-design" to ensure that I am in the correct branch and then used the commands "git add .", "git commit -m "Nothing" " and "git push". This staged the file to be committed and committed it with the message "Nothing", and pushed it to the remote branch "ui-design".

## Week 2
I started out with making a sketch of the UI. I drew inspiration from different restaurant UI's and websites and tried to design something that would be user-friendly and clean.
After creating the sketch I asked my group if the sketch needed anything changed or added to it. 
One thing with the sketch that I did not take in to account when creating it, was the creation of the layout. To create the exact same layout in HTML, CSS and javascript might be too hard to make.

## Week 3
After getting the feedback about the layout design, I started trying to create the UI with HTML, CSS and JavaScript.
I made a new folder and created multiple files, two python files with flask that created the local web application so I could be able to see the UI.
For the UI design and functionality I created a HTML file and a CSS file. I added all the images that I used in the sketch to the project and started out trying to implement them into the web application using HTML and CSS. I looked up how to add images and text to the UI using HTML. 

## Week 4
I created the base UI layout. The layout consists of the logo, navigation bar, the burgers and the background. I implemented these with HTML and CSS. 
I did not have any prior experience with these programming languages and had to search the web for tutorials to be able to learn how to use them.
One of the few inconveniences I stumbled upon was the creation of the grid layout. The burger layout I had planned on using was a bit too complicated to create and decided to use a more simple layout for the burgers.

## Week 5
I implemented burger selection for the UI, so when a burger is clicked it becomes bigger and gets moved to the right side of the screen. I used JavaScript and CSS to implement the movement and action that occurs when a burger is clicked. 
I started making the layout for the specials selection screen using HTML, CSS and JavaScript. 
HTML and CSS to create the look and functionality of the specials selection and JavaScript to make the specials show up when the burger is clicked.

JavaScript is also used to record when a burger was selected and what special requests was given. This data will be saved as JSON data and will be able to be used by the backend.
Finalized the UI design and functionality and pushed it to the remote branch "ui-design"

## Week 6
Now that the projects branches has been merged into the main file, I started to use docker to be sure that the I had the requirements needed to run the project correctly. 
I added docstrings that explains the parameters and the functionality of the methods in kitchen_view. 
After documenting the functionality of the methods in kitchen_view I started a debug session. 

### The Debug session
I chose to check what happens if I put a breakpoint in the get_specials method from the main.py file in the burger_orderer container. The variable that the breakpoint was set on was "burger_name = request.args.get("burger", default = "", type = str)" this made it so that when a burger was clicked, the burger name does not get sent to the kitchen_view and prevents any specials to appear for selection, this happens because the breakpoint makes the debugger pause execution right before the value of the 'burger' parameter gets extracted from the request. The breakpoint makes it possible to view the incoming request object and allows me to see if the correct value is assigned to the burger_name variable.
To test if the correct name was assigned to the burger_name variable I looked under the "Globals" variables tab, went down to the request tab and then to the args tab. Under the args tab you can see that the correct value has been passed as the 'burger' parameter which will result in assigning the correct value to burger_name. I confirmed this by using the step over button, basically stepping to the next line of code, allowing the burger_name value to get assigned with the correct value. You can see this by checking the "Locals" tab and viewing the variable burger_name = 'Cheeseburger'.
I also checked what happens if you change the value of the burger_name variable to a different valid name. I changed burger_name = 'Cheeseburger' to burger_name = 'Burger 20'. By doing this the specials for the Burger 20 gets retrieved instead of the Cheesburger specials. This does not change the burger selection, only the specials. Placing the order with the different specials selections does not cause any errors. 

The other buttons that can be used for debugging are continue, step into and step out. The continue button does at it says and runs the code after being paused at the breakpoint. The step into button can be used to step into functions and methods that are on the line and allows debugging inside the function or method. The step out is used to step out of a function or a method and runs the rest of the code inside of the function or method and pauses once it returns to the place it was called from.

### Conclusions from the debugging session
Carrying out the debugging session was a learning experience and was a bit complicated to understand in the beginning. But once I tested out the different buttons and setting different breakpoints in the code, it was less complicated than what I assumed. The things that was hard for me to understand in the beginning was the breakpoints, I did not get if the breakpoint completely "removed" the line of code it was set on or if the line of code it was set on was the last line it ran. But after using it I understand that it is kind of a middle ground to that, it stops the execution on that line and makes it possible to view what the different variables values are and how the program state in that moment looks like, allowing you to have a step by step approach to debugging.  
I found this very useful as I can see how this could be used for when an error occur, instead of using prints to check every variable etc.

 





