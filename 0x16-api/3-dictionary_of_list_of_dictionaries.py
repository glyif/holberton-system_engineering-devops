#!/usr/bin/python3
"""
grabs data from json api, exports to csv
"""


from collections import namedtuple, OrderedDict
import csv
import json
import requests


ALL_TODO_URL = "https://jsonplaceholder.typicode.com/todos/"
ALL_EMPLOYEE_URL = "https://jsonplaceholder.typicode.com/users/"


def all_employees():
    """
    gets all employees, returns list of ids
    :return: list tuples (id, username)
    """
    all_employees = requests.get(ALL_EMPLOYEE_URL).json()
    all_ids = []

    for employee in all_employees:
        all_ids.append(employee.get("id"))

    return all_ids


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


def to_dict(data):
    """
    exports employee data to json
    :param data: data to export
    :param path: path to export to
    :return:
    """
    export_data = {str(data[0]): []}
    for task in data[2]:
        task_data = {"username": data[1],
                     "completed": task.get("completed"),
                     "task": task.get("title")}
        export_data.get(str(data[0])).append(task_data)

    return export_data

if __name__ == "__main__":
    Employee = namedtuple("Employee",
                          ["id", "name", "tasks"])

    all_e = all_employees()
    all_data = OrderedDict()

    for id in all_e:
        e_name = get_name(str(id))["name"]
        e_data = get_tasks(str(id))
        employee = Employee(id=id, name=e_name, tasks=e_data)
        all_data.update(to_dict(employee))

    with open("./todo_all_employees.json", "w+") as json_file:
        json.dump(all_data, json_file)
