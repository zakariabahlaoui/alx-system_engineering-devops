#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """get the number of subscribers for a given subreddit"""

    # check argument
    if not subreddit or not isinstance(subreddit, str):
        return 0

    endpoint = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Reddit API requires a User-Agent header
    headers = {"User-Agent": "Mozilla/5.0"}

    # call API and get data
    try:
        response = requests.get(
            endpoint, headers=headers, allow_redirects=False
        )
        if response.status_code == 200:
            subscribers = (
                response.json().get("data", {}).get("subscribers", None)
            )
            if subscribers:
                return subscribers
    except:
        pass
    return 0
