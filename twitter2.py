import tweepy
import app_config

config = app_config.read_config()
client = tweepy.Client(config['twitter']['bearer_token'])

# Search Recent Tweets

# This endpoint/method returns Tweets from the last seven days

response = client.search_recent_tweets("Arjen Kamphuis", max_results=100)
# The method returns a Response object, a named tuple with data, includes,
# errors, and meta fields
print(response.meta)

# In this case, the data field of the Response returned is a list of Tweet
# objects
tweets = response.data


# Each Tweet object has default ID and text fields
for tweet in tweets:
    print(tweet.id)
    print(tweet.text)
