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
with open('Brexit_NEW.csv', 'a') as outfile:
  # Searching a selected number of tweets (e.g., 1000) about a specific keyword in connection to Brexit (e.g., unemployment)
  # Restriction on date/period & language
    for tweet in tweepy.Cursor(api.search, q="brexit AND <keyword>",
                               lang="en",
                               since="2017-11-15",
                               until="2017-11-20").items(1000):
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
