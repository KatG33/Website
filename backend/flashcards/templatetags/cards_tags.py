#  imports Django’s template module
from django import template
# # imports your Card model and the BOXES variable.
from flashcards.models import BOXES, Flashcard
# Creates an instance of Library used for registering your template tags.
register = template.Library()
# Uses the Library instance’s .inclusion_tag() as a decorator. This tells Django that boxes_as_links is an inclusion tag.
@register.inclusion_tag("flashcards/box_links.html")
def boxes_as_links():
    boxes = []
    for box_num in BOXES:
        card_count = Flashcard.objects.filter(box=box_num).count()
        # append a dictionary with the box number as key and the number of cards 
        # in the box as the value to the boxes list.
        boxes.append({
            "number": box_num,
            "card_count": card_count,
        })

    return {"boxes": boxes}
