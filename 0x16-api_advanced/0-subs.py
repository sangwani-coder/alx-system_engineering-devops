#!/usr/bin/python3
""" Queries the Reddit API for a given subreddit.
    If an invalid subreddit is given, the function should return 0
"""

import json
import requests
import sys


def number_of_subscribers(subreddit):
    """ queries the Reddit API and returns the number of subscribers
        :returns: the numbe of subscribers (not active users)"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
            'User-Agent': 'custo-magent/0.0.1'
            }
    try:
        response = requests.request("GET",
                                    url,
                                    headers=headers,
                                    allow_redirects=False)
        jsonData = response.json()
        subscribers = jsonData["data"]["subscribers"]
        return subscribers
    except Exception:
        return 0
