#!/usr/bin/python3
"""a Python script that takes in a URL and an email address"""
import sys
import urllib.request


def fetch():
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))


if __name__ == "__main__":
    fetch()
