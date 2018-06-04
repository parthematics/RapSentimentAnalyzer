# Rap Sentiment Analyzer
Twitter is a great way to gain insight into the minds of people, getting a glimpse of their thoughts, opinions, and feelings towards specific events and individuals. Recently, a public disagreement, or "beef," sparked between Drake and Pusha T, dividing the public on their music and revealing several surprising alleged facts. As a die-hard Drake fan, I wanted to try and analyze what people were saying on Twitter regarding the two rappers and recent events, gauging the overall sentiment towards the beef.

For this mini-project, I used Tweepy and TextBlob API to scrape tweets related to the beef between Drake and Pusha T, and performed sentiment analysis using TextBlob's NLP algorithms to determine an overall public outlook towards each rapper. I then graphed each of these figures to see which rapper was viewed in a more positive light, using this as a measure of overall public support. For comparison purposes, the sentiment analysis was performed on Kanye West, Kendrick Lamar, Lil Wayne, and Birdman. 

To actually view the tweets that were scraped in a systematic format, each rapper's specific tweets were written to a .csv file, along with a column indicating whether or not the tweet was "positive" or "negative." 

The results of the project are shown below for your amusement. Based on the results, Drake should eventually come out on top - hopefullt with a diss track that ends Pusha's career.

Below are the raw results of the overall sentiment polarity for each rapper by scraping 100 tweets and taking the mean of individual sentiment polarities, ranked from -1 (pure negative sentiment) to +1 (pure positive sentiment). It should be no surprise that Kendrick, for his empowering lyrics and powerfully positive social image, comes out on top. 

![](https://github.com/parthematics/RapSentimentAnalyzer/blob/master/Screen%20Shot%202018-06-03%20at%207.07.07%20PM.png)

Here are the numbers above shown graphically in a histogram, using MatPlotLib.

![](https://github.com/parthematics/RapSentimentAnalyzer/blob/master/Screen%20Shot%202018-06-03%20at%207.07.27%20PM.png)

Finally, the result we've all been waiting for, Drake vs. Pusha T. The circle graph below uses the sentiment polarity value for each rapper as a gauge for their level of public support. Despite Pusha's harsh blows at Drake's character, Drake's cheeky smile and status as a pivotal influencer in pop culture lends him the upper hand in this recent beef as of June 3rd, 2018. Let's see if he lives up to what the numbers say.

![](https://github.com/parthematics/RapSentimentAnalyzer/blob/master/Screen%20Shot%202018-06-03%20at%207.07.16%20PM.png)

Come on Drake, as Pusha so eloquently put, let's see what happens when you get angry.

*mic drops.*
