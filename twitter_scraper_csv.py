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
with open('Brexit_.csv', 'a') as outfile:
  # Searching a selected number of tweets (e.g., 2000) containing the keyword 'Brexit' 
  # Restriction on date/period & language
    for tweet in tweepy.Cursor(api.search, q="brexit", 
                               lang="en",
                               since="2017-11-20",
                               until="2017-11-26").items(2000):
        csv_write = csv.writer(outfile, delimiter=',', quotechar='"')
        csv_write.writerow([tweet.id, 
                            tweet.author.screen_name,
                            tweet.author.verified,
                            tweet.author.followers_count, 
                            tweet.created_at, 
                            tweet.text,
                            tweet.in_reply_to_screen_name,
                            tweet.in_reply_to_status_id,
                            tweet.source,
                            tweet.is_quote_status,
                            tweet.retweeted,
                            tweet.favorite_count,
                            tweet.retweet_count,
                            tweet.author.location])
