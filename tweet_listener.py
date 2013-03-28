# coding: utf-8
import tweetstream
import simplejson as json
import sys
import re
import tweepy
from config import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#Commented code is for setting up the app for the first time
# auth_url = auth.get_authorization_url()
#print 'Please authorize: ' + auth_url
#verifier = raw_input('PIN: ').strip()
#auth.get_access_token(verifier)
#print "ACCESS_KEY = '%s'" % auth.access_token.key
#print "ACCESS_SECRET = '%s'" % auth.access_token.secret
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


try:
    with tweetstream.FilterStream(TWITTER_USERNAME, TWITTER_PASSWORD,
                                  track=SEARCH_WORDS) as stream:
        """
        streaming api which pulls all the tweets with the given words in them
        """
        for tweets in stream:
            tweet = json.loads(str(json.dumps(tweets)))
            twitter_post_id = tweet["id_str"]
            screen_name = tweet["user"]["screen_name"]
            uid = tweet["user"]["id"]
            user_name = tweet["user"]["name"]
            print user_name
            if user_name != TWITTER_USERNAME:
                userobject = api.get_user(uid)
                userobject.follow()
except tweetstream.ConnectionError, e:
    print "Disconnected from twitter. Reason:", e.reason

