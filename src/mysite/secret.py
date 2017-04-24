import tweepy
#Twitter Auth
consumer_key = 'whcSTlT8Z1Sq6jalVojqWDSAP'
consumer_secret = 'ivxRvCBbcHejLNLCDu69CL6lyb6pnCyN5u92Xbdh3hzZl8vPXL'
access_token = '851283766865571840-L60bKmCM7tqkuFy9dwTD3Py8RrX5rWv'
access_token_secret = 'YfsBAeLzNbWIrGZ4KWWVMNZFagATpX2pgYe7NqDr1CcxA'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter = tweepy.API(auth)
