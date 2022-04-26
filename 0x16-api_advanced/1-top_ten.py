#!/usr/bin/python3
"""
    1-top_ten
    Queries the Reddit API for a given subreddit.
"""

import requests
import sys


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
            'User-Agent': 'custom-agent/0.0.1'
            }
    try:
        response = requests.request("GET",
                                    url,
                                    headers=headers,
                                    allow_redirects=False)
        jsonData = response.json()
        posts0 = jsonData["data"]["children"]
        counter = 10
        for po in posts0:
            if counter > 0:
                print(po["data"]["title"])
                counter -= 1
            else:
                break
    except Exception:
        print(None)
