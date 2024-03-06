import requests

#!/usr/bin/python3
"""get users totale of subreddits"""
def number_of_subscribers(subreddit):
    """"""
    headers = {'User-Agent': 'subreddit_subscriber_counter/0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
