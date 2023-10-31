import math
import random


def delta(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    return dx, dy


def add_point(x, y, points):
    points.append((round(x), round(y)))

def importante(val):
    string = val.replace(" ", "")
    string = string.replace(",", " ")
    valores = string.split()
    return tuple(float(valor) for valor in valores)


def denormalizar_coordenadas(x_norm, y_norm, largura, altura):
    rmin = -1
    rmax = 1
    xs = (x_norm - rmin) / (rmax - rmin)
    ys = (y_norm - rmin) / (rmax - rmin)

    xs *= altura - 0
    ys *= largura - 0

    xs += 0
    ys += 0

    return round(xs), round(ys)


def gen_point():
    x = round(random.uniform(-1, 1), 2)
    y = round(random.uniform(-1, 1), 2)
    print(f'({x}, {y})')
    return x, y


def plot_rasterized(points, matrix):
    for x, y in points:
        if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]):
            matrix[math.floor(y)][math.floor(x)] = 1

    return matrix


def gen_matrix():
    resolution_list = [(100, 100), (300, 300), (800, 600), (1920, 1080)]
    matrix_list = []

    for resolution in resolution_list:
        matrix = [[0 for _ in range(resolution[0])] for _ in range(resolution[1])]
        matrix_list.append(matrix)

    return matrix_list
