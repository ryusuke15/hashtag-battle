from __future__ import unicode_literals
from django.contrib import admin
from forms import MatchForm
from .models import Match 

class MatchAdmin(admin.ModelAdmin):
    form = MatchForm
    list_display = "name","hashtag_1", "hashtag_2", "start_time", "end_time"


admin.site.register(Match, MatchAdmin)
