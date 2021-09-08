#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for element in dir():
        if element[0] != '_':
            if element[1] != '_':
                print(element)
