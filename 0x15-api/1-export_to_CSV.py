#!/usr/bin/python3
"""A script that load data to csv file"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    userUrl = url + "users/{}".format(userId)
    todosUrl = url + "todos"
    todos = requests.get(todosUrl, params={"userId": userId}).json()
    user = requests.get(userUrl).json()
    userName = user.get("username")
    with open("{}.csv".format(userId), "w", newline="") as fw:
        writer = csv.writer(fw, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
