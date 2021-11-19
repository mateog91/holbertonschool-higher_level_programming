def validate(m, name):
    if not isinstance(m, list):
        raise TypeError(f"{name} must be a list")

    if not all(isinstance(row, list) for row in m):
        raise TypeError(f"{name} must be a list of lists")

    if len({len(row) for row in m}) != 1:
        raise TypeError(f"each row of {name} must be of the same size")

    if not all(isinstance(elem, (int, float)) for row in m for elem in row):
        raise TypeError(f"{name} should contain only integers or floats")

    if len(m) == 0:
        raise ValueError(f"{name} can't be empty")

    if len(m[0]) == 0:
        raise ValueError(f"{name} can't be empty")

    return (len(m), len(m[0]))


def matrix_mul(m_a, m_b):

    shape_a = validate(m_a, "m_a")
    shape_b = validate(m_b, "m_b")

    if shape_a[1] != shape_b[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    return [
        [
            sum(m_a[i][k] * m_b[k][j] for k in range(shape_a[1]))
            for j in range(shape_b[1])
        ]
        for i in range(shape_a[0])
    ]
