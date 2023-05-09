#!/usr/bin/python3
"""A function that queries reddit API & print first 10
hot posts
"""
import requests


def top_ten(subreddit):
    """A function that returns top ten hot post """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Linux: 0x16.api.advanced:v1.0.0 (by /u/ufaz_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    rlt = list()
    for result in results.get("children"):
        rlt.append(result.get("data").get("title"))
    print(rlt)
