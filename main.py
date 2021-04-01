# ----------------------------------------
# Created on 1st Apr 2021
# By the Cached Coder
# ----------------------------------------
'''
This is the main script. Run it to get the
get the post to tweet and then tweet it
'''
import twitter
import reddit

if __name__ == '__main__':
    # Reddit stuff first
    bot = reddit.redditLogin()
    data = reddit.getPosts(bot)
    msg = reddit.getMsgToTweet(data)

    # Then the twitter stuff
    api = twitter.getAPIObject()
    twitter.postTweet(msg, api)