#!/usr/bin/python3
"""Import modules."""
from sys import argv
from requests import get


def number_of_subscribers(subreddit):
    """
    Function gets subscriber count
    from subreddit using Reddit API.
    """
    head = {'User-Agent': 'Sima Njoli'}
    sub_count = get(
            'https://www.reddit.com/r/{}/about.json'.format(
                subreddit), headers=head).json()
    try:
        return (sub_count.get('data').get('subscribers'))
    except:
        return (0)


if __name__ == "__main__":
    number_of_subscribers(argv[1])
