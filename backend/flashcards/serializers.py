# The purpose of a serializer is to automatically convert complex data types like Django models
# into something similar to JSON format that can be easily used by API


# Utilising Django REST Framework's provided serialiser
from rest_framework import serializers
# Imports Flashcard models that we have prepared earlier
from .models import Flashcard

# Creating a new serialiser for Flashcards based on 'ModelSerialiser'
# It automatically provides fields and validation rules
class FlashcardSerializer(serializers.ModelSerializer):
    # Nested class that specifies what model and fields to include into function
    class Meta:
        model = Flashcard
        # We could also specify specific fields by listing them
        fields = '__all__'
        