from django.db.models.signals import post_save, post_delete
from battles import start_battle
from .models import Match, Tweet

# Create Match
def create_match(sender, instance, **kwargs):

    start_battle(instance)

post_save.connect(create_match, sender=Match)
