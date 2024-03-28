#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import requests


def fetch():
    """Fetches given url"""
    url = "https://alx-intranet.hbtn.io/status"
    req = request.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))


if __name__ == "__main__":
    fetch()
