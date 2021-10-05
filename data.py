project_data = [
    {
        "id": 0,
        "title": "WoW Class Picker",
        "short_desc": "A simple front-end web app to randomly select a playable class for the video game World of Warcraft.",
        "long_desc": "This project was built using entirely front-end technologies to practice adding logic to webpages. "
                     "The picker has filtering options a user can apply prior to the randomizer selecting a class for them.",
        "imgURL": "assets/444x444wowpicker.png",
        "githubURL": "https://github.com/blakeoconnell/wow-class-picker",
        "technologies": ["Responsive Web Design", "HTML", "CSS", "JavaScript", "jQuery"],
        "learnings": "This was a fun little challenge early on in my web development learning. I gained an understanding of "
                     "the importance of cleaning storing data so I could use it without a ton of difficulty. "
                     "All in all, the most difficult part of this challenge was actually the HTML/CSS portion. I wanted to "
                     "make sure the design was responsive so mobile users could also use this without difficulty clicking the buttons."
    },
    {
        "id": 1,
        "title": "Do Your Chores",
        "short_desc": "A mobile application designed to randomly designate chore assignments.",
        "long_desc": "This is an iOS app I developed in college as a capstone project. A user must input the names of each person they wish to have chores assigned to, as well as each chore to be completed. The app will then assign an even amount of "
                     "unique chores randomly to each person on the user's list. If the user is satisfied, the session can be saved and referenced at their convenience. "
                     "A map feature is also implemented to take the user from their current location to their home address.",
        "imgURL": "assets/doyourchores.png",
        "githubURL": "https://github.com/blakeoconnell/DoYourChores",
        "technologies": ["Swift 4", "CoreData", "Web APIs"],
        "learnings": "Mobile development is one of my biggest passions, and I had a lot of fun with this project. The "
                     "biggest thing I learned from this is how to integrate APIs directly into an application. I also had "
                     "to spend a decent amount of time pouring over documentation to learn how to tap into some of the native "
                     "iOS features such as getting the phone's current location and saving data into the phone's CoreData."

    },
    {
        "id": 2,
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

    }
]