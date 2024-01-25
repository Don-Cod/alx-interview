#!/usr/bin/python3
"""Rotate 2D Matrix."""


def rotate_2d_matrix(matrix):
    """Rotate 2D matrix 90 degrees clockwise."""
    ziped = zip(*reversed(matrix))
    for i, j in enumerate(ziped):
        matrix[i] = list(j)
