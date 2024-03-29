#!/usr/bin/python3
""" A script that returns the number of subscribers """

import requests


def number_of_subscribers(subreddit):
    """ returns 0 if not a valid subreddit, else
    returns the number of subscribers
    """

    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
