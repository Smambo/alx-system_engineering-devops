#!/usr/bin/python3
"""Import modules for json script"""
import json
from requests import get
from sys import argv


def json_export(user):
    """Export data in JSON format."""
    data = get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        user)).json()
    name = get('https://jsonplaceholder.typicode.com/users/{}'.format(
        user)).json().get('username')

    records = []

    for line in data:
        records.append({"task": line.get('title'), "completed":
                        line.get('completed'), "username": name})
    with open('{}.json'.format(user), 'w') as f:
        json.dump({user: records}, f)


if __name__ == "__main__":
    json_export(int(argv[1]))
