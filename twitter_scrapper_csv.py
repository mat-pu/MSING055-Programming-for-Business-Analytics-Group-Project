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

# Open/Create a CSV file to append data:
outfile = open('Brexit.csv', 'a')

# Use CSV writer to impute data to the CSV file:
csv_write = csv.writer(outfile)

# Create header row for our data:
csv_write.writerow(["tweet_id",
                    "username",
                    "number_of_followers",
                    "created_at",
                    "tweet_text",
                    "source",
                    "likes",
                    "retweets",
                    "user_location"])

# Search restricted to 400 most recent tweets in English containing the hashtag 'brexit'
for tweet in tweepy.Cursor(api.search, q="#brexit", lang="en").items(400):
     csv_write.writerow([tweet.id,
                         tweet.author.screen_name,
                         tweet.author.followers_count,
                         tweet.created_at,
                         tweet.text,
                         tweet.source,
                         tweet.favorite_count,
                         tweet.retweet_count,
                         tweet.author.location])
outfile.close()
