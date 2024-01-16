#!/usr/bin/python3
"""Import modules."""
from requests import get
from sys import argv


def recurse(subreddit, hot_list=[], after=None):
    """Function recursively queries Reddit API and returns list
    containing titles of all hot articles for a subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, after)
    url2 = "https://www/reddit.com/r/{}/hot.json".format(subreddit)
    head = {'User-Agent': 'Sima Njoli'}

    try:
        if after:
            count = get(url, headers=head).json().get('data')
        else:
            count = get(url2, headers=head).json().get('data')
        hotlist += [dic.get('data').get('title')
                    for dic in count.get('children')]

        if count.get('after'):
            return (recurse(subreddit, hotlist, after=count.get('after')))
        return (hotlist)
    except Exception:
        return (None)


if __name__ == "__main__":
    recurse(argv[1])
