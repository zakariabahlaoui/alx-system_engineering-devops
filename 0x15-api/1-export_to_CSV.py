#!/usr/bin/python3
"""Script save information about employee TODO list progress
in the CSV format"""

import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    endpoint = f"https://jsonplaceholder.typicode.com/users/{id}"

    # get user name
    name = requests.get(endpoint).json().get("username")

    # get employee todos
    endpoint += "/todos"
    todos = requests.get(endpoint).json()

    # save todos on CSV file
    filename = f"{id}.csv"
    with open(filename, "w") as file:
        for task in todos:
            completed = task.get("completed")
            title = task.get("title")
            file.write(f'"{id}","{name}","{completed}","{title}"\n')
