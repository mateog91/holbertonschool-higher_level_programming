#!/usr/bin/python3
"""class MyInt that inherits from int:"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""

    def __eq__(self, x: object):
        """overrides the magic method into this new one by calling it into the
            upper class int method ne"""
        return super().__ne__(x)

    def __ne__(self, x: object):
        """overrides the magic method into this new one by calling it into the
            upper class int method eq"""
        return super().__eq__(x)
