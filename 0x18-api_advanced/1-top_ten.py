#!/usr/bin/python3
"""
top 10 posts of a sub reddit
"""

import requests


def top_ten(subreddit):
    """
    top 10 posts of a subreddit
    :param subreddit: subreddit to search
    :return: None if invalid or top 10 titles
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    r = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10".
                     format(subreddit),
                     headers=headers)
    response = r.json()

    if response.get("error") is not None:
        return None

    top_posts = response.get("data").get("children")

    if len(top_posts) is 0:
        print(None)
        return None

    for post in top_posts:
        print("{}".format(post.get("data").get("title")))
