# ----------------------------------------
# Created on 1st Apr 2021
# By the Cached Coder
# ----------------------------------------
'''
This script defines the function required
to get a Twitter API object and post a
Tweet.

Functions:
    getAPIObject():
        No Inputs
        Returns API object (tweepy)

    postTweet(msg, api):
        Takes the message and api object
        as inputs, and posts the tweet
'''
# ----------------------------------------
import tweepy
import json
# ----------------------------------------


def getAPIObject():
    # Loads secrets
    with open('secrets.json', 'r') as fh:
        secrets = json.load(fh)

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(
        secrets['twitter_consumer_key'],
        secrets['twitter_consumer_sec']
    )

    auth.set_access_token(
        secrets['twitter_access_token'],
        secrets['twitter_access_secret']
    )

    # Create API object
    api = tweepy.API(
        auth,
        wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True
    )

    # Retunrs API object
    return api


# Function to post a tweet
def postTweet(msg, api):
    api.update_status(msg)


if __name__ == '__main__':
    print("Getting api object")
    api = getAPIObject()
    print("Posting a tweet")
    postTweet("Bot go bleep bloop, tweet go tweet twoot", api)
