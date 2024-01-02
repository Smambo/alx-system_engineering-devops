#!/usr/bin/python3
"""Import modules for csv script"""
import csv
from requests import get
from sys import argv


def csv_export(user):
    """Exports data in CSV format."""
    data = get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        user)).json()
    name = get('https://jsonplaceholder.typicode.com/users/{}'.format(
        user)).json().get('username')
    user_data = open('{}.csv'.format(user), 'w')
    c_export = csv.writer(user_data, quoting=csv.QUOTE_ALL)

    for line in data:
        lines = [line.get('userId'), name, line.get('completed'),
                 line.get('title')]
        c_export.writerow(lines)
    user_data.close()


if __name__ == "__main__":
    csv_export(argv[1])
