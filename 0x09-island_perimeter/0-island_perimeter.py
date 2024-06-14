#!/usr/bin/python3
"""Generate a grid Island based on a matrix (lisf of list in python)"""


def island_perimeter(grid):
    """Island Function"""
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows = len(grid)
    columns = len(grid[0])
    lands = []

    for x, line in enumerate(grid):
        for y, column in enumerate(line):
            if column == 1:
                lands.append([x, y])

    for land in lands:
        # Checking Top
        if land[0] == 0 or grid[land[0]-1][land[1]] == 0:
            perimeter += 1
        # Checking Bottom
        if land[0] == rows - 1 or grid[land[0]+1][land[1]] == 0:
            perimeter += 1
        # Checking Left
        if land[1] == 0 or grid[land[0]][land[1]-1] == 0:
            perimeter += 1
        # Checking Right
        if land[1] == columns - 1 or grid[land[0]][land[1]+1] == 0:
            perimeter += 1

    return perimeter
