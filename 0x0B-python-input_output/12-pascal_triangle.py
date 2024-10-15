#!/usr/bin/python3
def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n"""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Start a new row with `1`
        row = [1] * (i + 1)

        # Fill in the interior values of the row
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
