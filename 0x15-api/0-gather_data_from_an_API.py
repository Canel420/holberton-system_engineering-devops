#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script that uses a REST API for searching a given employee ID,
and returns information about his/her TO-DO list progress.
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = get(url)
    name = response.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = get(url)
    tasks = response.json()
    done_tasks = []
    for task in tasks:
        if task.get('completed'):
            title = task.get('title')
            done_tasks.append(title)

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(done_tasks), len(tasks)))
    for title in done_tasks:
        print("\t {}".format(title))
