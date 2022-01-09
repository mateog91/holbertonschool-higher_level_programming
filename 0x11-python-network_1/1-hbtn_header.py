#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status
"""

from sys import argv


if __name__ == "__main__":
    import sys
    import urllib.request

    if len(sys.argv) > 1:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            print(response.getheader('X-Request-Id'))
