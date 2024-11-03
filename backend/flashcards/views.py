# Module below supposed to ccombine HTML with the data and return HTTP response
from django.shortcuts import render
# Imports flashcards' model and lets us interact with the object Flashcard
from .models import Flashcard
# A decorrator that defines allowed HTTP methods, determines functions like GET and/or POST
from rest_framework.decorators import api_view
# 'import Response' sends data back as an HTTP response
from rest_framework.response import Response
# converts Flashcard model and data into JSON format
from .serializers import FlashcardSerializer
# Create your views here.
# Argument request is a HTTP request from the browsed, Passed as a paramether, handles request to flashcards,
# rendering HTML for the flashcards view
def flashcard_list_html(request):
    # ATTENTION! This is where Django's ORM is utilised if u wanted an example of that
    flashcards = Flashcard.objects.all()  # Get all flashcards
    # 'flashcards/flashcard_list.html': Specifies the path to the HTML code that is used to show flashcards
    # Notice, that the dictionary is utilised 
    # To connect key 'flashcards' to the list of flashcard objects fetched from the database 
    return render(request, 'flashcards/flashcard_list.html', {'flashcards': flashcards})

# The line before, called decorator, specifies that THIS view will only accept GET requests.
@api_view(['GET'])
# The function below utilises a decorator to return JSON data with the help of the Django REST Framework for the API.
def flashcard_list(request):
    flashcards = Flashcard.objects.all()
    # The line below will pass a list of flashcards to FlashcardSerializer with many=True, with multiple instances at once
    serializer = FlashcardSerializer(flashcards, many=True)
    # Returns the serialized data as a JSON response to the client
    return Response(serializer.data)