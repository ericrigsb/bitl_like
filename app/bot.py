import os
import tweepy
import time
import logging

# API key
api_key = os.getenv("API_KEY")
# API secret key
api_secret = os.getenv("API_SECRET")
# Access token
key = os.getenv("KEY")
# Access token secret
secret = os.getenv("SECRET")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

def favorite():
  for tweet in api.search_tweets(q="#beerleaguehockey", lang="en", result_type="recent", count=18):
    status = api.get_status(tweet.id, tweet_mode = 'extended')
    if not status.retweeted:  # Check if Retweet
      try:
        api.create_favorite(tweet.id)
      except Exception as e:
        logger.error("Error on like", exc_info=True)
while True:
  favorite()
  time.sleep(900)