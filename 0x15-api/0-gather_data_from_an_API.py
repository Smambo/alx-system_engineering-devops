#!/usr/bin/python3
"""Import modules for api script"""
import requests
from sys import argv


def todo_api(userid):
    """Returns information about employees TODO list progress."""
    name = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
        userid)).json().get('name')
    task = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
                userid)).json()
    tasks_done = ['\t {}\n'.format(dic.get('title')) for dic in task
                  if dic.get('completed')]
    if name and task:
        print("Employee {} is done with tasks({}/{}):".format(
            name, len(tasks_done), len(task)))
        print(''.join(tasks_done), end='')


if __name__ == "__main__":
    if len(argv) == 2:
        todo_api(int(argv[1]))
