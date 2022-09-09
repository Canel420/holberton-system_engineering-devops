#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script that uses a REST API for searching a given employee ID,
and export data into a json format.
"""

from json import dump
from requests import get

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = get(url)
    users = response.json()

    result = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('usernam')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = get(url)
        tasks = response.json()
        result[user_id] = []
        for task in tasks:
            result[user_id].append({
                                    "task": task.get('title'),
                                    "completed": task.get('completed'),
                                    "username": username
                                    })

    with open('todo_all_employees.json', 'w') as file:
        dump(result, file)
