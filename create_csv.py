import csv
# Creating a new CSV file:
outfile = open('Brexit_data.csv', 'w')
csv_write = csv.writer(outfile, delimiter=',')
# First row used for column headings:
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
