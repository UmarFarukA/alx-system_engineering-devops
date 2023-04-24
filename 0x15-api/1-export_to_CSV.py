#!/usr/bin/python3
"""A script that load data to csv file"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userUrl = url + "users/{}".format(sys.argv[1])
    todosUrl = url + "todos"
    todos = requests.get(todosUrl, params={"userId": sys.argv[1]}).json()
    user = requests.get(userUrl).json()
    userId = user.get("id")
    userName = user.get("username")
    with open("{}.csv".format(sys.argv[1]), "w", newline="") as fw:
        writer = csv.writer(fw, qouting=csv.QOUTE_ALL)
        [writer.writerow([userId, userName, todo.get("completed"),
                             todo.get("title")]) for todo in todos]
