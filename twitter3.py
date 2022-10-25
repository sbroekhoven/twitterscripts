import tweepy
import app_config

config = app_config.read_config()
client = tweepy.Client(config['twitter']['bearer_token'])

response = client.search_recent_tweets(
    "ddos attack -is:retweet lang:en -is:reply",
    max_results = 100,
    tweet_fields = ['author_id','created_at','text','source','lang','geo'],
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

    print(f"URL: https://twitter.com/{user.username}/status/{tweet.data['id']}")


# https://twitter.com/places/555d6b4e2f6a18f6 # BOZ
# https://dev.to/twitterdev/a-comprehensive-guide-for-using-the-twitter-api-v2-using-tweepy-in-python-15d9