#!/usr/bin/python3
"""Script save information about employee TODO list progress
in the CSV format"""
import csv

def export_to_csv(user_id):
    """
    Exports task data for a given user to a CSV file.

    Args:
        user_id: The ID of the user.
    """

    # Replace this with your actual function to fetch user tasks
    user_tasks = get_user_tasks(user_id)

    # Create the CSV file
    filename = f"{user_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  


        # Write the header row
        writer.writeheader()

        # Write the task data
        for task in user_tasks:
            writer.writerow({
                'USER_ID': task['user_id'],
                'USERNAME': task['username'],
                'TASK_COMPLETED_STATUS': task['completed'],
                'TASK_TITLE': task['title']
            })