import os
import time
import tweepy
import logging
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

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

api = tweepy.API(auth,wait_on_rate_limit=True)

with open('hashtags') as f:
    hashtags = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
hashtags = [x.strip() for x in hashtags]

def favorite():
  for hashtag in hashtags:
    for tweet in tweepy.Cursor(api.search_tweets, q=hashtag, lang="en", result_type="recent").items(18):
      status = api.get_status(tweet.id, tweet_mode = 'extended')
      if not status.favorited:  # Check if already favorited
        try:
          print('\nTweet by: @' + tweet.user.screen_name)
          print('\nTweet content: ' + tweet.text)
          api.create_favorite(tweet.id)
        except Exception as e:
          logger.error("Error on like", exc_info=True)
while True:
  favorite()
  time.sleep(86400)