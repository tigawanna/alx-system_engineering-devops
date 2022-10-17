#!/usr/bin/python3
"""Module fetches employe tasks and display on stdout."""


class Fetch:
    """Class provides fetch services."""

    def __init__(self, userId):
        """Initialize fetch instance."""

        payload = {"userId": userId}
        userInfo = requests.get(
            "https://jsonplaceholder.typicode.com/users/{:s}".format(
                userId
            )
        ).json()

        self.userId = userId
        self.name = userInfo.get("name")
        self.userName = userInfo.get("username")
        self.todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos/",
            params=payload
        ).json()

        return None

    def project_task_one(self):
        """Return information about employee TODO list progress

        Args:
            self (object): <class 'main.Fetch'> type object

        Returns:
            Comperhensive string of employee TODO list progress
        """
        brief = "Employee {:s} is done with tasks ({:d}/{:d}):\n".format(
            self.userName,
            len(Fetch.__tasks(self.todos)["complete"]),
            len(self.todos)
        )
        completed = Fetch.__completed_tasks(
            Fetch.__tasks(self.todos)["complete"]
        )
        return [brief, completed]

    def project_task_two(self):
        """Export data in CSV format.

        Records all tasks that are owned by this employee
        Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

        Args:
            self (object): <class 'main.Fetch'> type object

        Returns:
            None
        """
        todos = deepcopy(self.todos)
        with open("{:s}.csv".format(self.userId), 'w') as file:
            fieldnames = ["userId", "name", "completed", "title"]
            writer = csv.DictWriter(
                file,
                quoting=csv.QUOTE_ALL,
                fieldnames=fieldnames
            )
            for obj in todos:
                obj.pop("id", None)
                obj["name"] = self.userName
                writer.writerow(obj)
        return None

    @staticmethod
    def __tasks(tasks_list):
        """returns dictionary of task lists acording to completeness.

        Args:
            tasks_list (list): List of tasks fetched.
            status (str): `finished` or `unfinished`.

        Returns:
            dictionary of completed and uncompleted task lists.
        """
        status_dict = {
            "complete": [],
            "incomplete": []
        }

        for elem in tasks_list:
            if elem.get("completed") is True:
                status_dict["complete"].append(elem)
        for elem in tasks_list:
            if elem not in status_dict["complete"]:
                status_dict["incomplete"].append(elem)
        return status_dict

    @staticmethod
    def __completed_tasks(tasks_list):
        """Returns string representation of all tasks in provided list

        Args:
            tasks_list (list): List of tasks fetched.

        Returns:
            Tabulated list of completed tasks
        """
        brief = ""
        for elem in tasks_list:
            brief += "\t {:s}\n".format(elem.get("title"))
        return brief
    pass


if __name__ == "__main__":
    from copy import deepcopy
    import csv
    import requests
    import sys

    fetch = Fetch(sys.argv[1])
    fetch.project_task_two()
