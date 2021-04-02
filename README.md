# thsb
Twitter bot that posts from reddit.

[Youtube Video](https://www.youtube.com/watch?v=pobm1t32Y2g)

Run `pip install -r requirements.txt` to get the required libraries up.

Then, make sure you have a `secrets.json` file that stores all the required keys (eg below)

```json
{
    "twitter_access_token":"1",
    "twitter_access_secret":"x",
    "twitter_consumer_key":"q",
    "twitter_consumer_sec":"L",
    "reddit_username" : "C",
    "reddit_password" : "2",
    "reddit_clientid" : "p",
    "reddit_clientse" : "v",
    "reddit_usragent" : "O"
}
```

Then, run `main.py` to automatically take the top post from the past day and post it onto twitter.
