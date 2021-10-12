#!/usr/bin/python3
"""class MyInt that inherits from int:"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""

    def __eq__(self, x: object):
        return super().__ne__(x)

    def __ne__(self, x: object):
        return super().__eq__(x)


my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
