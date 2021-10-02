from config import config
import twitter

twitter_config = config['twitter']

twitter_api = twitter.Api(
    consumer_key = twitter_config['consumer_key'],
    consumer_secret = twitter_config['consumer_secret'],
    access_token_key = twitter_config['access_token_key'],
    access_token_secret = twitter_config['access_token_secret'],
)

res = twitter_api.GetFollowers('quleuber')
for u in res:
    print(u.screen_name)
