import matplotlib.pyplot as plt


# GRAPHICS TOOLS


def show_image(grid: list) -> list:
    r"Shows the changes generated by the A star algorithm"
    ptl.imshow(grid)
    return grid


# GENERATE ROADS