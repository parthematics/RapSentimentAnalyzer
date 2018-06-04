import tweepy
from textblob import TextBlob as tb
import matplotlib.pyplot as plt
import numpy as np
import operator

# authentication for tweepy, changed for privacy concerns
consumer_key = 'Z03e28I1edSCRX'
consumer_secret = 'p7fXTdOnr2m152RsHZcRFJ'

access_token = 'I9QWNS6YXVMWPv5kd49PYvoHF1xzMHsrZQL'
access_token_secret = '1qk0pQIZPh6M9MqF1dc9cdlXnO2n'

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

# plotting the results and showing relative public outlook on these two rappers
plt.figure(1, figsize=(7, 7))
plt.title('Overall Sentiment Regarding\nDrake vs. Pusha T')
pie_data = [overall_sentiment[i] for i in ['Drake', 'Pusha T']]
pie_data_refined = [pie_data[i] / sum(pie_data) for i in range(2)]
pie_labels = ['Drake', 'Pusha T']
plt.pie(pie_data_refined, autopct='%1.1f%%', labels=pie_labels)

plt.show()

y_pos = np.arange(len(overall_sentiment.keys()))
popularity = overall_sentiment.values()

plt.bar(y_pos, popularity, align='center', alpha=0.5)
plt.xticks(y_pos, overall_sentiment.keys())
plt.ylabel('Overall Sentiment')
plt.title('Twitter User Outlook on Rappers')

plt.show()
