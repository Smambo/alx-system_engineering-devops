#!/usr/bin/python3
"""Import modules."""
from requests import get
from sys import argv


def top_ten(subreddit):
    """
    function queries Reddit API to print titles
    of first 10 hot posts in a subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?count=10".format(subreddit)
    head = {'User-Agent': 'Sima Njoli'}

    response = get(url, headers=head)

    if response.status_code == 200:
        data = response.json()
        count = data['data']['children']
        print('\n'.join([dic.get('data').get('title')
              for dic in count][:10]))
    elif response.status_code == 404:
        print("None")
    else:
        print("None")


if __name__ == "__main__":
    top_ten(argv[1])
