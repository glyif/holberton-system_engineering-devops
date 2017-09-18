#!/usr/bin/python3
"""
grabs data from json api, exports to csv
"""


import requests
from collections import namedtuple
from sys import argv
import csv
import json


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
    return requests.get(ALL_TODO_URL + "?userId=" + id).json()


def export_csv(data, path):
    """
    exports employee data to csv
    :param data: data to export
    :param path: path to export to
    :return:
    """
    export_data = []
    for task in data[2]:
        export_data.append([data[0],
                            data[1],
                            task.get("completed"),
                            task.get("title")])

    with open(path, "w+") as csv_file:
        writer = csv.writer(csv_file, delimiter=",", quoting=csv.QUOTE_ALL)
        for line in export_data:
            writer.writerow(line)


def export_json(data, path):
    """
    exports employee data to json
    :param data: data to export
    :param path: path to export to
    :return:
    """
    export_data = {str(EMPLOYEE_ID): []}
    for task in data[2]:
        task_data = {"username": data[1],
                     "completed": task.get("completed"),
                     "task": task.get("title")}
        export_data.get(str(EMPLOYEE_ID)).append(task_data)

    with open(path, "w+") as json_file:
        json.dump(export_data, json_file)


if __name__ == "__main__":
    Employee = namedtuple("Employee",
                          ["id", "name", "tasks"])
    e_name = get_name(EMPLOYEE_ID)["name"]
    e_data = get_tasks(EMPLOYEE_ID)
    employee = Employee(id=EMPLOYEE_ID, name=e_name, tasks=e_data)
    export_json(employee, "./{}.json".format(EMPLOYEE_ID))
