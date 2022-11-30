#!/usr/bin/python3
"""Returns Employee information about todo list progression."""
from sys import argv
import json
import requests
"""argv argument is user_id"""
user_id = argv[1]

"""get todo information"""
todo_response = requests.get('https://jsonplaceholder.typicode.com/todos/\
?userId={}'.format(user_id))

"""get user information"""
user_response = requests.get('https://jsonplaceholder.typicode.com/users/\
{}'.format(user_id))

"""parse through todo information"""
todo_data = todo_response.text
parse_todo = json.loads(todo_data)

"""parse through user information"""
user_data = user_response.text
parse_user = json.loads(user_data)

"""task functions"""
name = parse_user['name']
completed_tasks = 0
total_tasks = 0

for task in parse_todo:
    total_tasks += 1
    if task['completed']:
        completed_tasks += 1

print("Employee {} is done with tasks({}/{}):\
".format(name, completed_tasks, total_tasks))

for task in parse_todo:
    if task['completed']:
        print("\t {}\n".format(task['title']), end="")
