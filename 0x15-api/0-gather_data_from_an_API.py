#!/usr/bin/python3
"""A scripts that fetches user data"""
import requests
import sys


url = "https://jsonplaceholder.typicode.com"
user = url + "/users/{}".format(sys.argv[1])
todos = url + "/todos?userId={}".format(sys.argv[1])

response = requests.get(todos)
res = requests.get(user)

tasks = response.json()
theUser = res.json()

completed = 0
for task in tasks:
    if task['completed']:
        completed += 1
print("Employee {} is done with task ({}/{}):"
      .format(theUser.get('name'), completed, len(tasks)))
[print("\t {}".format(task['title']))
 for task in tasks if task['complete']]
