#!/usr/bin/python3
'''
gather employee data from API
'''

import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(employee_id))
    user = user_response.json()
    params = {"userId": employee_id}
    todo_response = requests.get(url + "todos", params = params)
    todos = todo_response.json()
    complete = []

    for todo in todos:
        if todo.get("complete") is True:
            complete.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{})".format(user.get("name"), len(complete), len(todos)))

    for complet in complete:
        print("\t {}".format(complet))
