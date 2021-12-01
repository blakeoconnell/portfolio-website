project_data = [
    {
        "id": 0,
        "title": "JedBot",
        "short_desc": "A Discord.js bot built as an integration between Discord and Discourse forums. Also assigns roles via emojis.",
        "long_desc": "This project is a Discord bot built for an online gaming community of over 1500 members. This community uses an "
                     "implementation of Discourse forums and requires users who wish to join the community to register "
                     "on the forums before being granted full access to the Discord server. Manually, when a user joins "
                     "the Discord server after registering on the forums, an admin must check the logs to verify this new "
                     "user is who they say they are. With the bot, this is done seamlessly with no action needed from "
                     "the community admins. The new user instead provides their forum username to the bot, and the bot "
                     "calls the Discourse API to verify that the Discord name of the user who joined the server matches "
                     "the Discord name of the account registered on the forums. If so, the bot grants the new user "
                     "full access to the Discord server. Additionally, the bot is set up to grant roles pertaining to "
                     "specific games based on emoji reactions by users. Click an emoji, bot gives the role pertaining to"
                     " that emoji.",
        "imgURL": "assets/jedbot-roles.png",
        "carouselImages": ["assets/jedbot-roles.png", "assets/jedbot-auth.png"],
        "githubURL": "https://github.com/blakeoconnell/JedBot",
        "technologies": ["JavaScript", "App Integration via Web APIs", "Version Control", "Client Communication"],
        "learnings": "This project was a lot of fun. As a member of this community, I saw a problem with how inefficient "
                     "their system of granting access to new users was, and offered to fix the problem. This made the "
                     "project somewhat unique compared to my others up to this point, as previously I built things for "
                     "myself and I made all the specifications for myself. That was not the case with this, as I was "
                     "building this for a large community and they had very specific requirements I had to follow. "
                     "I learned more from this project than any other, as JavaScript was something I'd only ever used "
                     "for front-end web apps and I never got into the more intricate things like working with APIs and "
                     "data structures. I spent a great deal of time reading documentation for JavaScript, Discourse and "
                     "Discord.js, the library for building Discord bots with JavaScript. Learning how to build an "
                     "integration between two applications was invaluable to my progression as a software developer. "
                     "Aside from getting more comfortable with referencing documentation, I think the biggest takeaway "
                     "from this project was learning how to host an application that is always running, as well as "
                     "providing support for when the community asks for changes. This got me to learn version control "
                     "with GitHub very quickly, as I made more and more commits for each and every change I made. This "
                     "bot is still hard at work every single day for the Evolved Gaming Community."

    },
    {
        "id": 1,
        "title": "Breakout Game",
        "short_desc": "A recreation of the classic arcade game Breakout using Python and the Turtle Module.",
        "long_desc": "Breakout is an arcade game developed and published by Atari in 1976. The goal of the game "
                     "is to break all the blocks by repeatedly bouncing a ball off a paddle into them. "
                     "What you see here is my recreation of the game using Python and the built-in Turtle Module. ",
        "imgURL": "assets/breakout_image_square.png",
        "carouselImages": ["assets/breakout_image.PNG"],
        "githubURL": "https://github.com/blakeoconnell/turtle-breakout-game",
        "technologies": ["Python", "turtle.py", "Object-Oriented Programming"],
        "learnings": "This project was more of a challenge than I first anticipated. The biggest challenge I faced was "
                     "programming the interaction between the ball and the bricks, and giving the ball a realistic "
                     "bounce angle based on which side of the brick it made contact with. I learned a lot about "
                     "coordinates and constantly updating the graphics to make the gameplay look fluid. Perhaps the "
                     "most useful practice I got with this project was that of OOP. The ball, paddle, and all of the "
                     "bricks are objects. Programming in this way is absolutely invaluable considering the number "
                     "of bricks needed to be placed. Creating objects prevented the necessity to repeat a ton of "
                     "code throughout the whole project."

    },
    {
        "id": 2,
        "title": "Dummy Blog",
        "short_desc": "A dummy blog built with Flask utilizing a relational database to hold users, blog posts and comments.",
        "long_desc": "This project is a blog which allows the admin user to create/delete posts, as well as any non-admin "
                     "user to comment on posts. The frontend was created using an HTML template as a starting point. "
                     "The backend is built with Flask. Sqlite3 was used during development for the database, and Postgres "
                     "was used once I moved to 'prod' to bring it online. This blog also features a contact page, which "
                     "when filled out will generate and send an email to me with their contact information and message.",
        "imgURL": "assets/dummy-blog.png",
        "carouselImages": ["assets/dummy-blog.png"],
        "githubURL": "https://github.com/blakeoconnell/dummy-blog",
        "technologies": ["Python", "Flask", "Relational Database", "Jinja Templates", "Login Manager", "WTForms"],
        "learnings": "I learned a great deal from this project in regards to databases and how websites manage logins. "
                     "Before this, 'Relational Database' to me was just a keyword I didn't fully understand. But, "
                     "having connected blog posts to comments, users to comments it really started to click for me. "
                     "Using the flask_login module it was deceptively easy to manage both logins and determining if "
                     "the logged in user was an admin. The other feature of this blog is a contact form. Not the most "
                     "impressive thing in the world, but I learned how to incorporate WTForms with Flask to create a "
                     "form that allows users to fill out a contact form that sends me an email with their message. "
                     "Overall, I had a ton of fun with this project and it opened up a lot of ideas "
                     "in my mind on future projects I would like to implement using a database and managing users. "

    },
    {
        "id": 3,
        "title": "Typing Test",
        "short_desc": "A simple typing test to measure words per minute when typing a list of random words.",
        "long_desc": "This project gives users an option to select 30, 50 or 100 randomly generated words to test "
                     "themselves on. The words are displayed in the top portion of the GUI and the user is prompted "
                     "to type in the bottom portion, copying the words they see above. As words are typed, the program "
                     "calculates how many words per minute the user has accurately typed.",
        "imgURL": "assets/type-test-square.png",
        "carouselImages": ["assets/typing-test-begin.png", "assets/typing-test-end.png"],
        "githubURL": "https://github.com/blakeoconnell/typing-test",
        "technologies": ["Python", "tkinter"],
        "learnings": "With this project, I think the biggest challenge I faced was managing the limitations of the "
                     "tkinter module. A feature I wanted to include was adding markup to the words as they were "
                     "completed by the user to indicate both where they were in the list and if they typed the word "
                     "accurately. Unfortunately, after hours of reading documentation, StackOverflow browsing and "
                     "Google perusing, it was clear that what I wanted to do was simply not possible with tkinter. "
                     "This was disappointing, but nonetheless I completed what I could and although it's not the "
                     "prettiest thing, it gets the job done and gives me an opportunity to redo this project down the "
                     "road using other tools to make it exactly what I want."

    },
    {
        "id": 4,
        "title": "Space Invaders",
        "short_desc": "A clone of the classic arcade game, Space Invaders. Developed in Python using the Turtle Module.",
        "long_desc": "Space Invaders is an arcade game first released in 1978. Space Invaders was the first "
                     "'fixed shooter' and inspired many popular games thereafter. The goal is to defeat waves of enemy "
                     "aliens to earn as many points as possible. "
                     "What you see here is my recreation of the game using Python and the built-in Turtle Module. ",
        "imgURL": "assets/space-invaders-square.png",
        "carouselImages": ["assets/space-invaders-lg.png"],
        "githubURL": "https://github.com/blakeoconnell/SpaceInvadersClone",
        "technologies": ["Python", "turtle.py", "Object-Oriented Programming", "Sounds", "Multithreading"],
        "learnings": "I spent more time on this project than others up to this point. The biggest thing I learned from "
                     "this project was how important planning and design is. I spent a good amount of time drawing up "
                     "a UML diagram beforehand, planning out all the classes, functions, features, etc. I wanted to "
                     "include in the game. The performance of the turtle module was a challenge I had to tackle. "
                     "Having each enemy ship, the player ship, each missile, the bonus ship, and all of the defenses "
                     "as their own objects seemed to hinder the performance of the game a great deal that I did not "
                     "anticipate, and so I spent some time working out how best to optimize the game loop so it could "
                     "run as efficiently as possible. I also worked with sounds for the first time while creating this "
                     "game. I noticed that playing a sound on the same thread as the main game would halt everything "
                     "until the sound effect finished, and that was obviously a huge problem. With that, I had to "
                     "implement multithreading so the sound effects could play on a separate thread and the game could "
                     "continue to run without delay. Finally. the limitation of the turtle module prevented me from "
                     "implementing one feature I wanted to recreate from the original game: visual effects. This "
                     "would have included both the enemy ship animations and all explosion animations. I learned that "
                     "turtle can not play animations, so I had to scrap this feature entirely. Overall, despite the "
                     "limitations of the module, I'm pleased with the results!"

    },
    {
        "id": 5,
        "title": "Spotify Wayback Machine",
        "short_desc": "An application that will generate a playlist of the top 100 songs from any given day by the user.",
        "long_desc": "This application utilizes web scraping the Billboard Top 100 list to get a list of the top 100 songs "
                     "from a date provided by the user. It will then take the list of songs and create a new Spotify "
                     "playlist using the Spotify API. Python's Beautiful Soup is used for the web scraping portion.",
        "imgURL": "assets/spotify.jpg",
        "carouselImages": ["assets/spotify.jpg"],
        "githubURL": "https://github.com/blakeoconnell/spotify-wayback-machine",
        "technologies": ["Python", "Web Scraping (Beautiful Soup)", "Web APIs"],
        "learnings": "This project was really fun to develop. It was really cool to not only learn which songs were "
                     "popular the day I was born, but also be able to instantly generate a Spotify playlist and start "
                     "listening right away. Setting up Beautiful Soup to scrape the song titles was not too difficult, "
                     "though I did run into an interesting issue when using some of the song titles to call the Spotify "
                     "API. Not every song is available on Spotify, so in the case that a song title API call returned "
                     "nothing, I had to implement some try/catch logic so the program would not crash. What resulted "
                     "was some playlists not having a full 100 songs on them, but all in all I would call it a success. "
                     "In the future I want to expand on this and maybe even make it into a mobile app that people can "
                     "use to generate a playlist at any time!"
    },
    {
        "id": 6,
        "title": "Automated Cookie Clicker",
        "short_desc": "An automation which plays the well-known web game Cookie Clicker with no human interaction.",
        "long_desc": "This project was built using Selenium to interact with the elements on the webpage. "
                     "The automation clicks cookies as fast as possible, whilst also checking the 'Store' to see if "
                     "any upgrades are available to purchase every 10 seconds. The automation will buy the most "
                     "expensive upgrade it can acquire so it can, of course, get even more cookies.",
        "imgURL": "assets/cclicker-square.png",
        "carouselImages": ["assets/cclicker.jpg"],
        "githubURL": "https://github.com/blakeoconnell/cookie-clicker-automation",
        "technologies": ["Python", "Selenium", "Gameplay Automation"],
        "learnings": "Who doesn't love cookies? Learning about Selenium was kind of a Twilight Zone moment for me, "
                     "becaause in my previous job I was an RPA developer, which involved pretty much doing exactly what "
                     "Selenium does, just with a different (and more powerful) tool. It was really interesting to see "
                     "how other tools are used to solve the same problems I dealt with in RPA. Developing this Cookie "
                     "Clicker automation was fun, because I had to challenge myself to figure out what the optimal "
                     "strategy would be in terms of when to check the store, and what to buy. I spent (probably too "
                     "much) time messing around with different timings, different upgrades, before finally settling on "
                     "'check every 10 seconds, buy most expensive upgrade' and that seemed to work the best. While this "
                     "is just one example of automation with Selenium, I feel that with my background in RPA I could "
                     "come up with a ton more things that would be really awesome to automate, and I'm excited to try "
                     "it out some more in later projects."
    },
    {
        "id": 7,
        "title": "WoW Class Picker",
        "short_desc": "A simple front-end web app to randomly select a playable class for the video game World of Warcraft.",
        "long_desc": "This project was built using entirely front-end technologies to practice adding logic to webpages. "
                     "The picker has filtering options a user can apply prior to the randomizer selecting a class for them.",
        "imgURL": "assets/wowpicker.png",
        "carouselImages": ["assets/wowpicker.png", "assets/wowpicker-2.png"],
        "githubURL": "https://github.com/blakeoconnell/wow-class-picker",
        "technologies": ["Responsive Web Design", "HTML", "CSS", "JavaScript", "jQuery"],
        "learnings": "This was a fun little challenge early on in my web development learning. I gained an understanding of "
                     "interacting with the DOM utilizing jQuery and working with data stored in arrays. "
                     "All in all, the most difficult part of this challenge was actually the HTML/CSS portion. I wanted to "
                     "make sure the design was responsive so mobile users could also use this without difficulty clicking the buttons."
    },
    {
        "id": 8,
        "title": "Do Your Chores",
        "short_desc": "A mobile application designed to randomly designate chore assignments.",
        "long_desc": "This is an iOS app I developed in college as a capstone project. A user must input the names of each person they wish to have chores assigned to, as well as each chore to be completed. The app will then assign an even amount of "
                     "unique chores randomly to each person on the user's list. If the user is satisfied, the session can be saved and referenced at their convenience. "
                     "A map feature is also implemented to take the user from their current location to their home address.",
        "imgURL": "assets/doyourchores.png",
        "carouselImages": ["assets/doyourchores.png"],
        "githubURL": "https://github.com/blakeoconnell/DoYourChores",
        "technologies": ["Swift 4", "CoreData", "Web APIs"],
        "learnings": "Mobile development is one of my biggest passions, and I had a lot of fun with this project. The "
                     "biggest thing I learned from this is how to integrate APIs directly into an application. I also had "
                     "to spend a decent amount of time pouring over documentation to learn how to tap into some of the native "
                     "iOS features such as getting the phone's current location and saving data into the phone's CoreData."

    },
]