#!/usr/bin/python3
"""Import modules."""
from requests import get
from sys import argv


def number_of_subscribers(subreddit):
    """
    Function gets subscriber count
    from subreddit using Reddit API.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    head = {'User-Agent': 'Sima Njoli'}

    response = get(url, headers=head)

    if response.status_code == 200:
        data = response.json()
        sub_count = data['data']['subscribers']
        return (sub_count)
    elif response.status_code == 404:
        return (0)
    else:
        return (0)


if __name__ == "__main__":
    number_of_subscribers(argv[1])
