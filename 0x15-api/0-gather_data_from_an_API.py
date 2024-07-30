#!/usr/bin/python3
'''
gather employee data from API
'''

import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(employee_id))
    user = user_response.json()
    param = {"userId": employee_id}
    todo_response = requests.get(url + "todos", param = param)
    todo_response = todo_reponse.json()
    complete = []

    for todo in todos:
        if tod.get("complete") is True:
            complete.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{})".format(user.get("name"), len(complete), len(todos)))

    for complet in complete:
        print("\t {}".format(complet))
