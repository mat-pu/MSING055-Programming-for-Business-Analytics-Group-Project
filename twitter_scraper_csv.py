import tweepy
import csv
import pandas as pd

# Enter authentification credentials:
consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_token_secret = 'ACCESS_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open CSV file to append new rows with data (based on the query):
with open('Brexit_data.csv', 'a') as outfile:
  # Searching a selected number of tweets (e.g., 100) about a specific topic in connection to brexit (e.g., stock market)
  # Restriction on date/period
    for tweet in tweepy.Cursor(api.search, q="brexit AND <search term>",lang="en",since="2017-11-11", until="2017-11-18").items(100):
      # Using CSV writer to inpute new rows with data:
        csv_write = csv.writer(outfile, delimiter=',', quotechar='"')
        csv_write.writerow([tweet.id, 
                        tweet.author.screen_name, 
                        tweet.author.followers_count, 
                        tweet.created_at, 
                        tweet.text, 
                        tweet.source, 
                        tweet.favorite_count, 
                        tweet.retweet_count, 
                        tweet.author.location])
