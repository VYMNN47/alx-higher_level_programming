#!/usr/bin/python3
"""a Python script that takes in a URL and an email address"""
import sys
import requests


def fetch():
    url = sys.argv[1]
    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)


if __name__ == "__main__":
    fetch()
