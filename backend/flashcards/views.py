# Module below supposed to ccombine HTML with the data and return HTTP response
from django.shortcuts import render

# A decorrator that defines allowed HTTP methods, determines functions like GET and/or POST
from rest_framework.decorators import api_view
# 'import Response' sends data back as an HTTP response
from rest_framework.response import Response
# converts Flashcard model and data into JSON format
from .serializers import FlashcardSerializer
# 'ListView' is a tool in Django that can show a list of items
# 'CreateView' is CreateView can: automatically generate form, handle validations, create object and redirect
from django.views.generic import (ListView,CreateView,UpdateView,)
# Imports flashcards' model and lets us interact with the object Flashcard
from .models import Flashcard
# 'reverse': This tool looks up the web address right away when you ask for it.
# 'reverse_lazy' module waits to look up the web address until it's actually needed. 
from django.urls import reverse_lazy

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

class ViewFlashcards(ListView):
    model = Flashcard
    # Sorting order set is: first by the number of the box, and then by the earliest date cof creation
    queryset = Flashcard.objects.all().order_by("box", "-date_created")
    # I have to specify the path to the flashcard template, so DJANGO STOPS FUCKING LOSING IT
    # template_name = "flashcards/listOfCards.html" 

class FlashcardCreateView(CreateView):
    model = Flashcard
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("flashcard-create")
    
class FlashcardUpdateView(FlashcardCreateView, UpdateView):
    success_url = reverse_lazy("flashcard-list")
    
class BoxView(ViewFlashcards):
    template_name = "flashcards/box.html"

    def get_queryset(self):
        return Flashcard.objects.filter(box=self.kwargs["box_num"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        return context