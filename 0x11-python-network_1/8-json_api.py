#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a parameter.

    The letter must be sent in the variable q
    If no argument is given, set q=""
    If the response body is properly JSON formatted and not emptY:
        displaythe id and name like this: [<id>] <name>
    Otherwise:
        Display Not a valid JSON if the JSON is invalid
        Display No result if the JSON is empty
    You must use the package requests and sys
    You are not allowed to import packages other than requests and sys
    """

if __name__ == "__main__":
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    response = requests.post(url, data={'q': q})
    try:
        d = response.json()
        if not d:
            print("No result")
        else:
            print("[{}] {}".format(d['id'], d['name']))

    except ValueError("Not a valid JSON"):
        pass
