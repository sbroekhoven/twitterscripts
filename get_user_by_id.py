import tweepy
import app_config

config = app_config.read_config()
client = tweepy.Client(config['twitter']['bearer_token'])

# User ID's to get
user_ids = [2244994945, 6253282]

# By default, only the ID, name, and username fields of each user will be
# returned # Additional fields can be retrieved using the user_fields parameter
response = client.get_users(ids=user_ids, user_fields=["profile_image_url", "created_at", "description", "public_metrics"])

for user in response.data:
    print(user.username, user.profile_image_url, user.public_metrics)