# GamerConnect

![Gamer-Connect-Logo](https://github.com/JamieB92/Gamer-Connect-Backend-PP4/assets/117354147/e4e36b51-8241-4e63-a082-cbd723366145)

Welcome to GamerConnect, the ultimate social media platform for gamers!

GamerConnect is a dynamic and inclusive platform designed for gamers of all ages and backgrounds. Whether you're a seasoned pro or just starting your gaming journey, our platform is tailored to bring the gaming community together.

This is the Backend Repo for the project please click [here](https://github.com/JamieB92/Gamer-Connect-Frontend-PP4) for the frontend repo.

## Features
- Game Clips & Screenshots: Share your gaming triumphs, epic moments, and funniest fails with our intuitive media uploading features.

- Likes & Follows: Connect with fellow gamers, support their content with likes, and build your own dedicated following.

- Find Gamers: Discover like-minded players and create lasting gaming partnerships. Find friends to join you in your gaming adventures!

## Why GamerConnect?
- Community-First Approach: GamerConnect puts the community at the heart of everything we do. We're all about creating connections, friendships, and epic gaming memories.

- User-Friendly Interface: Our platform is designed with simplicity in mind, ensuring an easy and enjoyable experience for users of all levels.

- Diverse Gaming Experience: No matter your preferred platform, genre, or style, you'll find a welcoming and diverse community here.

## How to Get Started
- Sign up for a GamerConnect account.
- Customize your profile with your favorite games, gaming interests, and a profile picture.
- Start uploading your game clips, screenshots, and engage with the gaming community.
- Connect with other gamers, follow your favorite content creators, and make new gaming buddies.
- Join the Community
- GamerConnect is not just a platform; it's a gaming family waiting to welcome you. Start your gaming journey, connect with fellow players, and level up your social gaming experience today.

## Feedback and Contributions
- We welcome your feedback and contributions to make GamerConnect even better. Feel free to report issues, suggest improvements, and contribute to our open-source development.


# User Stories

## Epic 1 - Post Sharing & Interaction:

### Create Gaming Posts: 
As a GamerConnect user, I aim to share my gaming experiences by crafting posts containing clips and images, facilitating connections with the gaming community.

### View All Posts:
As a GamerConnect user, I wish to scroll through all the latests posts on the site

### View Post Details: 
As a GamerConnect user, I want to check out individual posts to learn more about interesting gaming posts.

## Epic 2 - Content Discovery & Engagement:

### Show Appreciation: 
As a GamerConnect user, I want to show my liking for interesting posts to express support.

### Keyword-Based Search: 
As a GamerConnect user, I aim to search for posts and user profiles using keywords to find content and gamers matching my interests.

### Review Liked Posts: 
As a GamerConnect user, I want a straightforward way to revisit posts I've liked, making it easy to relive favorite gaming moments

## Epic 3 - Post-Specific Interactions:

### Post Editing Privileges: 
As a post owner on GamerConnect, I aim to have control over the editing of my post title and description to ensure accuracy and updates.

### Active Commenting: 
As a GamerConnect user, I intend to contribute to post discussions by adding comments, allowing me to share thoughts and engage with fellow gamers.

### Comment Control: 
As the owner of a comment, I wish to have the capability to delete and edit my comments, allowing me to manage the content within the application.

## Epic 4 - User Profiles & Connections:

### New Account Creation:
As a GamerConnect user, I intend to establish a fresh account to access all the privileges available to registered gamers.

### User Profile Viewing:
As a GamerConnect user, I want to check out fellow gamers' profiles to explore their gaming posts and learn more about their gaming experiences.

### User Following & Unfollowing: 
As a GamerConnect user, I want to be able to follow and unfollow other gamers.

### Profile Customization: 
As a GamerConnect user, when logged in, I want to personalize my gaming identity by changing my profile picture and updating my bio.

## Epic 5 - Developer 

### Initial Backend Setup
As a developer, I need to set up the backend project structure for seamless project development.

### Initial Frontend Setup
As a developer, I must configure the frontend project structure to facilitate project development.

### Deploy Backend
As a developer, I need to guarantee the successful deployment of the project's backend for site accessibility.

### Deploy Frontend
As a developer, I must ensure the successful deployment of the project's frontend for users to interact with.

### Database Setup
As a developer, it's crucial to create a database and integrate it into the project for effective information storage.

## Design

#### Colors
![color-palete](https://github.com/JamieB92/Gamer-Connect-Backend-PP4/assets/117354147/4c72a043-a4e3-49ba-b583-5ec8cf4a4c46)

#### Font
Google Font - Lexend


 # Deployment And Setup 
Here you can find the instructions to recreate the project from scrath with setup and deployment instructions

## Backend API Setup

### Github
- In the top right of the page click the plus symbol
- Click New Repository
- Select Template - Code-Institute-Org/gitpod-full-template
- Name the repository (Reference Backend)
- Click Create

### Gitpod (Please use Chrome or Firefox)
- open a new tab in your browser and go to your browsers extensions store
- Search for Gitpod
- Install Gitpod extension
- Go back to your newly created repo
- Click the Green Gitpod Open button
- Click Continue with Github 
- Gitpod will now create a workspace 

### Django and Django Rest Framework Setup
- In your IDE open a new terminal
- Enter in the terminal pip3 install 'django<4'
- Enter in the terminal django-admin startproject {{project_name}} .
- Enter in the terminal to create an App with - python manage.py startapp {{app_name}}
- Add the new app to the allowed apps in the settings.py file.
- Enter in the terminal - pip install djangorestframework
- Now go to settings.py and add 'rest_framework' to installed apps.
- Enter in the terminal pip install django_filter
- Now go to settings.py and 'django_filers' to installed apps.
- pip freeze > requirements.txt



### Cloudinary and Pillow
- Go to Cloudinary - https://cloudinary.com/
- Create an account
- Click dashboard
- Copy your cloudinary API Environment variable
- Install Cloudinary in the terminal with - pip install django-cloudinary-storage
- pip install django-cloudinary-storage[video]
- Install Pillow in the terminal with - pip install Pillow
- Now go to settings.py in your project 
- In installed apps add 'cloudinary_storage' above 'django.contrib.staticfiles' and 'cloudinary' below.
- create an env.py file in the top directory
- add your cloudinary API Environment variable to the env.py file
- add the following to settings.py underneath "from pathlib import Path":
        
        import os

        if os.path.exists('env.py'):
            import env

        CLOUDINARY_STORAGE = {
            'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
        }
        MEDIA_URL = '/media/'
        DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


### dj_rest_auth
- run the following in the terminal - pip3 install dj-rest-auth==2.1.9
- Add the following in INSTALLED_APPS in settings.py:

        'rest_framework.authtoken',
        'dj_rest_auth',

- Add the following in the main app (gamer_connect_api) urls.py: 

        path('dj-rest-auth/', include('dj_rest_auth.urls')),

- Now migrate the db with  python manage.py migrate
- run the following in the terminal - pip freeze > requirements.txt

### All Auth
- run the following in the terminal -  pip install 'dj-rest-auth-[with_social]'
- got to INSTALLED_APPS and add the following:

        'django.contrib.sites',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'dj_rest_auth.registration',

- Underneath INSTALLED_APPS add:

        SITE_ID = 1

- Add the following in the main app (gamer_connect_api) urls.py:     

        path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
- run pip freeze > requirements.txt 

### JWT Tokens
- Run the following in the terminal - pip install djangorestframework-simplejwt
- add DEV to env.py
- Add the following in settings.py under BASE_DIR :

        REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': [(
                'rest_framework.authentication.SessionAuthentication'
                if 'DEV' in os.environ
                else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
            )]
        }

- Again in setting.py add the following under REST_FRAMEWORK : 

        REST_USE_JWT = True
        JWT_AUTH_SECURE = True
        JWT_AUTH_COOKIE = 'my-app-auth'
        JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
        
        REST_AUTH_SERIALIZERS = {
            'USER_DETAILS_SERIALIZER': 'gamer_connect_api.serializers.CurrentUserSerializer'
        }
- Create serializers.py and create dj_rest_auth
- python manage.py migrate
- run pip freeze > requirements.txt 

## Deployment 





### ElephantSQL(Database):
- Navigate to https://www.elephantsql.com/
- Click Login/Creat a account.
- Click "Create New Instance".
- Create a name for the instance.
- Select Tiny Turtle.
- Leave Tags empty and click "Select Region".
- Select your region.
- Click Review in the bottom right corner.
- Click Create instance.
- Click on your newly created instance.
- Copy the URL of the instance.
- Go to Heroku 
- Click on settings and reveal config vars
- set the key as DATABASE_URL and paste in the url in the value :

       [DATABASE_URL]   [postgres://xxxxxxxxxxxxxxxxxxxxx]

- Now go back to your IDE 
- Run pip3 install dj_database_url==0.5.0 psycopg2 in the terminal
- go to settings.py and import dj_database_url underneath the import for os

        import os
        import dj_database_url
- Still in settings.py update the DATABASES section with the following: 

        if 'DEV' in os.environ:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }
        else:
            DATABASES = {
                default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
            }

- add you db url to env.py :

        os.environ['DATABASE_URL'] = "<your PostgreSQL URL here>"

- Temporarly comment out DEV so that the external db can connect to your IDE
- Go back to settings.py and add a print satement at the bottom of the database if else statement:

        
        if 'DEV' in os.environ:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }
        else:
            DATABASES = {
                default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
            }
            print("connected")

- -–dry-run your makemigrations with following in the terminal:

    python3 manage.py makemigrations --dry-run

- if succesful connection is made you should see connected in the terminal
- Remove print statement
- Run python3 manage.py migrate
- Create yourself a super user for the database by running - python3 manage.py createsuperuser
- Follow the steps to create your superuser username and password
- Confirm this has been added by going back to Elephantsql
- click on your instance 
- select browser in the left navigation
- Click the table queries and select auth_user
- When you click execute you should now see your new superuser

### IDE Setup For Deployment: 

- In the terminal of your IDE run - pip3 install gunicorn django-cors-headers
- Run in the terminal - pip freeze --local > requirements.txt
- Create a Profile in the top level of the project (Needed for Heroku)
- Add the following to the Procfile: 

        release: python manage.py makemigrations && python manage.py migrate
        web: gunicorn drf_api.wsgi

- Go to settings.py and take your Heroku app's URL and add to ALLOWED_HOSTS

        ALLOWED_HOSTS = ['localhost', '{{your_app_name}}.herokuapp.com']
- Add corsheaders to INSTALLED_APPS underneath dj_rest_auth.registration

        INSTALLED_APPS = [

            'dj_rest_auth.registration',
            'corsheaders',
        ]

- Add corsheaders middleware to the TOP of the MIDDLEWARE

            SITE_ID = 1
            MIDDLEWARE = [
                'corsheaders.middleware.CorsMiddleware',
                ...
            ]
- Under the MIDDLEWARE list, set the ALLOWED_ORIGINS for the network requests made to the server with the following code:

            if 'CLIENT_ORIGIN' in os.environ:
                CORS_ALLOWED_ORIGINS = [
                    os.environ.get('CLIENT_ORIGIN')
                ]
            else:
                CORS_ALLOWED_ORIGIN_REGEXES = [
                    r"^https://.*\.gitpod\.io$",

- Enable sending cookies in cross-origin requests to allow users to use authentication.

            else:
                CORS_ALLOWED_ORIGIN_REGEXES = [
                    r"^https://.*\.gitpod\.io$",
                ]

            CORS_ALLOW_CREDENTIALS = True


- Set the JWT_AUTH_SAMESITE attribute to 'None' to allow the front end and the API to talk between different platforms
            
            JWT_AUTH_COOKIE = 'my-app-auth'
            JWT_AUTH_REFRESH_COOKE = 'my-refresh-token'
            JWT_AUTH_SAMESITE = 'None'

- Remove the default SECRET_KEY and replace with the following to use env.py

            SECRET_KEY = os.getenv('SECRET_KEY')
    
- Create a NEW value for your SECRET_KEY environment variable and add it to env.py file:

            os.environ.setdefault("SECRET_KEY", "YourNewKey")


- Set DEBUG to be True only if the DEV environment variable exists.

            DEBUG = 'DEV' in os.environ

- Comment DEV back in env.py

- Run - pip freeze --local > requirements.txt
- Add, Commit & Push to Github





# Bugs and Testing 

You can find all the bugs and testing in the following files:

GamerConnect [Backend](https://github.com/JamieB92/Gamer-Connect-Backend-PP5/blob/main/bugs_and_testing_backend.md)