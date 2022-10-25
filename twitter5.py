# OAuth2.0 Version 
import tweepy
from datetime import datetime, timedelta, timezone
import app_config

config = app_config.read_config()
client = tweepy.Client(config['twitter']['bearer_token'])

"""
If you don't understand search queries, there is an excellent introduction to it here: 
https://github.com/twitterdev/getting-started-with-the-twitter-api-v2-for-academic-research/blob/main/modules/5-how-to-write-search-queries.md
"""

# Replace with time period of your choice
start_time = datetime.utcnow() - timedelta(days=1)
print(start_time.isoformat('T'))
# Replace with time period of your choice
end_time = datetime.utcnow() - timedelta(seconds=30)
print(end_time.isoformat('T'))

#d1.strftime("%Y-%m-%dT%H:%M:%SZ")

# Get tweets that contain the hashtag #petday
# -is:retweet means I don't wantretweets
# lang:en is asking for the tweets to be in english
query = "ddos attack -is:retweet -is:reply"
tweets = tweepy.Paginator(client.search_recent_tweets, query=query,
                              tweet_fields=['created_at'], start_time=start_time,
                              end_time=end_time,max_results=100).flatten(limit=1000)

for tweet in tweets:
    print(tweet.text)

number_of_elements = len(tweet)
print("Number of elements in the list: ", number_of_elements)