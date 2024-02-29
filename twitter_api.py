import tweepy


access_token = "1480030186829615104-yzUyRCm2aIHh2FWZPyrAVYEw7N7QXX"
access_token_secret = "BNmRclrWmHbAPUXW7FtPTLRrDKWxSY1bbjWJzdylbKong"
api_key = "wQAqcIo5FswK0chPV22LLC5Bb"
api_key_secret = "X3KWhWEWnx1r7DRmLL6DgJvZwOsFW3kxwbkRqr0jwAhIPzzavW"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAFZfsgEAAAAAogCrSK3hdLwDgHBVb%2BJoksg2U7A%3DgHzuyw0EaFTX3RgrozI2e4PsfA8ig9dIACHVSVgh9DT5nWfRA4"

client = tweepy.Client(bearer_token=bearer_token)

print(client.search_all_tweets(query="environment"))