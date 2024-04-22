#!/usr/bin/python3
"""script that gather some data from a REST API"""
import json
import requests
import sys

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
        name = user_info['name']
        user_name = user_info['username']

    task_info = fetch_data(todos_url)
    if task_info is not None:
        list_of_title = []
        number_of_task = 0
        task_done = 0
        for item in task_info:
            number_of_task += 1
            for key, value in item.items():
                if key == 'completed' and value is True:
                    task_done += 1
                    list_of_title.append(item['title'])

        my_dictionnary = {}
        for task in task_info:
            user_id = task['userId']
            if user_id not in my_dictionnary:
                my_dictionnary[user_id] = []
            my_dictionnary[user_id].append({
                                            "task": task['title'],
                                            "completed": task['completed'],
                                            "username": f"{user_name}"
                                            })

        with open(F"{user_id}.json", "w") as file:
            json.dump(my_dictionnary, file)
