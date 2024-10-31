# The module below provides access to database package
# Classes and packages, needed to create a database
from django.db import models
# Create your models here.
# (models.Model) tells Django that this class represents a database table
# Django will automatically create a table in a database 
# to store instances of this class
class Flashcard(models.Model):
    # This initialises fields that will store questions, 225 char max
    question = models.CharField(max_length=255)
    # Creating attribute answer in Flashcards class
    # This also will be initialised as another column in the database to store answers
    answer = models.TextField()
    # This method will be called when conversion of an Obj to String is required
    def __str__(self):
        return self.question

