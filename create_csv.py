import csv

outfile = open('Brexit_data.csv', 'w')
csv_write = csv.writer(outfile, delimiter=',')
csv_write.writerow(["tweet_id",
                    "username",
                    "followers",
                    "created_at",
                    "tweet_text",
                    "source",
                    "likes",
                    "retweets",
                    "user_location"])
outfile.close()
