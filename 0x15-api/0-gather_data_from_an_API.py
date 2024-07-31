#!/usr/bin/python3
"""Script that uses REST API"""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    endpoint = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    # get user name
    employee_name = requests.get(endpoint).json().get("name")

    # get employee todos
    endpoint += "/todos"
    todos = requests.get(endpoint).json()
    completed_todos = [todo for todo in todos if todo.get("completed")]

    all = len(todos)
    completed = len(completed_todos)

    print(
        f"Employee {employee_name} is done with tasks({completed}/{all}):"
    )
    # display the title of completed tasks
    for task in completed_todos:
        print(f"	 {task.get('title')}"
