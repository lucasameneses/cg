import raster.raster_line as raster_line
import util
import math


def generate_hermite(matrix, p1, p2, t1, t2, step=.1, qtn: int = None):
    points = []
    if qtn:
        step = 1 / qtn
    t = 0
    while t <= 1:
        point = generate_hermite_point(p1, p2, t1, t2, t)
        points.append(point)
        t += step
    vectors = []
    for i in range(1, len(points)):
        pa = points[i - 1]
        pp = points[i]
        vectors.append((pa, pp))
    ptx = []
    for vec in vectors:
        x1, y1 = util.scale_dot(*vec[0], len(matrix), len(matrix[0]))
        x2, y2 = util.scale_dot(*vec[1], len(matrix), len(matrix[0]))
        ts = raster_line.rasterize(x1, y1, x2, y2)
        ptx.extend(ts)

    insert_points(matrix, ptx)
    return matrix


def insert_points(matrix, points):
    for x, y in points:
        x = math.floor(x)
        y = math.floor(y)

        if (y > 0 and x > 0) and (y < len(matrix) and x < len(matrix[0])):
            matrix[y][x] = 1


def generate_hermite_point(p1, p2, t1, t2, t):
    # P(t) = THGh
    # Will be implemented into parts. Expanding the Linear Algebra
    pt0 = 2 * (t * t * t) - 3 * (t * t) + 1
    pt1 = -2 * (t * t * t) + 3 * (t * t)
    pt2 = (t * t * t) - 2 * (t * t) + t
    pt3 = (t * t * t) - (t * t)

    x = pt0 * p1[0] + pt1 * p2[0] + pt2 * t1[0] + pt3 * t2[0]
    y = pt0 * p1[1] + pt1 * p2[1] + pt2 * t1[1] + pt3 * t2[1]

    return x, y
