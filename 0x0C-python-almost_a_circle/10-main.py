#!/usr/bin/python3
""" 10-main """
from models.square import Square
from models.rectangle import Rectangle

if __name__ == "__main__":

    s1 = Square(9)
    print(s1.size)
    s2 = Rectangle(5, 3)
    print(s2)

    # print(s1.size)
    # s1.size = 10
    # print(s1)

    # try:
    #     s1.size = "9"
    # except Exception as e:
    #     print("[{}] {}".format(e.__class__.__name__, e))
