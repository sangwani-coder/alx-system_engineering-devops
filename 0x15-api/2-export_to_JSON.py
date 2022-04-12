#!/usr/bin/python3
""" Returns data from a REST API and exports to data to JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_url = requests.get(url + "users/{}".format(user_id)).json()
    username = user_url.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
            } for t in todos]}, jsonfile)
