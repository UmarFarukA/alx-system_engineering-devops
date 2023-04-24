#!/usr/bin/python3
"""A script that load data to csv file"""
import json
import requests
import sys


if __name__ == "__main__":
    userId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(userId)).json()
    userName = user.get("username")
    todos = requests.get(url + "todos", params={"userId": userId}).json()

    with open("{}.json".format(userId), "w") as fw:
        json.dump({userId: [{"task": todo.get("title"),
                             "completed": todo.get("completed"),
                             "username": userName} for todo in todos]}, fw)
