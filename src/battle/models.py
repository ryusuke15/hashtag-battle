from __future__ import unicode_literals
import pytz
from django.utils import timezone
from datetime import datetime, timedelta
from django.db import models
from pprint import pprint

utc = pytz.UTC
now = utc.localize(datetime.now())

class Match(models.Model):
    name = models.CharField(max_length=100)
    hashtag_1 = models.CharField(max_length=100)
    hashtag_2 = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField() 
     
class Tweet(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    hashtag_search = models.CharField(max_length=100)
    twitter_id = models.IntegerField()
    score = models.IntegerField()
