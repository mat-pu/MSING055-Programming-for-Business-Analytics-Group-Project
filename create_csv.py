import csv

outfile = open('Brexit_.csv', 'w')
csv_write = csv.writer(outfile)
csv_write.writerow(["tweet_id",
                    "username",
                    "verified",
                    "followers",
                    "created_at",
                    "tweet_text",
                    "reply_to_user",
                    "reply_to_tweet",
                    "platform",
                    "quoted",
                    "retweeted",
                    "likes",
                    "retweets",
                    "user_location"])
outfile.close()
