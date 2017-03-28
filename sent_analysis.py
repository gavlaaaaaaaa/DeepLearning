import pandas
import matplotlib

n = 1578628

filename = "Sentiment Analysis Dataset.csv"

df = pandas.read_csv(filename, skiprows=range(1,n-1000))
print df.head(10)

df = df.drop('SentimentSource', 1)
df['TextLength'] = df['SentimentText'].apply(len)
avg_tweet_length = df['TextLength'].mean()
print avg_tweet_length


df['TextLength'].head(10).plot(kind='bar')