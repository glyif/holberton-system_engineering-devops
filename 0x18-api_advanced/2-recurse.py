#!/usr/bin/python3
"""
recursively get all hot posts
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    recursively get all hot posts
    :param subreddit: subreddit to search
    :return: None if invalid or list of all hot posts
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    params = {"limit": 1}

    r = requests.get("https://www.reddit.com/r/{}/hot.json".
                     format(subreddit),
                     headers=headers,
                     params=params)
    response = r.json()

    if response.get("error") is not None:
        return None

    top_posts = response.get("data").get("children")

    if len(top_posts) is 0:
        return None

    post_id = top_posts[0].get("data").get("name")

    hot_list.append(top_posts[0].get("data").get("title"))

    return real_recurse(subreddit, post_id, hot_list)


def real_recurse(subreddit, after_id, hot_list=[]):
    """
    recursively get all hot posts
    :param subreddit: subreddit
    :param after_id: after this id
    :param hot_list: hot list
    :return:
    """
    if after_id is None:
        return None

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    params = {"limit": 100,
              "after": after_id}

    r = requests.get("https://www.reddit.com/r/{}/hot.json".format(subreddit),
                     headers=headers,
                     params=params)
    response = r.json()

    if response.get("error") is not None:
        return None

    top_posts = response.get("data").get("children")

    if len(top_posts) is 0:
        return hot_list

    post_id = top_posts[-1].get("data").get("name")

    for post in top_posts:
        hot_list.append(post.get("data").get("title"))

    return real_recurse(subreddit, post_id, hot_list)
