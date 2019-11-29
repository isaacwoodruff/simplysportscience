# Simply Sport Science
[Simply Sport Science](#https://simplysportscience.herokuapp.com/) was created as a job board to connect employers and candidates in the area of sport science.

[![Build Status](https://travis-ci.org/isaacwoodruff/simplysportscience.svg?branch=master)](https://travis-ci.org/isaacwoodruff/simplysportscience)

## Table of Contents

1. [UX](#ux)
    - [Goals](#goals)
        - [Business Goals](#business-goals)
        - [Employer Goals](#employer-goals)
        - [Candidate Goals](#candidate-goals)
    - [User Stories](#user-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)

3. [Information Architecture](#information-architecture)

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
- Create an efficient service to help the sport science community connect with employers/employees they want
- Monetize the job board by offering job posting packages to potential employers

The target audiences for this website are:
- Employers in the area of sport science
- Candidates in the area of sport science

### Employer Goals
The goals of employers on the website are to:
- Gain good exposure to the right candidates
- Find a selection of quality candidates for job openings in their organisation
- Have a dashboard to easily manage all their job posts

### Candidate Goals
The goals of candidates on the website are to:
- Easily find the jobs they want in the area of sport science
- Quickly apply to jobs
- Get alerts when new jobs get posted

## User Stories

## Design Choices

## Wireframes
The following wireframes were designed with Balsamiq.

Desktop View
- [Jobs Search Page](https://ibb.co/bvJbY9G)

Mobile View
- [Jobs Search Page](https://ibb.co/hdb58TG)

# Features
## Existing Features
##### Job Search
- The main component is the search feature for finding all jobs on the website with options to:
    - Filter by job title, location, type of employment (full time, part time, etc.)
- The search features an autocomplete for job titles that pulls job titles from the database and suggest them to the user. This uses jQuery UI 
- The search also makes use of Algolia Places API in the location input to autocomplete city names from all over the world
- Paginated results with 10 posts per page
- The amount of days ago the job was posted
- Posts containing job title, employement company, employment type, location
- Each company name, location, and employment type is a tag that can be clicked to search for all jobs relating to the tag
- A minimalist, professional design

##### Employers Page
- A list of reasons why employers would benefit from posting listings on the website
- An option to sign up as an employer
- If a candidate is viewing the page they also have an option to sign up as a candidate

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
- Has a link at the button to sign up if the user hasn't got an account
- Has a forgot password option

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
- Next to the post job button the amount of credits they have is displayed
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
    - Links to career advise articles on the blog

##### Miscellaneous Features
- Set alerts for a specific search parameter *e.g. biomechanist jobs in New York, US.*
- Save jobs to favourites list. If user hasn't got an account this leads to them signing up to use this feature
- Newsletter of newest jobs, and industry specific career advise
- Easy one click applications (by uploading CV or filling out profile on signup)

# Information Architecture

#### Users Collection

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
- [SQlite3](https://www.sqlite.org/index.html) as the database for development environment, provided by django.

### Libraries
- [JQuery](https://jquery.com) to simplify HTML DOM tree traversal and manipulation, event handling, and Ajax.
- [JQuery UI](https://jqueryui.com/) to enables users to quickly find and select from a pre-populated list of values as they type, leveraging searching and filtering.
- [Bootstrap](https://www.bootstrapcdn.com/) CSS Framework was used to develop responsive and mobile-first pages more easily.
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) a font and icon toolkit based on CSS used to provide icons for the project.
- [Google Fonts](https://fonts.google.com/) to provide and style fonts for the project.

# Testing
### Validation Tools

### Testing Matrix

# Deployment
## Local Deployment

### Instructions

## Heroku Deployment

# Credits
### Content

### Media

### Code

### Acknowledgements
- Thanks to [Aaron Sinnott](https://github.com/aaronsnig501) for his help and suggestions throughout the project
