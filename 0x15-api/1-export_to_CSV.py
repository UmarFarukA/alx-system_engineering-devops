#!/usr/bin/python3
"""A script that load data to csv file"""
import requests
import sys
import csv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userUrl = url + "users/{}".format(sys.argv[1])
    todosUrl = url + "todos"
    todos = requests.get(todosUrl, params={"userId": sys.argv[1]}).json()
    user = requests.get(userUrl).json()
    with open("{}.csv".format(sys.argv[1]), "w") as fw:
        userId = user.get("id")
        userName = user.get("username")
        for todo in todos:
            writer = csv.writer(fw, qouting=csv.QOUTE_ALL)
            writer.writerow([userId, userName, todo.get("completed"),
                              todo.get("title")])
