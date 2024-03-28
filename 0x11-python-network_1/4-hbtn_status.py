#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import requests


def fetch():
    """Fetches given url"""
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        html = response.read()
        decoded = html.decode('utf-8')

    print("Body response:")
    print("\t- type: {}".format(type(html.text)))
    print("\t- content: {}".format(html.text))


if __name__ == "__main__":
    fetch()
