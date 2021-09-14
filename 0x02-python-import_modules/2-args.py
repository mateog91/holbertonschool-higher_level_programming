#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    if length == 0:
        txt = "."
    else:
        txt = ":"

    if length == 1:
        txt2 = ""
    else:
        txt2 = "s"
    print("{} argument{}{}".format(length, txt2, txt))
    for i in range(1, length + 1):
        print("{}: {}".format(i, sys.argv[i]))
