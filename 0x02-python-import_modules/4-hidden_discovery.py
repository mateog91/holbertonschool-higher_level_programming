#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for element in dir(hidden_4):
        if element[:2] != "__":
            print(element)
