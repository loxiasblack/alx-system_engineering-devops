#!/usr/bin/python3
""""""
import requests

def top_ten(subbreddit):
    """"""
    headers = {'User-Agent': 'subreddit_subscriber_counter/0.1'}
    url="https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url=url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data
