#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status

    You must use the package requests
    You are not allow to import packages other than requests
    The body of the response must be display
    like the following example (tabulation before -)
"""

if __name__ == "__main__":
    import requests

    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)
    content = response.content.decode('utf-8')

    print("Body response:")
    print("\t- type: < {}".format(type(content)))
    print("\t- content: {}".format(content))
