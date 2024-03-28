#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io"""
import urllib.request
import urllib.parse
from sys import argv


def fetch():
    """Fetches X-Request-Id variable"""
    url = argv[1]

    email = {'email': argv[2]}
    data = urllib.parse.urlencode(email).encode()

    request = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(request) as response:
        b = response.read().decode('utf-8')

    print(b)


if __name__ == "__main__":
    fetch()
