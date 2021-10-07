#!/usr/bin/python3
"""Module to multiply two matrix

Description:
Must be list, list of lists, elements must be integers or floats
Matrixes must have correct dimension to be able to be multiplied
"""


def matrix_mul(m_a, m_b):
    """returns a matrix of result multiplication of two matrix

    Args:
        m_a (list): Frist matrix. Must be a list of list of integers or floats
        m_b (list): Frist matrix. Must be a list of list of integers or floats

    Description:
        Multiplies m_a by m_b. Columbs of m_a must be same size as rows of m_b
    """
    # Not list
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    # Not list of lists
    for rows in m_a:
        if type(rows) is not list:
            raise TypeError("m_a must be a list of lists")

    # Not empty
    for rows in m_b:
        if type(rows) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise TypeError("m_a can't be empty")
    for rows in m_a:
        if rows == []:
            raise TypeError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_a can't be empty")
    for rows in m_b:
        if rows == []:
            raise ValueError("m_b can't be empty")

    # Elements of list of lists not integer or float
    for rows in m_a:
        for element in rows:
            if type(element) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")

    for rows in m_b:
        for element in rows:
            if type(element) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    # Not matrix rectangles
    size_rows = len(m_a[0])
    for rows in m_a:
        if size_rows != len(rows):
            raise TypeError("each row of m_a must be of the same size")

    size_rows = len(m_b[0])
    for rows in m_b:
        if size_rows != len(rows):
            raise TypeError("each row of m_b must be of the same size")

    # size of columns of m_a must be same as rows of m_b
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m3 = []
    for i in range(0, len(m_a)):
        m3.append([])
        current_sum = 0
        for j in range(0, len(m_b)):
            current_sum += m_b[j][i] * m_a[i][j]
        m3[i].append(current_sum)

    return m3


print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
