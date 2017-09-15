import re
import csv
from sys import argv


# script, file_ = argv

def processRow(row):
    tweet = row[3]
    # Lower case
    tweet.lower()
    # Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub('[\n]+', ' ', tweet)
    # Remove not alphanumeric symbols white spaces
    tweet = re.sub(r'[^\w]', ' ', tweet)
    # Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    # Remove :( or :)
    tweet = tweet.replace(':)', '')
    tweet = tweet.replace(':(', '')
    # trim
    tweet = tweet.strip('\'"')

    row[3] = tweet

    return row


# end processTweet

if __name__ == '__main__':
    # Read the tweets one by one and process it
    clnfile = open("CLN-" + file_, 'wb')
    filewriter = csv.DictWriter(clnfile, fieldnames=["tweetID", "userHandler", "tweetUrl", "tweetText", "is_spam"])

    with open(file_, "rb") as csvfile:
        filereader = csv.reader(csvfile)
        for row in filereader:
            new_row = processRow(row)
            filewriter.writerow({
                "tweetID": new_row[0],
                "userHandler": new_row[1],
                "tweetUrl": new_row[2],
                "tweetText": new_row[3],
                "is_spam": new_row[4]
            })
    clnfile.close()