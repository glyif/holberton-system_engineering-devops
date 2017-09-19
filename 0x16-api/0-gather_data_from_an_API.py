#!/usr/bin/python3
"""
grabs data from json api
"""


import requests
from sys import argv


EMPLOYEE_ID = argv[1]
ALL_TODO_URL = "https://jsonplaceholder.typicode.com/todos/"
ALL_EMPLOYEE_URL = "https://jsonplaceholder.typicode.com/users/"


def get_name(id):
    """
    gets employee name from id
    :param id: employee id
    :return: employee name as string
    """
    return requests.get(ALL_EMPLOYEE_URL + id).json()


def get_tasks(id):
    """
    fetches all tasks
    :param id: id of employee
    :return: tuple
            (# of complete tasks,
             # of total tasks,
             list of complete tasks [Title])
    """
    all_tasks = requests.get(ALL_TODO_URL + "?userId=" + id).json()
    all_count = 0
    complete_count = 0
    list_comp_task = []

    for task in all_tasks:
        all_count = all_count + 1
        if task.get("completed") is True:
            complete_count = complete_count + 1
            list_comp_task.append(task.get("title"))

    return complete_count, all_count, list_comp_task


if __name__ == "__main__":
    e_name = get_name(EMPLOYEE_ID)["name"]
    e_data = get_tasks(EMPLOYEE_ID)
    print("Employee {} is done with tasks({}/{}):".format(e_name,
                                                          e_data[0],
                                                          e_data[1]))
    for task in e_data[2]:
        print("\t{}".format(task))
