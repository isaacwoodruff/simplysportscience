# ! THIS IS THE OLD VERSION !
This version uses some old APIs that are unfortunetly no longer supported. This version is left here to demonstrate the rapid development of a project of this scope by the developer.

Please find the new version [here](https://github.com/isaacwoodruff/simplysportscience-v2). 

# Simply Sport Science
[Simply Sport Science](https://simplysportscience.herokuapp.com/) was created as a job board to connect employers and candidates in the area of sport science.

[![Build Status](https://travis-ci.org/isaacwoodruff/simplysportscience.svg?branch=master)](https://travis-ci.org/isaacwoodruff/simplysportscience)

## Table of Contents

1. [UX](#ux)
    - [Goals](#goals)
        - [Business Goals](#simply-sport-science-goals)
        - [Employer Goals](#employer-goals)
        - [Candidate Goals](#candidate-goals)
    - [User Stories](#user-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)
    - [Information Architecture](#information-architecture)

2. [Features](#features)
    - [Existing Features](#existing-features)
        - [Job Search](#job-search)
        - [Employers Page](#employers-page)
        - [Candidates Page](#candidates-page)
        - [User Profile Page](#user-profile-page)
        - [Delete Account Page](#delete-account-page)
        - [Sign Up Page](#sign-up-page)
        - [Sign In Page](#sign-in-page)
        - [Job Details Page](#job-details-page)
        - [New Job Page](#new-job-page)
        - [Checkout](#checkout)
    - [Features Left to Implement](#features-left-to-implement)

4. [Technologies Used](#technologies-used)

5. [Testing](#testing)

6. [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Heroku Deployment](#heroku-deployment)

7. [Credits](#credits)

# UX
## Goals
The goal of this website is to create a job board to connect employers and candidates in the area of sport science.

### Simply Sport Science Goals
The goals of Simply Sport Science are to:
- Create an efficient service to help the sport science community connect with the employers/employees they want
- Monetize the job board by offering job posting packages to potential employers

The target audiences for this website are:
- Employers in the area of sport science
- Candidates in the area of sport science

### Employer Goals
The goals of employers on the website are to:
- Have access to a platform that connects employers and candidates in the sport science community
- Find a selection of quality candidates for job openings in their organisation

### Candidate Goals
The goals of candidates on the website are to:
- Easily find the jobs they want in the area of sport science
- Connect with employers

## User Stories
### Employer User Stories
A employer using [Simply Sport Science](https://simplysportscience.herokuapp.com/) expects to:
- Be able to register, login, and logout
- Have their own profile which they can create, read, update or delete
- Create job posts
- Easily and securely pay for publishing job posts

### Candidate User Stories
A candidate using [Simply Sport Science](https://simplysportscience.herokuapp.com/) expects to:
- Be able to register, login, and logout
- Have their own profile which they can create, read, update or delete
- View jobs from employers
- Easily search through jobs by job title, location, and employment type
- Have access to contact information for the employers on each job

## Design Choices
Simply Sport Science was designed to look professional and minimalistic:
- It utilises office/desk/business setting images for backgrounds and banners
- Only two fonts were chosen to keep the design familiar to the user throughtout the site
- Only a handful of icons were used to convey visual communication to the user *e.g search inputs, breadcrumbs*
- A light shade of blue was mainly used for buttons because it is known in color psychology for signifying reliability, responsibility, and dependability. It is a professional color

## Wireframes
The following wireframes were designed with Balsamiq.

Desktop View
- [Jobs Search Page](https://ibb.co/GRSb6Hx)
- [Employer/Candidates Page](https://ibb.co/YQXxyNS)
- [New Job Page](https://ibb.co/HhVC42P)
- [Job Details Page](https://ibb.co/qjDCvGp)
- [Profile Page](https://ibb.co/2q1grSB)

Mobile View
- [Jobs Search Page](https://ibb.co/jWjb0bX)

# Information Architecture
- During the develoment phase of the project a SQlite3 database was used. This is the default that Django uses for local development.
- The deployed site uses a PostgreSQL database. This is provided as an add-on in Heroku.

## Database Models
#### User Model
The User model for this project is the standard User model provided by Django.

#### EmployerProfile Model
Key | Validation | Field Type |
--- | --- | ---
user | User, on_delete=models.CASCADE | OneToOneField
is_employer | default=True | BooleanField
is_candidate | default=False | BooleanField
company_name | max_length=200 | CharField
credits | default=0 | IntegerField
slug | blank=True, null=True | SlugField

#### CandidateProfile Model
Key | Validation | Field Type |
--- | --- | ---
user | User, on_delete=models.CASCADE | OneToOneField
is_employer | default=True | BooleanField
is_candidate | default=False | BooleanField
first_name | max_length=100 | CharField
last_name | max_length=100 | CharField

#### Job Model
Key | Validation | Field Type |
--- | --- | ---
title | max_length=200 | CharField
employment_type | max_length=50, choices=EMPLOYMENT_TYPE_CHOICES, default=FULL_TIME | CharField
requirements | blank=True, null=True | TextField
location | max_length=100 | CharField
employer | max_length=200 | CharField
views | default=0 | IntegerField
created_date | auto_now_add=True | DateTimeField
published_date | blank=True, null=True, default=timezone.now | DateTimeField
slug | blank=True, null=True | SlugField

# Features
## Existing Features
##### Job Search
- The main component is the search feature for finding all jobs on the website with options to:
    - Filter by job title, location, type of employment (full time, part time, etc.)
- The search features an autocomplete for job titles that pulls job titles from the database and suggest them to the user. This uses jQuery UI 
- The search also makes use of Algolia Places API in the location input to autocomplete city names from all over the world
- Paginated results with 10 posts per page
- The amount of days ago the job was posted
- Posts containing job title, employment company, employment type, location
- Each company name, location, and employment type is a tag that can be clicked to search for all jobs relating to the tag
- A minimalist, professional design

##### Employers Page
- A list of reasons why employers would benefit from posting listings on the website
- An option to sign up as an employer
- If a candidate is viewing this page they also have an option to sign up as a candidate

##### Candidates Page
- A list of reasons why candidates would benefit from signing up to an account
- An option to sign up as a candidate
- If an employer is viewing the page they also have an option to sign up as an employer

##### User Profile Page
- Displays a form with user profile details. The form is autopopulated from their account in the database
- The user has two options on the page. Update their profile or delete their account.

##### Delete Account Page
- Asks the user if they are sure they want to delete their profile
- Requires the user to confirm with their email and password

##### Sign Up Page
- Shows a registration form with two buttons at the top to easily switch between employer and candidate registration
- Has a link at the bottom that redirects to the sign in page if the user already has an account

##### Sign In Page
- Shows a sign in form with an encouraging message at the top
- Has a link at the bottom to sign up if the user doesn't have an account
- Has a 'Forgot Password' option

##### Job Details Page
- Shows all the details of the job such as:
    - Description
    - Requirements
    - Location
    - Employer
    - Employment type
    - Contact info
- A button at the bottom displays a modal with the contact details of the employer
- A circular button with a back arrow navigates the user back to their previous page

##### New Job Page
- Displays a form to create a new job
- Uses Algolia Places API to autocomplete on the location input for suggestions of cities worldwide
- At the bottom of the page there is a button to post the new job. If the employer has credits then the job will be posted. If they don't have credits then they receive a warning telling them to buy more
- The amount of credits they have is displayed next to the post job button
- There is a Buy More button next to the credit amount. This navigates to a page that redirects the user to Stripe Checkout's payment gateway.
- Upon successful completion the user is redirected to the payment success page which tells the user it was successful

##### Checkout
- The checkout uses webhooks to confirm with Stripe API that the payment was successful
- Stripe sends a checkout successful object with the session ID sent at time of payment
- The client_reference_id is used to send the unique email attached to their account on our website to Stripe in the session object
- When the session object is received by Simply Sport Science a function is called that uses the client_reference_id to uniquely identify the user and assign their account credit
- A response is sent to Stripe to confirm that the webhook was received and to complete the payment


## Features Left To Implement
##### Home/Landing Page
- Landing page which shows several sections:
    - A search bar for finding jobs at the top
    - A small selection of the jobs page with around 5 jobs and a button to Find More Listings which redirects to the jobs page
    - A Call-To-Action for signing up to a newsletter and registering an account
    - Some companies that the website lists jobs for
    - A small selection of articles from the blog

##### Blog
- A blog with:
    - Industry specific career advice
    - Interviews with people in the industry
    - Articles in the area of sport science
    - Useful resources

##### Employer Account Page
- Dashboard for a logged in employer with:
    - Help section on how to use the dashboard
    - Option to post a job
    - List of all job postings from employer
    - Amount of times job post was clicked on next to each job post in the list
    - Amount of times job post was applied to next to each job post in the list
    - Option to click on profiles of candidates who applied (If they are registered on the website)
    - View job package subscription and have option to repeat payment or upgrade

##### Candidate Account Page
- Dashboard for a logged in candidate with:
    - Help section on how to use the dashboard
    - Option to upload CV
    - Option to fill out profile or autopopulate profile from CV
    - Offer CV templates
    - View list of favourite/saved jobs
    - Links to career advice articles on the blog

##### Miscellaneous Features
- Set alerts for a specific search parameter *e.g. biomechanist jobs in New York, US.*
- Save jobs to favourites list. If user hasn't got an account this leads to them signing up to use this feature
- Newsletter of newest jobs, and industry specific career advice
- Easy one click applications (by uploading CV or filling out profile on signup)

# Technologies Used

### Programming Languages
- This project uses **HTML**, **CSS**, **JavaScript** and **Python**.

### Tools
- [Django](https://www.djangoproject.com/) as a python web application framework for faster development.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to style django forms for speeding up design.
- [Gunicorn](https://pypi.org/project/gunicorn/) a Python Web Server Gateway Interface HTTP server to aid in deployment of the Django project for heroku deployment.
- [Psycopg2](https://pypi.org/project/psycopg2/) as a DB API 2.0 compliant PostgreSQL driver for Python.
- [Whitenoise](http://whitenoise.evans.io/en/stable/) to allow the web app to serve its own static files.
- [Visual Studio Code](https://code.visualstudio.com/) as the Integrated Development Environment while developing this project.
- [PIP](https://pip.pypa.io/en/stable/installing/) to install the tools needed in this project.
- [Stripe](https://stripe.com) as a payment gateway to validate and accept credit card payments securely.
- [Algolia Places ](https://community.algolia.com/places/) to provide a fast and easy way to use address search autocomplete by harnessing OpenStreetMap's database.
- [Git](https://git-scm.com) for version control during the development process. 
- [GitHub](https://github.com/) for a remote repository.
- [Travis](https://travis-ci.org/) for Continuous Integration.
- [Heroku](https://www.heroku.com/) for hosting and deployment.
- [Balsamiq](https://balsamiq.com/) to build wireframes in the planning stage of development.
- [Google Chrome - Dev Tools](https://www.google.com/chrome/) to test responsiveness, to debug code by utilising breakpoints and the console, and to speed up the design process.
- [AutoPrefixer](https://autoprefixer.github.io/) to add prefixes in the CSS for cross-browser support.
- [Imgbb](https://imgbb.com) to store external images.

### Databases
- [PostgreSQL](https://www.postgresql.org/) as the database for the deployed site, hosted on Heroku.
- [SQlite3](https://www.sqlite.org/index.html) as the database for the development environment, provided by django.

### Libraries
- [JQuery](https://jquery.com) to simplify HTML DOM tree traversal and manipulation, event handling, and Ajax.
- [JQuery UI](https://jqueryui.com/) to enables users to quickly find and select from a pre-populated list of values as they type, leveraging searching and filtering.
- [Bootstrap](https://www.bootstrapcdn.com/) to develop responsive and mobile-first pages more easily.
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) to provide icons for the project.
- [Google Fonts](https://fonts.google.com/) to provide and style fonts for the project.

# Testing
### Validation Tools
These tools were used to test the validity of the code for this project:
- [W3C HTML Validator]( https://validator.w3.org/) was used to validate HTML.
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/) was used to validate CSS.
- [Pylint-django](https://pypi.org/project/pylint-django/) and [Microsofts Python Extension for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-python.python) was used to validate Python.

### Testing Matrix
A testing matrix was created using google spreadsheets. It details all of the tests to make sure the site is responsive and that each feature and compenent works on different screen sizes, devices, and browsers. The testing matrix can be found [here](https://github.com/isaacwoodruff/simplysportscience/blob/master/Testing_Matrix.pdf).

# Deployment
## Local Deployment
To run this project locally the following must be installed in your IDE:
- [Git](https://git-scm.com/downloads)
- [Python 3](https://www.python.org/downloads/)
- [PIP](https://pip.pypa.io/en/stable/installing/)

You have to set up free accounts with the following services for the site to function fully:
- [Stripe](https://stripe.com/)
- [Algolia Places](https://community.algolia.com/places/)
- [Gmail](https://accounts.google.com/signup/)

For information on how to set these up, you can explore their documentation in the links above.

### Instructions

1. Follow [this link](https://github.com/isaacwoodruff/simplysportscience/) to the main page of the Simply Sport Science repository.
2. On the right side of the page click the green **Clone or download** button.
3. In the '**Clone with HTTPS**' section, copy the URL for the repository.
4. Open your **terminal/Git Bash**.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type **git clone**, and then paste the URL that was copied in Step 3 or copy and paste this command:
    ```
    git clone https://github.com/isaacwoodruff/simplysportscience.git
    ```
    
7. Press **Enter**.
8. Create a virtual environment using Pythons built in virtual environment by entering the command(for Windows):
    ```
    python -m .venv venv
    ```
9. Activate the .venv with the command(for Windows):
    ```
    .venv\Scripts\activate 
10. Install all required modules from requirements.txt with the command:
    ```
    pip install -r requirements.txt.
    ```
11. Set up your environment variables. 

    - If you're using VSCode, locate the **settings.json** file in the .vscode directory and add your environment variables as below. Once saved you may have to restart VSCode to activate your environment variables: 

    ```json
    "terminal.integrated.env.windows": {
        "SECRET_KEY": "<enter key here>",
        "DEVELOPMENT": "1", # for development, dont include this in production
        "HOSTNAME": "<enter hostname url here>",
        "ALGOLIA_PUBLIC_KEY": "<enter key here>",
        "ALGOLIA_PUBLIC_APP_ID": "<enter key here>",
        "STRIPE_PUBLISHABLE": "<enter key here>",
        "STRIPE_SECRET": "<enter key here>",
        "ENDPOINT_SECRET": "<enter key here>",
        "EMAIL_HOST_USER": "<enter email here>",
        "EMAIL_PASS": "<enter app password here>",
    }

12. Migrate all the models to create your database tables with the terminal command(for windows):
    ```
    python manage.py migrate
    ```
13. To access the Django admin panel create a superuser with the following command(for windows):
    ```
    python manage.py createsuperuser
    ```
14. Now you can run the project locally with the command(for windows):
    ```
    python manage.py runserver
    ```
15. Click on the localhost link provided to navigate to the deployed site.

16. To access the admin panel type **/admin** at the end of the localhost URL.

#### Stripe Webhook Instructions
1. To use webhooks for local development you will need to use [ngrok](https://ngrok.com/) to create a public URL for your localhost. Follow their documentation in the link provided to set it up.

2. Assuming you created your Stripe account as suggested above navigate to your [Dashboard](https://dashboard.stripe.com/).

3. On the side bar to the left click on **Developer**, then in the submenu slick on **Webhooks**.

4. In the Endpoints section click on **Add endpoint**.

5. Enter the endpoint URL which will be:
    ```
    https://<your ngrok url here>/checkout/router/
    ```
6. From the **Events to send** dropdown menu navigate to, and click on, **checkout.session.completed**. 

7. Then click **Add endpoint** and enter your account password.

8. Once created navigate to **Signing secret** and click on **Click to reveal**.

9. Copy this key and put it as the value for your environment variable:

    ```json
    { "ENDPOINT_SECRET": "<enter signing secret key here>" }

10. Your Stripe Webhook is now set up to securely add credit to your users accounts.

#### Password Reset Feature Instructions
**Note:** These instructions are only for setting up a Gmail account to allow SMTP for the Password Reset feature.

1. In your Gmail navigate to your account settings or click [this link](https://myaccount.google.com/).

2. From the side menu to the left click on **Security**.

3. Navigate to the **Signing in to Google** section. If you have't got 2 step verification set up, click on **2 step verification** and follow the instructions to set it up.

4. Click on **App passwords**. From the **select app** dropdown menu select **Mail**. From the **select device** dropdown menu select **Other (Custom name)** and enter a name for your app. Then click generate.

5. Copy the password and put it into your environment variable:
    ```json
    { "EMAIL_PASS": "<enter app password here>" }

**Note:** Be careful not to leave out the spaces in this password as they dont get copied to your clipboard when you copy and paste.

## Heroku Deployment
1. In your terminal create a **requirements.txt** file using the command:
    ```
    pip freeze --local > requirements.txt
    ```

2. Then create a **Procfile** with the terminal command:
    ```
    echo web: gunicorn <your app name>.wsgi:application > Procfile
    ```

3. Commit your changes and push to GitHub with the terminal commands:
***Note:*** set your GitHub remote to origin if not done already```
    
    ```
    git add requirements.txt Procfile
    ```
    
    ```
    git commit -m "Your commit message"
    ```
    
    ```
    git push origin
    ```
    
3. Go to [Heroku](https://heroku.com/) and create a new app by clicking the **New** button in your dashboard. Set your app name and set the region to whichever is closest to you for optimum speed.

4. In the heroku dashboard navigate to **Installed add-ons** then click on **configure add-ons** next to it.

5. Search for **Postgres** in the Add-ons search box and select it from the list.

6. Select hobby-dev free model. Once set up you will have an environment variable in your config with the **DATABASE_URL**.

7. In the heroku dashboard of your application, click on **Deploy** then **Deployment method** and select GitHub.

8. Click confirm in the pop up window to link the heroku app to the GitHub repository.

9. In the heroku dashboard of your application, click on **Settings** then **Reveal Config Vars** and set the following:

| Key | Value |
--- | ---
HOSTNAME | `<your heroku app hostname>`
DATABASE_URL | `<your postgres database url>`
STRIPE_PUBLISHABLE | `<your public key>`
STRIPE_SECRET | `<your secret key>`
SECRET_KEY | `<your secret key>`
ALGOLIA_PUBLIC_KEY | `<your public key>`
ALGOLIA_PUBLIC_APP_ID | `<your secret key>`
ENDPOINT_SECRET | `<your secret signing key>`
EMAIL_PASS | `<your secret key>`
EMAIL_HOST_USER | `<your email address>`

10. In your IDE open up a terminal and start a heroku shell. Then migrate your database models and create a superuser account in your database.
    
    You can find more in depth instructions on how to do those tasks in the [heroku documentation](https://devcenter.heroku.com/articles/heroku-postgresql).

11. In the heroku dashboard of your app you can either click **Deploy** or enable **Automatic Deploys** in the **Automatic Deployment** section.

12. To pick your branch for manual deployment go to the **Manual Deploy** section and set the branch to **master** then click **Deploy Branch**.

13. After the build is complete you can navigate to the deployed site by clicking the **View app** button.

14. To access the admin panel type **/admin** at the end of the heroku app URL.

# Credits
### Content
- The text for the job postings on the site was taken from [Careers In Sport](https://careers-in-sport.co.uk/)
- All other content on the site was written by the developer.

### Media
- The banner image in the job search pages uses an image from [this location](https://www.pexels.com/photo/photo-of-people-doing-fist-bump-3184430/?fbclid=IwAR38WzHnwwOuL2VcxFMn879hwp7a81MHEk9mYuYkB5Bzj4K0mRpSADZuUUA)
- The background image for sign in/sign up pages uses an image from [this location](https://www.pexels.com/photo/woman-writing-on-a-notebook-beside-teacup-and-tablet-computer-733856/?fbclid=IwAR1O-2oPVI040el3QIC9nsV3SAqNAidZxRPIBkTcR-FGBJmIGj_ftF5I3d4)
- The background image for the employer & candidates pages uses an image from [this location](https://www.pexels.com/photo/photo-of-people-near-wooden-table-3184418/?fbclid=IwAR3jFa1w88s5IBy01lXtVE923ZYRgi2O0B9ZVM20ivUOdi-JX9ZBNvL-Mng)
- The background image for the edit profile & new job pages uses an image from [this location](https://www.pexels.com/photo/adult-blur-books-close-up-261909/)
- The favicon for this site is take from [Flaticon](https://www.flaticon.com/free-icon/gym_755298)

### Code
- Code for in the @receiver function for the user profiles was modified from a blog post by [SimpleIsBetterThanComplex](https://simpleisbetterthancomplex.com/tutorial/2016/11/23/how-to-add-user-profile-to-django-admin.html)
- The [William Vincent](https://wsvincent.com/django-slug-tutorial/) helped me understand how to use slugs with absolute urls
- The CSS gradient for the instagram icon was taken from [Brand Gradients](http://www.brandgradients.com/instagram-colors/)

### Acknowledgements
- [Corey Schafers](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p) youtube [Django Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p) helped me a lot in my understanding of Django.
- Thanks to [Aaron Sinnott](https://github.com/aaronsnig501) for his help and suggestions throughout the project
- [SlackOverflow](https://stackoverflow.com/) was invaluable for understanding issues and bugs throughout the development of the project
