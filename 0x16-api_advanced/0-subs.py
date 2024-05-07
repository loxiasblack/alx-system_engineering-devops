#!/usr/bin/python3
"""get the numb of subs"""
import requests


def number_of_subscribers(subreddit):
    """my function get"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'MyBot/1.0 (by YourUsername)'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        elif response.status_code == 404:
            return 0
        else:
            return 0
    except requests.RequestException as e:
        return 0
