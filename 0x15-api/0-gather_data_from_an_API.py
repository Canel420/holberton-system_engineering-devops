#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script that uses a REST API for searching a given employee ID,
and returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = get(url)
    name = response.json().get('name')

    url_tasks = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    response = get(url_tasks)
    tasks = response.json()
    done_tasks = []
    for task in tasks:
        if task.get('completed'):
            title = task.get('title')
            done_tasks.append(title)
    print(f'Employee {name} is done with tasks\
({len(done_tasks)}/{len(tasks)}):')
    for title in done_tasks:
        print(f'\t {title}')
