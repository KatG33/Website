## Project Overview:
This is a full-stack flashcard web app built with React (frontend) and Django (backend). Users can create, view, and manage flashcards.
I based this project on the tutorial from Real Python – Build a Flashcard App With Django: https://realpython.com/django-flashcards-app/.

### This project utilises:
1. Django models to define flashcards in the database
2. Django views to handle user actions like adding or deleting cards
3. Django templates to render HTML pages
4. Static CSS files to style the site
5. SQLite as the database (default for Django)

### This project helped me to learn:
1. How Django’s URL routing works
2. How to use templates and context variables
3. How to link CSS styles from the static/ folder
4. How to use the admin panel for easy flashcard management


## How to Run This Project:
1. Download the Project 
2. Navigate to the backend folder via 'cd backend' command
3. Create and activate a virtual environment via commands:
'python -m venv venv' and then
 'source venv/bin/activate'
 OR if using Windows
 venv\Scripts\activate

5. Run migrations:
python manage.py migrate

6. Start the development server:
python manage.py runserver

7. Visit the app in your browser:
http://127.0.0.1:8000/


```
Unlike the previous version of the website's structure, I don't need a separate -server/ folder,
Because Django is a full-stack framework, it already contains server functionality in its framework.

Potential Project Structure v0.2:
project-folder/
├── frontend/       # Everything that related to the part of the website interacted with and seen by the user
│   ├── public/     # For HTML, CSS, images, icons files that will be shown on the website
│   │   ├── index.html  # Main HTML file that tells user's browser WHAT to show
│   │   ├── styles.css   # Global CSS styles, like colors and fonts
│   │   └── images/      # Images and icons
│   ├── src/        # For JavaScript and React components, which are building blocks of the website
│   │   ├── components/ # Reusable React components
│   │   │   ├── FlashcardList.js  # Component to display flashcards
│   │   │   ├── FlashcardAdd.js   # Component to add new flashcards
│   │   │   └── ...   # Other components
│   │   ├── App.js    # Main part of websie, where everything is tied together
│   │   ├── index.js  # Entry point for React, aka sene in movie that sets everything in motion
│   │   └── api.js    # Functions to handle API requests to Django, it helps website communicate with backend server
│   ├── package.json  # React project configuration, keeps track of all tools and libraries
│   └── .gitignore    # Files to ignore for version control, so they don't get mixed up in project history
├── backend/          # Django application, everything that user doesn't see. It handles data and business logic.
│   ├── manage.py     # Django control and management script for the project. I don't fully understand its functionality yet, but it allows for such actions as like starting the server, creating apps, or running database migrations..
│   ├── backend/      # Django project files
│   │   ├── __init__.py     # This is a folder for Python package. Signals to Python that his folder has modules that can be imported and used in other parts of the program
│   │   ├── settings.py # Settings and configurations for Django project
│   │   ├── urls.py     # URL routing for the project and website, it tells Django what to do when someone visit's a specific page
│   │   └── wsgi.py     # WSGI configuration for deployment, helps Django to communicate with web server for deployment.
│   ├── flashcards/   # Django app for handling flashcards
│   │   ├── migrations/ # Database migrations for flashcards, helps manage changes to the database
│   │   ├── admin.py   # Admin interface settings and design
│   │   ├── models.py  # Database models for flashcards, blueprint for flash cards
│   │   ├── serializers.py # Serializers for API, converts data between different formats, for example: turning a flashcard into JSON to send to the frontend
│   │   ├── urls.py    # URL routing for flashcard API, tells Django how to handle flashcards requests
│   │   ├── views.py   # Views for handling requests and returning responses for user's requests. 
│   │   └── tests.py   # Tests for flashcards app to make sure everything works as intended
├── db/              # For database models or scripts-related files, which store all the data used in the application
│   ├── db.sqlite3    # This is the actual database file (if you’re using SQLite). It’s where all the flashcard data is stored
│   ├── seed.py       # Script to seed database with initial data (optional)
└── .gitignore       ## Files to ignore for version control, so they don't get mixed up in project history


I am utilizing such dependencies as React for frontend and Django for backend. 
The reasons why I choose Django Python for backend and React JavaScript for frontend: 
    1.  This is a small to medium project that hasn't been fully planned out yet. 
        Due to the fact that Django has plenty of built-in functionalities, it allows for fast and flexible development, 
        enabling me to quickly adapt to additional ideas and changing requirements. 
    2.  Django has bre-build Authentication and such Security features as password encryption and data access control, 
        which is a good start for a beginner web developer who does not know how to implement those features from scratch. 
    3.  Django does not utilize SQL for databases, but instead uses ORM. ORM has much easier syntax and implementation than SQL.
    4.  Both Django and React use popular and easy-to-learn languages. I am already familiar with Python.
    5.  Both React and Django have great modularity which permits to reuse the code. 
        This will make the management and debugging of smaller components of the application much easier.
