#!/usr/bin/python3
"""A function that queriessubscribers on given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """A function tha treturns the number of subscribers
    on given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Linux: 0x16.api.advanced:v1.0.0 (by /u/ufaz_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
