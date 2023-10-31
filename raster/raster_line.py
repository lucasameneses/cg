import util
import math


def raster_line(matrix, ponto1, ponto2):
    x1, y1 = util.scale_dot(*ponto1, len(matrix), len(matrix[0]))  # type: ignore
    x2, y2 = util.scale_dot(*ponto2, len(matrix), len(matrix[0]))  # type: ignore
    points = rasterize(x1, y1, x2, y2)
    return util.plot_rasterized(points, matrix)


def rasterize(x1, y1, x2, y2):
    dx, dy = util.delta(x1, y1, x2, y2)

    x, y = x1, y1
    points = []

    m = 0 if dx == 0 else dy / dx
    b = y - m * x

    util.add_point(x, y, points)

    if math.fabs(dx) >= math.fabs(dy):
        step_x = 1 if x1 < x2 else -1
        while x != x2:
            x += step_x
            y = m * x + b
            util.add_point(x, y, points)
    else:
        step_y = 1 if y1 < y2 else -1
        while y != y2:
            y += step_y
            if m != 0:
                x = (y - b) / m
            util.add_point(x, y, points)

    return points
