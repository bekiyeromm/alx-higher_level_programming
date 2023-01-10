#!/usr/bin/python3
"""module for pascal_triangle"""


def pascal_triangle(n):
    """a method to create a pascal_triangle"""
    triangle = []
    line = [1]
    y = [0]
    for x in range(max(n, 0)):
        triangle.append(line)
        line = [a + r for a, r in zip(line + y, y + line)]
    return triangle
