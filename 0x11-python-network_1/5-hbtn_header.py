#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers['X-Request-Id'])
