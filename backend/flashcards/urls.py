# This module allows to define URL pattern in Django application 
from django.urls import path
# This module contains logic for handling requests and returning responses for the app Flashcards
from . import views
# The list below contains URL patters Django project needs to recognise.
# Each URL provides an address to view a function that manages the request
urlpatterns = [
# '' - means that this pattern corresponds to the root URL of the program: http://127.0.0.1:8000/flashcards/
# 'views.flashcard_list' - indicates that when user visits the URL,
#   Django supposed to call the flashcard_list function defined in the views module and processes request.
# name='flashcard_list' - assigns a name to this URL pattern
    path('', views.flashcard_list, name='flashcard_list'), 
]