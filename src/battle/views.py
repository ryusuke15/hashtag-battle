from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.core import serializers
from battles import check_status
from .models import Match, Tweet

def single_battle(request, id):
    match = get_object_or_404(Match, pk=id)
    name = match.name
    hashtag_1 = match.hashtag_1
    hashtag_2 = match.hashtag_2
    start_time = match.start_time
    end_time = match.end_time

    tweets = Tweet.objects.filter(match_id=id)
    h1_score = 0
    h2_score = 0

    for tweet_list in range(0, len(tweets)):
        if tweets[tweet_list].hashtag_search == hashtag_1:
            h1_score += tweets[tweet_list].score
        else:
            h2_score += tweets[tweet_list].score

    status = check_status(h1_score, h2_score, end_time, hashtag_1, hashtag_2)

    data = {
        'battle_name': name,
        'hashtag_1':{'title': hashtag_1, 'score': h1_score},
        'hashtag_2':{'title': hashtag_2, 'score': h2_score},
        'start_time': match.start_time,
        'end_time': match.end_time,
        'status': status
    }
 
    return JsonResponse(data, safe=False)
