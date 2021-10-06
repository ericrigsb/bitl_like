import os
import tweepy
import time
import logging
from dotenv import load_dotenv

# API key
API_KEY = os.getenv('API_KEY')
# API secret key
API_SECRET = os.getenv('API_SECRET')
# Access token
KEY = os.getenv('KEY')
# Access token secret
SECRET = os.getenv('SECRET')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
auth = tweepy.OAuthHandler("API_KEY", "API_SECRET")
auth.set_access_token("KEY", "SECRET")

api = tweepy.API(auth)

def favorite():
  for tweet in api.search_tweets(q="#beerleaguehockey", lang="en", count=18):
    status = api.get_status(tweet.id, tweet_mode = 'extended')
    if not status.retweeted:  # Check if Retweet
      try:
        api.create_favorite(tweet.id)
      except Exception as e:
        logger.error("Error on retweet", exc_info=True)
while True:
  favorite()