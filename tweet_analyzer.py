import tweepy
from textblob import TextBlob as tb
import matplotlib.pyplot as plt
import numpy as np
import operator

# authentication for tweepy
consumer_key = 'JC5Z03e2RXIVeS2'
consumer_secret = 'KCwWyp7fXrYEKc9TDqH52RsHZcUM5p2B9V4WRFJ'

access_token = '5444-FIBRcI9QWNS6YX1xzMHsrZQL'
access_token_secret = 'pQIZPh6M9MqFsL9cdlXnO2yoqr5n'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

app = tweepy.API(auth)

# tags for analysis, recent beef between drake & pusha
# extra names, such as Kanye, Kendrick, Lil Wayne, and Birdman added for comparison
names = ['Drake', 'Pusha T', 'Kanye', 'Kendrick', 'Lil Wayne', 'Birdman']
major_tag = "Adidon"
from_date = "2018-05-02"
to_date = "2018-06-02"

# return labels for sentiment analysis
def get_sentiment(text_analysis, threshold=0):
    if text_analysis.sentiment[0] > threshold:
        return 'Positive'
    else:
        return 'Negative'

overall_sentiment = {}
for rapper in names:
    rapper_polarities = []
    tweet_texts = []
    total_sentiment = 0
    rapper_tweets = app.search(q=rapper, count=100, since=from_date, until=to_date)
    # modify q value to filter results to include tweets with 'Adidon'
    # rapper_tweets = app.search(q=[rapper, major_tag], count=100, since=from_date, until=to_date)

    with open('%s_tweets.csv' % rapper, 'w') as rapper_file:
        rapper_file.write('Tweet, Sentiment_Label\n')
        for tweet in rapper_tweets:
            text_analysis = tb(tweet.text)  # might use NaiveBayesAnalyzer()
            total_sentiment += text_analysis.sentiment[0]
            if tweet.text.encode('utf-8') not in tweet_texts:  # to prevent quoted tweets from skewing results
                rapper_polarities.append(text_analysis.sentiment[0])
                rapper_file.write('%s,%s\n' % (tweet.text.encode('utf-8'), get_sentiment(text_analysis)))
            tweet_texts.append(tweet.text.encode('utf-8'))

    overall_sentiment[rapper] = total_sentiment / len(rapper_polarities)

cumul_analysis = sorted(overall_sentiment.items(), key=operator.itemgetter(1), reverse=True)
print('Overall Sentiment Polarity on the Beef: ')
for rapper, polarity in cumul_analysis:
    print(rapper + ' : ' + "%.4f" % polarity)