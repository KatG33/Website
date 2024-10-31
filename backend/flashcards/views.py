# Module below supposed to ccombine HTML with the data and return HTTP response
from django.shortcuts import render
# Imports flashcards' model and lets us interact with the object Flashcard
from .models import Flashcard
# Create your views here.
# Argument request is a HTTP request from the browsed 
# Passed as a paramether
def flashcard_list(request):
    # ATTENTION! This is where Django's ORM is utilised if u wanted an example of that
    flashcards = Flashcard.objects.all()  # Get all flashcards
    # 'flashcards/flashcard_list.html': Specifies the path to the HTML code that is used to show flashcards
    # Notice, that the dictionary is utilised 
    # To connect key 'flashcards' to the list of flashcard objects fetched from the database 
    return render(request, 'flashcards/flashcard_list.html', {'flashcards': flashcards})