#!/usr/bin/python3
"""get the numb of subs"""
import requests


def number_of_subscribers(subreddit):
    """"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
