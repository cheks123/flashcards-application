from django import template
from cards.models import BOXES, Card

register = template.Library()

@register.inclusion_tag("cards/box_links.html")
def boxes_as_links():
    boxes = []
    for box_number in BOXES:
        card_count = Card.objects.filter(box=box_number).count()
        boxes.append({
            "number": box_number,
            "card_count": card_count,
        })
    return {"boxes": boxes}