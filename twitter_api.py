import tweepy

access_token = "1480030186829615104-yzUyRCm2aIHh2FWZPyrAVYEw7N7QXX"
access_token_secret = "BNmRclrWmHbAPUXW7FtPTLRrDKWxSY1bbjWJzdylbKong"
api_key = "wQAqcIo5FswK0chPV22LLC5Bb"
api_key_secret = "X3KWhWEWnx1r7DRmLL6DgJvZwOsFW3kxwbkRqr0jwAhIPzzavW"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAFZfsgEAAAAAogCrSK3hdLwDgHBVb%2BJoksg2U7A%3DgHzuyw0EaFTX3RgrozI2e4PsfA8ig9dIACHVSVgh9DT5nWfRA4"
client_id = "ZURWdjBZM3d4OXpKd3lfanRWeWQ6MTpjaQ"
client_secret = "FZdCIcCzs359YRMWBz0cZjcbKZVlyCF7w_qYgz4oyk6pXsAF1e"

auth = tweepy.OAuth1UserHandler(consumer_key=api_key, consumer_secret=api_key_secret,
                                access_token=access_token,access_token_secret=access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

search_query = "'Joe Biden' 'environment'"
numTweets = 100

tweets = api.search_tweets(q=search_query, count=numTweets)

for tweet in tweets:
    print(tweet)