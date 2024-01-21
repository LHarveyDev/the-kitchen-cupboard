![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for the mongo lessons. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Codeanywhere and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **April 3rd, 2023**

## Codeanywhere Reminders

# IDE

- **Connect to Mongo CLI on a IDE**
- navigate to your MongoDB Clusters Sandbox
- click **"Connect"** button
- select **"Connect with the MongoDB shell"**
- select **"I have the mongo shell installed"**
- choose option 4.4 for : **"Select your mongo shell version"**
- choose option: **"Run your connection string in your command line"**
- `mongo "mongodb+srv://<CLUSTER-NAME>.mongodb.net/<DBname>" --username <USERNAME>`
  - replace all `<angle-bracket>` keys with your own data
- enter password *(will not echo **\*\*\*\*** *on screen)\*

#### Clear screen in Mongo Shell:

- `cls`

#### Show all database collections:

- `show collections`

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A button should appear to click: _Open Preview_ or _Open Browser_.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

---

Happy coding!

# The Kitchen Cupboard
The Kitchen Cupboard is a searchable database of recipes. Registered users can add comments and recipe ideas and become part of the Kitchen Cupboard community. This is my submission for the Code Institute Level 5 Diploma in Web Application Development Milestone Project 3.

## Table Of Contents:
1. [Design & Planning](#design-&-planning)
    * [User Stories](#user-stories)
    * [Wireframes & Flowcharts](#wireframes-&-flowcharts)
    * [Typography](#typography)
    * [Colour Scheme](#colour-scheme)
    * [Database Diagram](#database-diagram)
    
2. [Features](#features)
    * [Navigation](#Navigation-bar)
    * [Footer](#footer)
    * [Home page](#home-page)
    * [Register page](#register-page)
   

3. [Technologies Used](#technologies-used)
4. [Libraries](#libraries-used)
5. [Testing](#testing)
6. [Bugs](#bugs)
7. [Deployment](#deployment)
8. [Credits](#credits)
9. [Acknowledgment](#acknowledgment)

## Design & Planning:

## User Experience (UX)

- ### User stories

  - #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn how to navigate to the areas I want to use.
    2. As a First Time Visitor, I want to be able to easily navigate throughout the site and search for content.
    3. As a First Time Visitor, I want to register as a user.
    4. As a First Time Visitor, I want to locate their social media links to see their followings on social media to determine how trusted and known they are.

  - #### Returning Visitor Goals

    1. As a Returning Visitor, I want to log in and view my profile.
    2. As a Returning Visitor, I want to search for a new recipe to make.
    3. As a Returning Visitor, I want to log in and add my own recipes.
    4. As a Returning Visitor, I want to check if there are any social media updates.

  - #### Frequent User Goals

    1. As a Frequent User, I want to log in and add a recipe.
    2. As a Frequent User, I want to log in and edit/delete a recipe I have previously added.
    3. As a Frequent User, I want to search for a new recipe to make.
    4. As a Frequent User, I want to check if there are any social media updates.

- ### Design

  - #### Colour Scheme
    - I chose the colours to create a fresh, vibrant feel to users. I used [Coolers](https://coolors.co/93032e-c69f89-a6a15e-84894a-034c3c) to select a complimentary colour palette ![colour palette](/documentation/coolers.png "Colour Palette")
  - #### Typography
  - #### Imagery
    - Imagery is important. The large background image is designed to be striking and catch the user's attention. It creates a uniformity that links all the pages together. Photo by Lukas</a> on <a href="https://www.pexels.com/photo/variety-of-vegetables-616401/">Pexels</a>

* ### Wireframes & Flowcharts

  - User Flowchart - [View](/documentation/the_kitchen_cupboard.png)
  - Home Page Wireframe - [View](/documentation/kitchen_home.png)
  - Register Page Wireframe - [View](/documentation/kitchen_register.png)
  - Sign In Page Wireframe - [View](/documentation/kitchen_signin.png)
  - Search Page Wireframe - [View](/documentation/kitchen_search.png)
  - Search Results Page Wireframe - [View](/documentation/kitchen_results.png)
  - Add/Edit Page Wireframe - [View](/documentation/edit.pdf)

## Features

- Responsive on all device sizes - [Am I Responsive](https://ui.dev/amiresponsive?url=https://lharveydev.heroku.com/the-kitchen-cupboard/)

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [PYTHON](https://www.python.org/)

### Frameworks, Libraries & Programs Used

1. [Lucidchart:](https://lucidchart.com/)
   - Lucidchart was used to create the [flowcharts](https://lucidchart.com/) during the design process
1. [Balsamiq:](https://balsamiq.com/)
   - Balsamiq was used to create the [wireframes](https://balsamiq.com/) during the design process
1. [dbdiagram:](https://dbdiagram.io)
   - Balsamiq was used to create the [database schema](https://dbdiagram.io) during the design process
1. [Flask:](https://palletsprojects.com/p/flask/)
   - Flask was used to create the Python web framework.
1. [Random Keygen:](https://randomkeygen.com/)
   - Random keygen was used to create the Secret Key which kept registered users details secure.
1. [Materialize 1.0.0:](https://materializecss.com/)
   - Materialize was used to assist with the responsiveness and styling of the website.
1. [JQuery:](https://releases.jquery.com/)
   - jQuery was used in conjunction with Materialize.
1. [CDNjs:](https://cdnjs.com/)
   - CDNjs was used to find the Font Awesome CDN.
1. [Hover.css:](https://ianlunn.github.io/Hover/)
   - Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.
1. [Google Fonts:](https://fonts.google.com/)
   - Google fonts were used to import the 'Ubuntu' font into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
   - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [Logo:](https://logo.com/)
   - Logo was used to create an eye-catching logo used on the home page.
1. [Favicon.io:](https://favicon.io/)
   - Favicon.io was used to create the icon on the web page tab.
1. [I Love IMG:](https://www.iloveimg.com/resize-image)
   - I Love IMG used to crop and resize all images to enhance performance and increase Lighthouse scores during testing.
1. [Codeanywhere](https://codeanywhere.com/signin)
   - Codeanywhere was used for version control by utilizing the Codeanywhere terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
   - GitHub was used to store the projects code after being pushed from Git.
1. [Heroku:](https://heroku.com/)
   - Heroku was used to deploy my project.

### DataBase Diagram
  - Database Schema - [View](/documentation/database_schema.png)

## Features:
Explain your features on the website,(navigation, pages, links, forms, input fields, CRUD....)

## Testing

### Google's Lighthouse Performance
Screenshots of certain pages and scores (mobile and desktop)
### Browser Compatibility
Check compatability with different browsers (Firefox, Edge, Chrome)
### Responsiveness
Screenshots of the responsivness, pick few devices
### Code Validation
Validate your code HTML, CSS, JS & Python - display screenshots
### Manual Testing user stories
Test all your user stories, you can create table 
User Story |  Test | Pass
--- | --- | :---:
paste here your user story | what is visible to the user and what action they should perform | &check;
- attach screenshot
### Manual Testing features
Test all your features, you can use the same approach 
| Status | feature
|:-------:|:--------|
| &check; | description
- attach screenshot
## Bugs
List of bugs and how did you fix them, you can create simple table
| Bug | Fix
|:-------:|:--------|
|   |    |
## Deployment
This website is deployed to Heroku from a GitHub repository, the following steps were taken:

#### Creating a Repository on GitHub
- First make sure you are signed into [Github](https://github.com/) and go to the code institutes template, which can be found [here](https://github.com/Code-Institute-Org/ci-mongo-template).
- Then click on **use this template** and select **Create a new repository** from the drop-down. Enter the name for the repository and click **Create repository**.
- Once the repository was created, I clicked the green **code** button and copied the HTTPS address. I then navigated to [Codeanywhere](https://app.codeanywhere.com/)and clicked on **New Workspace** to create a workspace in codeanywhere so that I could write the code for the site.
  
#### Making a Local Clone
1. Log in to GitHub and locate the [GitHub Repository](https://github.com/LHarveyDev/the-kitchen-cupboard)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/LHarveyDev/the-kitchen-cupboard
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/LHarveyDev/the-kitchen-cupboard
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

#### Forking the Github Repository 
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/LHarveyDev/the-kitchen-cupboard.git)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

#### Creating an app on Heroku
- After creating the repository on GitHub, head over to [heroku](https://www.heroku.com/) and sign in.
- On the home page, click **New** and **Create new app** from the drop down.
- Give the app a name(this must be unique) and select a **region** I chose **Europe** as I am in Europe, Then click **Create app**.

#### Deploying to Heroku.
- In Codeanywhere CLI, the root directory of the project, run: pip3 freeze --local > requirements.txt to create a requirements.txt file containing project dependencies.
- In the Codeanywhere project workspace root directory, create a new file called Procfile, with capital 'P'. Open the Procfile. - Inside the file, check that web: python3 app.py has been added when creating the file Save the file.
- Push the 2 new files to the GitHub repository
- Login to Heroku, select Create new app, add the name for your app and choose your closest region.
- Navigate to the Deploy tab on Heroku dashboard and select Github, search for your repository and click 'connect'.
- Navigate to the settings tab, click reveal config vars and input the following:


| Key | Value
|:-------:|:--------|
| DATABASE_URL  |    |
| IP  |    |
|  PORT |    |
|  SECRET_KEY   |     |

Actual Enviroment variables not disclosed for security

## Credits
- How to center a div using Flex [Stack Overflow](https://stackoverflow.com/questions/9862167/positioning-div-element-at-center-of-screen)

## Acknowledgment
Mention people who helped you with your project(mentor, colleagues...)

