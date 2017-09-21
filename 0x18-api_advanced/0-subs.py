#!/usr/bin/python3
"""
Gets all subscribers or a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    number of subscriber of subreddit
    :param subreddit: subreddit to find subscribers
    :return: 0 if not found or # of subscribers
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get("https://www.reddit.com/r/{}/about.json".
                     format(subreddit),
                     headers=headers)
    response = r.json()

    if response.get("error") is not None:
        return 0

    return response.get("data").get("subscribers")
