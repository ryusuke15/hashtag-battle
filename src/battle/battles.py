import unicodedata
from enchant.checker import SpellChecker
from mysite.secret import twitter
from django.db.models.signals import post_save
from .models import Match, Tweet, now

check = SpellChecker("en_US")

def start_battle(search):
    
    hashtag_list =[]
    hashtag_list.append(search.hashtag_1)
    hashtag_list.append(search.hashtag_2)

    matchId = Match.objects.get(id=search.id)

    for tag in range(0, len(hashtag_list)):
        data = twitter.search(hashtag_list[tag])

        for tweet in range (0,len(data)):
            text = data[tweet].text
            tweet_id = data[tweet].id   
            word_list = text.split()
            prefixes = ('@','#','http','https')
            filtered = [ v for v in word_list if not v.startswith(prefixes) ]
            new_text = ' '.join(filtered)
            check.set_text(new_text)
            err_list = []
            for err in check:
                err_list.append(err.word)        

            typo_score = (len(err_list))  

            if not Tweet.objects.filter(twitter_id = tweet_id).exists():

                tweet_data = Tweet(hashtag_search = hashtag_list[tag], 
                                   match = matchId,
                                   twitter_id = tweet_id,
                                   score = typo_score)    
                tweet_data.save()

def check_status(h1_score, h2_score, end_time, hashtag_1, hashtag_2):
    if end_time > now:
        if h1_score > h2_score:
           status = hashtag_1 +" is winning."
        elif h1_score < h2_score:
            status = hashtag_2 + " is winning."
        else:
             status = "Tied"
    elif end_time < now:
        if h1_score > h2_score:
           status = hashtag_1 +" won."
        elif h1_score < h2_score:
            status = hashtag_2 + " won."
        else:
             status = "Draw"
    return status


def check_battle():
    match = Match.objects.all()
    for instance in range(0, len(match)):
        if match[instance].end_time > now:
           start_battle(match[instance]) 

