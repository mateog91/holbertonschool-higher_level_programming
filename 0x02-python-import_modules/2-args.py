#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    print("{} arguments:".format(length))
    for i in range(length):
        print("{}: {}".format(i, sys.argv[i]))
