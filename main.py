import tweepy
import os

consumer_key = os.environ["Twitter_Api"]
consumer_secret = os.environ["Twitter_Api_secret"]
access_token = os.environ["Twitter_access"]
access_token_secret = os.environ["Twitter_access_secret"]


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


api.update_status("@corner1705 *slap*")