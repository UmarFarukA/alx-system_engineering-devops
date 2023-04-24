#!/usr/bin/python3
"""A script that load data to csv file"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users").json()
    with open("todo_all_employees.json", "w") as fw:
        for userId in range(1, len(user)):
            user = requests.get(url + "users/{}".format(userId)).json()
            todos = requests.get(url + "todos",
                                 params={"userId": userId}).json()
            username = user.get("username")
            json.dump({userId: [{"task": todo.get("title"),
                                 "completed": todo.get("completed"),
                                 "username": userName} for todo in todos]}, fw)
