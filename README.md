<h1 align="center">David Harris - Milestone Project 3</h1>

The focus of this project is to design and build a back-end database application using Python and MongoDB that will allow users of a website to view, modify and delete items in a database via a front-end website. This will show full interaction of the data for the user from the front-end & the back-end. The database and application will be focused on all aspects of CRUD.

As the focus of this project will be the data, database & CRUD for the data from the back-end to the front end. I will spend the focus of this time on the design of the database, python interactions and will spend less time focusing on the front end. I have chosen to use HTML, CSS, Flask, Jinja, Google Materialize. I plan to implement the templating feature of Jinja along with a base template from Google Materialize to allow the front-end website to be fully interactive and have a standard template & design to ensure consistency throughout all pages of the site.

The content of the website will be a recipe website about cocktails, both alcoholic and non-alcoholic.
- The website will be a store of all recipes that users have created. All visitors to the website will be able to view the recipes, they will not need a user account to view.
- The website will have user authentication and privileges. What I mean by this is that only the creator of the recipe will be able to delete or modify their own created recipes, but all users and non-users will be able to view the recipes.

## User Experience (UX)

### User stories

#### First Time Visitor Goals
- As a first-time visitor I want to easily understand the main purpose of the website.
- As a first-time visitor I want to be able to view and browse the recipes instantly without a barrier to entry.

 #### Returning Visitor Goals
- As a returning visitor I want to be able to create my own personal user account for the website.
- As a returning visitor I want to be able to create and upload my own personal recipes for the website.

#### Frequent Visitor Goals
- As a frequent visitor I want to be able to access my previous recipes and modify them with changes, ensuring that the changes are saved back to the website.
- As a frequent visitor I want to be able to access my previous recipes and delete them if I wish.

### Design

#### Colour Scheme
As I will be focused on the Python3 & MongoDB side of this project, I have decided to focus my time spent on the back-end database/Python3 logic. To reduce time spent on the front-end design, I am going to use a pre-built template from the “Google Materialize” website. I will pick one that is neutral and fits to a broad audience. The aim here is to allow the data to be easy to view, digest and understand for the users.

#### Typography
The font that I have chosen is for this website is “Nunito” via “Google Fonts”. I have chosen to use this font as it is a nice balance of “easy to read”, “casual” & “professional”.

#### Wireframes
Please use the links below to download my wireframe designs in PDF format.
- [Desktop View Wireframe](assets/wireframes/wireframe-desktop-view.pdf)
- [Mobile View Wireframe](assets/wireframes/wireframe-mobile-view.pdf)
- [Tablet View Wireframe](assets/wireframes/wireframe-tablet-view.pdf)

## Technologies Used

### Languages Used
- [HTML:](https://en.wikipedia.org/wiki/HTML) This project uses HTML for the basic structure of the data.
- [CSS:](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) This project uses CSS for applying custom styles to the HTML.
- [Python3:](https://en.wikipedia.org/wiki/Python_(programming_language)) This project uses Python3 as the core logic and functionality of the application. The full data interaction with the MongoDB will be built and testing using Python3.

### Frameworks, Libraries & Programs Used
- [Git:](https://git-scm.com/) Git was used for version control by utilizing the GitPod terminal to commit to Git and Push to GitHub.
- [GitHub:](https://github.com/) GitHub is used to store the projects code after being pushed from Git.
- [Favicon:](https://favicon.io/favicon-generator/) I will generate a custom favicon image from this website for my project.
- [Font Awesome:](https://fontawesome.com/) I will be using Font Awesome custom icons for the site. I plan to use the social media icons for the footer of the website.
- [Google Fonts:](https://fonts.google.com/) Google Fonts were used to import the "Gloria Hallelujah" font into the style.CSS file which is used on all pages throughout the project.
- [Google Materialize:](https://en.wikipedia.org/wiki/Material_Design) Google Materialize will be used to take a temple of the front end-design. I will be using pre-built features as a base for a template and will make some customisations where required.
- [Flask:](https://en.wikipedia.org/wiki/Flask_(web_framework)) I will be used in conjunction with Python3 to allow additional functionality for my webapp. I am planning on using “Flask Flash” to display messages to users.
- [Jinja:](https://en.wikipedia.org/wiki/Jinja_(template_engine)) I will be using Jinja primarily for its templating and logic to automatically generate front-end layouts, depending on back-end content of the website.
- [Werkzeug:](https://en.wikipedia.org/wiki/Flask_(web_framework)#Werkzeug) I will be using Werkzeug to enable secure user authentication. This will be used to store the login details for the user accounts in a secure hash file.
- [MongoDB:](https://en.wikipedia.org/wiki/MongoDB) I will be using MongoDB as the database software. I have chosen this software as this is a NoSQL based database system. I have chosen this as I do not require a relational database structure for this project.
- [Heroku:](https://en.wikipedia.org/wiki/Heroku) I will be using Heroku to deploy my project, this is due to needing to deploy a back-end enabled application.
- [Balsamiq:](https://balsamiq.com/) Balsamiq was used to create the wireframes during the design process.