#!/usr/bin/python3
"""script that gather some data from a REST API"""
import requests
import sys
import csv


if __name__ == "__main__":
    def fetch_data(url):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None

    user_id = sys.argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    user_info = fetch_data(user_url)
    if user_info is not None:
        user_name = user_info['name']

    task_info = fetch_data(todos_url)
    if task_info is not None:
        list_of_title = []
        number_of_task = 0
        task_done = 0
        for item in task_info:
            number_of_task += 1
            for key, value in item.items():
                list_of_title.append(item['title'])
                if key == 'completed' and value is True:
                    task_done += 1

    
    with open(f'{user_id}.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=",")
        for item in task_info:
            writer.writerow([str(item['userId']),
                             str(f"{user_name}"),
                             str(item['completed']),
                             str(item['title'])])
            
