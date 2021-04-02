# ----------------------------------------
# Created on 1st Apr 2021
# By the Cached Coder
# ----------------------------------------
'''
This script defines the function required
to get a PRAW object to scrape the subreddit
for the content

Functions:
    redditLogin():
        No Inputs
        Returns API object (praw)

    getPosts(bot):
        Takes bot (praw object) as input
        and returns the top 10 posts from
        the previous day

    getMsgToTweet(data):
        Takes the top 10 posts and returns
        the first one which is under the
        character limit.
'''
# ----------------------------------------
import praw
import json
# ----------------------------------------


def redditLogin():
    # Gets secrets
    with open('secrets.json', 'r') as fh:
        secrets = json.load(fh)

    # Creates an instance of the bot
    bot = praw.Reddit(
        client_id=secrets['reddit_clientid'],
        client_secret=secrets['reddit_clientse'],
        password=secrets['reddit_password'],
        user_agent=secrets['reddit_usragent'],
        username=secrets['reddit_username']
    )
    return bot


def getPosts(bot):
    # Get subreddit to scrape
    subreddit = bot.subreddit('TwoSentenceHorror')
    data = []
    # Loops through the submissions to scrape data from api
    submission = subreddit.top('day', limit=10)
    for post in submission:
        data.append(
            [
                post.title,
                post.ups,
                post.num_comments,
                post.selftext
            ]
        )
    return data


def getMsgToTweet(data):
    msg = ''
    for post in data:
        msg = post[0] + ' ' + post[3]
        if len(msg) < 280:
            return msg
    return False


if __name__ == '__main__':
    bot = redditLogin()
    data = getPosts(bot)
    msg = getMsgToTweet(data)
    print(msg)
