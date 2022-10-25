import tweepy
from datetime import datetime, timedelta, timezone
import app_config

config = app_config.read_config()
client = tweepy.Client(config['twitter']['bearer_token'])


# Replace with time period of your choice
start_time = datetime.utcnow() - timedelta(days=1)
print(start_time.isoformat('T'))
# Replace with time period of your choice
end_time = datetime.utcnow() - timedelta(seconds=30)
print(end_time.isoformat('T'))

response = client.search_recent_tweets(
    "ddos attack lang:en -is:retweet -is:reply",
    start_time=start_time,
    end_time=end_time,
    max_results = 100,
    tweet_fields = ['author_id','created_at','text','source','lang','context_annotations'],
    user_fields = ['name','username','location','verified'],
    expansions = ['geo.place_id', 'author_id'],
    place_fields = ['country','country_code']
)

# print(response)

# Get users list from the includes object
users = {u["id"]: u for u in response.includes['users']}

for tweet in response.data:
    print("----------------------------------------------")
    print(tweet.text)           # print the text
    print("Language:", tweet.data['lang'])   # print the language (PL, since we're filtering by it)
    print("Source  :", tweet.data['source']) # what did the user use to publish the tweet?
    print("Created :", tweet.data['created_at'])

    if users[tweet.author_id]:
        user = users[tweet.author_id]

    #user = next(
    #    (item for item in response.includes['users'] if item['id'] == tweet.author_id),
    #    {}
    #)

    print(user.name)
    print(user.username)
    print(user.verified)

    # https://developer.twitter.com/en/docs/twitter-api/annotations/overview
    # print("context",tweet.context_annotations)

    print(f"URL: https://twitter.com/{user.username}/status/{tweet.data['id']}")


number_of_elements = len(response.data)
print("Number of elements in the list: ", number_of_elements)

my_date = datetime.utcnow()
print(my_date.strftime('%Y-%m-%dT%H:%M:%S.%f%z'))

# https://twitter.com/places/555d6b4e2f6a18f6 # BOZ
# https://dev.to/twitterdev/a-comprehensive-guide-for-using-the-twitter-api-v2-using-tweepy-in-python-15d9
# https://fairyonice.github.io/extract-someones-tweet-using-tweepy.html



