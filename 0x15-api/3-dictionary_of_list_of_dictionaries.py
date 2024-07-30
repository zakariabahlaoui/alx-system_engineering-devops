#!/usr/bin/python3
"""Script save information about all employees TODO list progress
in the JSON format"""

import json
import requests


if __name__ == "__main__":
    base_endpoint = f"https://jsonplaceholder.typicode.com/users"

    # get all employees
    employees = requests.get(base_endpoint).json()

    # loop through all employees
    dictionary = {}
    for emp in employees:

        # get employee id and username
        id = emp.get("id")
        username = emp.get("username")

        # get todos for current employee
        endpoint = f"{base_endpoint}/{id}/todos"
        todos = requests.get(endpoint).json()

        dictionary[id] = []
        for todo in todos:
            # save on dictionary
            dictionary[id].append(
                {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": username,
                }
            )

    # save dictionary that contains all employees data
    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        json.dump(dictionary, file)
