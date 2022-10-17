#!/usr/bin/python3
"""
Returns information about a employee's TODO list
"""
from sys import argv
import requests


def todo_list(employeeid):
    """uses employee id"""
    if len(argv) > 1:
        user = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        employee = requests.get("{}users/{}".format(url, user))
        name = employee.json().get("name")
        if name is not None:
            jreq = requests.get(
                "{}todos?userId={}".format(
                    url, user)).json()
            alltasks = len(jreq)
            completedtasks = []
            for t in jreq:
                if t.get("completed") is True:
                    completedtasks.append(t)
            count = len(completedtasks)
            print("Employee {} is done with tasks({}/{}):"
                    .format(name, count, alltasks))
            for task in completedtasks:
                print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    todo_list(argv[1])
    