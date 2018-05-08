
import json 
import tweepy

consumer_key = "evHVYPKDjAJ0JAitpY49z7KJ4"
consumer_secret= "MpG65nQZOuf0ErIyEtaUDPA0J8aI2qIdGRcbeLmgIpXuOXbCKM"
access_token="979169626012631041-vEFBfFZ1FCam3j9lRdqcMwn27aA2puX"
access_token_secret="I1AJRehHaXYZbfuYs1x64hVth0nzKALMhMLxOjU2pkSmN"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api= tweepy.API(auth, parser=tweepy.parsers.JSONParser())

target_user = "realDonaldTrump"

public_tweets= api.user_timeline(target_user)

for tweet in public_tweets:
    print(json.dumps(tweet, sort_keys=True, indent=4, separators=(',', ': ')))

