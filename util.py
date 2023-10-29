import math
import random


def delta(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    # length = math.sqrt(dx ** 2 + dy ** 2)

    # if length != 0:
    #     dx /= length
    #     dy /= length

    return dx, dy


def add_point(x, y, points):
    points.append((round(x), round(y)))


def normalizar_coordenadas(x, y, largura, altura):
    x_normalizado = (2 * x) / (largura - 1) - 1
    y_normalizado = (2 * y) / (altura - 1) - 1
    return x_normalizado, y_normalizado


def denormalizar_coordenadas(x_norm, y_norm, largura, altura):
    rmin=-1
    rmax=1
    xs = (x_norm - rmin) / (rmax - rmin)
    ys = (y_norm - rmin) / (rmax - rmin)

    xs *= altura - 0
    ys *= largura - 0

    xs += 0
    ys += 0

    print(f'({xs}, {ys})')
    return xs, ys

def scale2d_interval(vec, scale, rmin=-1, rmax=1):
    svec = []

    scale_x, scale_y = scale
    for point in vec:
        x = point[0]
        xs = (x - rmin) / (rmax - rmin)
        xs *= scale_x - 0
        xs += 0

        y = point[1]
        ys = (y - rmin) / (rmax - rmin)
        ys *= scale_y - 0
        ys += 0

        svec.append((xs, ys))

    return tuple(svec)


def gen_point():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    return x, y


def plot_rasterized(points, matrix):
    for x, y in points:
        if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]):
            matrix[math.floor(y)][math.floor(x)] = 1

    return matrix
