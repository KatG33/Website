# The module below provides access to database package
# Classes and packages, needed to create a database
from django.db import models
# Create your models here.

# The global variables below are the Leiner's boxes.
# Each of the boxes are associated with a certain frequency of how often
# The flashcard box should pop out for a review
NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

# (models.Model) tells Django that this class represents a database table
# Django will automatically create a table in a database 
# to store instances of this class
class Flashcard(models.Model):
    # This initialises fields that will store questions, 225 char max
    question = models.CharField(max_length=200)
    # Creating attribute answer in Flashcards class
    # This also will be initialised as another column in the database to store answers
    answer = models.TextField(max_length=300)
    # In class Flashcard, the box attribute is initialise as an IntegerField(). It means this function accepts only integers as parameters. 
    # Setting default parameter 'default=1' makes sure that every time a new flashcard is created, it automatically assigned to box #1. 
    # box = models.IntegerField(default=1)
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    # The date_created attribute automatically records the date and time when a new Card is created with 'auto_now_add=True' command. 
    date_created = models.DateTimeField(auto_now_add=True)
    # Category field, so students can organise their flashcards by category
    # Because we are utilising 'blank=True' parameter, it makes category field optional
    category = models.CharField(max_length=100, blank=True)

    # This method will be called when conversion of an Obj to String is required
    def __str__(self):
        return self.question
    
    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]

        if new_box in BOXES:
            self.box = new_box
            self.save()
        return self

