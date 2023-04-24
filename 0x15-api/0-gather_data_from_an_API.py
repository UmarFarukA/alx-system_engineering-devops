#!/usr/bin/python3
"""A scripts that fetches user data"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userUrl = url + "users/{}".format(sys.argv[1])
    todosUrl = url + "todos"
    todos = requests.get(todosUrl, params={"userId": sys.argv[1]}).json()
    user = requests.get(userUrl).json()
    completed = [todo.get("title") for todo in todos
                 if todo.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(completed), len(todos)))
    [print("\t {}".format(title) for title in completed)]
