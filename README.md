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

![Am I Responsive](/documentation/amiresponsive.jpg)

# The Kitchen Cupboard
The Kitchen Cupboard is a searchable database of recipes. Registered users can add comments and recipe ideas and become part of the Kitchen Cupboard community. This is my submission for the Code Institute Level 5 Diploma in Web Application Development Milestone Project 3.   
The website is live [Here](https://the-kitchen-cupboard-19573f40a32b.herokuapp.com/)

## Table Of Contents:
1. [Design & Planning](#design-&-planning)
    * [User Stories](#user-stories)
    * [Colour Scheme](#colour-scheme)
    * [Typography](#typography)
    * [Imagery](#imagery)
    * [Wireframes](#wireframes)
    * [Database Diagram](#database-diagram)
    
2. [Features](#features)
    * [Navigation](#Navigation-bar)
    * [Home page](#home-page)
    * [Search page](#search-page)
    * [Recipe Details page](#recipe-details-page)
    * [Register page](#register-page)
    * [Sign In page](#sign_in-page)
    * [Profile page](#profile-page)
    * [Add Recipe page](#add-recipe-page)
   

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
    - I chose the pastel colours to create a nostalgic 1950's feel. I used [Coolers](https://coolors.co/93032e-c69f89-a6a15e-84894a-034c3c) to select a complimentary colour palette ![colour palette](/documentation/coolers.png "Colour Palette")
  - #### Typography
    - I chose google fonts 'Pacifico' for my header. This font fits in perfectly with my 1950's styling. I added some text-shadow to create a bit more contrast between the font and the background to ensure legibility.
  - #### Imagery
    - Imagery is important. The large background image with repetitive pattern serves as a backdrop to the information displayed but does not compete for attention. It creates a uniformity that links all the pages together. Image by <a href="https://www.freepik.com/free-vector/flat-green-checkered-background_49189150.htm#query=gingham%20background&position=3&from_view=search&track=ais&uuid=c2a4f938-aa1b-48bb-8fd4-0dfadcc1a4e7">Freepik</a>

### Wireframes
  - User Flowchart - [View](/documentation/flow_chart.png)
  - Home Page Wireframe - [View](/documentation/kitchen_home.png)
  - Register Page Wireframe - [View](/documentation/kitchen_register.png)
  - Sign In Page Wireframe - [View](/documentation/kitchen_signin.png)
  - Search Page Wireframe - [View](/documentation/kitchen_search.png)
  - Search Results Page Wireframe - [View](/documentation/kitchen_results.png)
  - Profile Page Wireframe - [View](/documentation/kitchen_profile.png)
  - Add/Edit Page Wireframe - [View](/documentation/kitchen_add_recipe.png)

### DataBase Diagram
  - Database Schema - [View](/documentation/database_schema.png)

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [PYTHON](https://www.python.org/)

### Frameworks, Libraries & Programs Used

1. [Lucidchart:](https://lucidchart.com/)
   - Lucidchart was used to create the [flowcharts](#wireframes-&-flowcharts) during the design process
1. [Balsamiq:](https://balsamiq.com/)
   - Balsamiq was used to create the [wireframes](#wireframes-&-flowcharts) during the design process
1. [dbdiagram:](https://dbdiagram.io)
   - dbdiagram was used to create the [database schema](/documentation/database_schema.png) during the design process
1. [Flask:](https://palletsprojects.com/p/flask/)
   - Flask was used to create the Python web framework.
1. [Random Keygen:](https://randomkeygen.com/)
   - Random keygen was used to create the Secret Key which kept registered users details secure.
1. [Materialize 1.0.0:](https://materializecss.com/)
   - Materialize was used to assist with the responsiveness and styling of the website.
1. [JQuery:](https://releases.jquery.com/)
   - jQuery was used in conjunction with Materialize.
1. [Hover.css:](https://ianlunn.github.io/Hover/)
   - Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.
1. [Google Fonts:](https://fonts.google.com/)
   - Google fonts were used to import the 'Pacifico' font into the style.css file which is used for my header text.
1. [Font Awesome:](https://fontawesome.com/)
   - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [Favicon.io:](https://favicon.io/)
   - Favicon.io was used to create the icon on the web page tab.
1. [I Love IMG:](https://www.iloveimg.com/resize-image)
   - I Love IMG was used to crop and resize all images to enhance performance and increase Lighthouse scores during testing.
1. [Codeanywhere](https://codeanywhere.com/signin)
   - Codeanywhere was used for version control by utilizing the Codeanywhere terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
   - GitHub was used to store the projects code after being pushed from Git.
1. [Heroku:](https://heroku.com/)
   - Heroku was used to deploy my project.

## Features:
  - **Navigation Bar**    
  I used Materialize to build my navigation bar, it collapses down on mobile screens and becomes a burger menu. The options available for non-registered users are HOME/SEARCH/SIGN IN/REGISTER. 
  ![Nav bar](/documentation/navbar.jpg)    
  Once registered the options offered are HOME/SEARCH/PROFILE/ADD RECIPE/SIGN OUT.    
  ![Nav bar extended](/documentation/navbar_extra.jpg) 
  I chose to keep the search option available to non-registered users as I wanted first-time visitors to be able to explore before committing to joining. Once logged in, users have the ability to upload recipes of their own and edit /delete their recipes too.    


  - **Home Page**    
  ![Home page](/documentation/uxhome_mobile.jpg)    
  The home page is simple and directs visitors towards either the search function in the nav bar or the invitation to join the Kitchen Cupboard community. The wording used aims to be friendly, welcoming and informal.    
  The use of the tablecloth image for the background creates uniformity within the pages of the site but also allows the content to be the focus.    
  The font used for the heading conjures up the 1950's feel that I wanted for the site, I chose "Pacifico" from google fonts.    
  The social media links are in the footer but they are very much in the background should people wish to find them rather than the focal point.


  - **Search Page**    
  ![Search page](/documentation/uxsearch_mobile.jpg)  
  The search page is probably the first place that new visitors will navigate to. There is no need to be registered so I anticipate they will explore whether the site is for them by using the search feature first.    
  Users can search by keyword. I chose this option as I feel it is quick and simple. I did consider having dropdown menus to select Difficulty Level and Cuisine but I abandoned this as it over-complicated things and made the interface cluttered especially on mobiles. I think it would be more useful to add this as an option to filter the results once a keyword search has been performed.    
  The keyword search interrogates two fields in my database, the name and ingredients. This picks up any recipe that uses the keyword as an ingredient within it even though it may not be specifically mentioned in the title.    
  The search results are returned and displayed using Materialize's card component. The class rule dictates that the results are displayed 4 side-by-side on desktops, 2 side-by-side on tablets and stacked singly on mobiles.  
    
  ![Mobile view](/documentation/uxresults_mobile.jpg =30%x) ![Tablet view](/documentation/uxresults_ipad.jpg =30%x) ![Desktop view](/documentation/uxresults_desktop.jpg =30%x)  

  The results cards only display the recipe image, name and difficulty level not the full details. This should be enough for the user to decide whether they would like to read further and the image and title are a link that will then open the individual recipe up on a separate page.    
  The full recipe details are then displayed - Image, name, difficulty level, ingredients, method and created by. As users are also allowed to upload their own recipes some of the fields may have been ommitted and these will not then be displayed, if there has been no image uploaded a placeholder image will be displayed instead to preserve the uniformity of the display style.


  - **Recipe Details Page**    

  - **Register Page**    
  ![Register page](/documentation/uxregister_mobile.jpg)  
  The register page has a simple layout where the user is presented with a form to fill in consisting of two fields, username and password. The placeholder text explains that the chosen username must contain at least five characters.    
  The form is based on the code from the Code Institute non-relational mini project. I really liked the idea of the input fields changing colour from red to green once a valid username and password have been selected. If an invalid word is chosen a pop-up prompt reminds the user of the minimum character rule. I have used font awesome icons to illustrate what the fields are for.    
  The text under the form provides a link to 'Sign In' for registered users who might have found themselves in the wrong place.    
  The form looks just as good on mobile devices with all information visible without having to scroll down.


  - **Sign In Page**    
  ![Sign in page](/documentation/uxsignin_mobile.jpg)  
  The sign in page repeats the layout and features of the 'Register' page, this keeps the site looking uniform. If an incorrect username or password is entered a flash message is displayed 'Incorrect Username and/or Password'. This message deliberately does not specify whether is was the username or password that was incorrect to reduce the chance of a malicious user attempting to guess. Extra layers of security and complexity could be added dependent on how the site evolves and the user data it contains. I have used Werkzeug for password hashing to protect registered users data.    
  The text under the form provides a link to 'Register' for new users who might have found themselves in the wrong place.    
  The form looks just as good on mobile devices with all information visible without having to scroll down.


  - **Profile Page**    
  ![Profile page](/documentation/uxprofile_mobile.jpg)  
  The signed in user is automatically re-directed to their profile page where they are greeted by a welcome message. The profile page contains the dashboard which displays their own recipes and offers the ability to edit or delete their own recipes if desired. Once signed in the 'Add Recipe' option is displayed in the navigation bar.


  - **Add Recipe Page**    
  ![Add recipe page](/documentation/uxaddrecipe_mobile.jpg)    
  This page allows the registered user to add their own recipes which will then be searchable by other users. The form follows the format of the other forms on the site for uniformity and brand identity. A text box explains the purpose of the form and then there are input fields for image, name, ingredients and method followed by a submit button.    
  The upload image field restricts uploads to a file size of 1MB maximum. This was chosen to limit the storage space needed but could be reduced furthur if required. The file extensions allowed have been restricted to jpg, jpeg and png. This is a safety precaution and only allows image file formats to be uploaded. The uploading of an image is optional and if no image is provided a placeholder image will be displayed in its place.   
  The recipe name field is unrestricted in length but the CSS text-overflow: ellipsis property has been applied to the display settings to prevent over-long titles being displayed in full.    
  The ingredients input field contains placeholder text asking the user to list each ingredient on a separate line. This is because I have written code that will add a semi-colon to the end of each inputted line and this will then split each line when displayed to create a list. The Materialize text-area class has been applied, this enables the size of the input box to expand to the amount of content within it.    
  The method input field contains placeholder text asking the user to list each step on a separate line. This is because I have written code that will add a semi-colon to the end of each inputted line and this will then split each line when displayed to create a list. The Materialize text-area class has been applied, this enables the size of the input box to expand to the amount of content within it.    
  The submit button posts the information to my Mongodb database.     


Explain your features on the website,(navigation, pages, links, forms, input fields, CRUD....)

## Testing

### Google's Lighthouse Performance
Screenshots of certain pages and scores (mobile and desktop)
### Browser Compatibility
I have tested compatibility on the following browsers. Safari, Chrome, Edge and Firefox.
### Responsiveness
- Responsive on all device sizes - This was checked using [Am I Responsive](https://ui.dev/amiresponsive) and by asking friends and family to test it on their devices. The devices checked included Android (Galaxy A30 and Galaxy A), iPhone 8 and 10, iPad Air, Chromebook, Laptop and PC.
![Am I Responsive](/documentation/amiresponsive.jpg)
### Code Validation
- **HTML** 
The W3 HTML validation tool was used. I validated by URI [HTML5](https://validator.w3.org/)
![HTML Validator](/documentation/html_validation.jpg)
- **CSS** 
The W3 CSS validation tool was used. I validated by URI [CSS](https://jigsaw.w3.org/css-validator/)
![CSS Validator](/documentation/css_validation.jpg)
- **JS** [JS](https://www.jslint.com/)
- **PYTHON** [PYTHON](https://www.pythonchecker.com/)
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

### Code

- Code Institute's Task Manager project walkthrough. Used to create the user authentication function[Code Institute](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/02-UserAuthenticationAndAuthorization/04-login_functionality)
- Code Institute's Task Manager project walkthrough. Used to create the search function[Code Institute](https://github.com/Code-Institute-Solutions/TaskManagerAuth/blob/main/08-SearchingWithinTheDatabase/01-text_index_searching/app.py#L28)
- How to center a div using Flex [Stack Overflow](https://stackoverflow.com/questions/9862167/positioning-div-element-at-center-of-screen)

### Content

- All content for the individual recipes (images and text) was obtained from [BBC Good Food](https://www.bbcgoodfood.com/)
- Placeholder image acquired from [Freepik]("https://www.freepik.com/free-vector/hand-drawn-cutlery-set_16263394.htm#query=plate%20cutlery&position=2&from_view=search&track=ais&uuid=14df9a14-5a9b-431b-80f6-777890683ee5")Image by rawpixel.com

### Acknowledgements

- My Mentor for continuous helpful feedback.
- Tutor support at Code Institute for their support.

