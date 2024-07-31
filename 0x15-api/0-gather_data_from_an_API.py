#!/usr/bin/python3
"""Script that uses REST API"""
import requests
import json

def get_employee_todo_progress(employee_id):
    """Fetches employee data from the API and prints the task progress."""

    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for error HTTP status codes

        data = response.json()
        employee_name = data['name']
        todos = data['todos']

        completed_tasks = [todo['title'] for todo in todos if todo['completed']]
        total_tasks = len(todos)
        completed_tasks_count = len(completed_tasks)

        print(f"Employee {employee_name} is done with tasks({completed_tasks_count}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 script.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
