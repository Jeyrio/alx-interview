#!/usr/bin/python3
"""
Module for island perimeter
"""


def island_perimeter(grid):
    # Determine the number of rows and columns in the grid
    rows = len(grid)
    columns = len(grid[0])

    # Intialize the perimeter variable to 0
    perimeter = 0

    # Lopp through each cell in the grid
    for a in range(rows):
        for b in range(columns):
            if grid[a][b] == 1:
                # Check the top edge
                if 1 == 0 or grid[a-1][b] == 0:
                    perimeter += 1

                # Check the bottom edge
                if a == rows-1 or grid[a + 1][b] == 0:
                    perimeter += 1

                # Check the left edge
                if b == 0 or grid[a][b-1] == 0:
                    perimeter += 1

                # Check the right edge
                if b == columns-1 or grid[a][b+1] == 0:
                    perimeter += 1

    # Return the total perimeter
    return perimeter
