#!/usr/bin/python3
"""Import modules for json script."""
import json
from requests import get
from sys import argv


def json_export():
    """Exports data in JSON format."""
    data = get('https://jsonplaceholder.typicode.com/users').json()
    ids = [(dic.get('id'), dic.get('username')) for dic in data]

    dumps = {}

    for user in ids:
        data = get(
                'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                    user[0])).json()
        records = [{"task": line.get('title'), "completed":
                    line.get('completed'), "username":
                    user[1]} for line in data]
        dumps[user[0]] = records

    with open('todo_all_employees.json', 'w') as f:
        json.dump(dumps, f)


if __name__ == "__main__":
    json_export()
