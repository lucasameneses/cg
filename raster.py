import util
import math

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

def plot_reta(matrix, ponto1, ponto2):
    x1, y1 = util.denormalizar_coordenadas(*ponto1, len(matrix), len(matrix[0]))  # type: ignore
    x2, y2 = util.denormalizar_coordenadas(*ponto2, len(matrix), len(matrix[0]))  # type: ignore
    points = rasterize(x1, y1, x2, y2)
    return util.plot_rasterized(points, matrix)

def ponto_dentro(ponto, vertices):
    x, y = ponto
    num_vertices = len(vertices)
    dentro = False

    for i in range(num_vertices):
        xi, yi = vertices[i]
        xj, yj = vertices[(i + 1) % num_vertices]
        if ((yi < y <= yj) or (yj < y <= yi)) and (xi + (y - yi) / (yj - yi) * (xj - xi) < x):
            dentro = not dentro

    return dentro


def plot_poli(matrix, edges_list):

    poli = [(.0, .0), (.2, .2), (.4, .0), (.2, -.2)]

    # for i in range(len(edges_list)):
    #     ponto1 = edges_list[i]
    #     ponto2 = edges_list[(i + 1) % len(edges_list)]
    #     plot_reta(matrix, ponto1, ponto2)

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            x_norm, y_norm = util.normalizar_coordenadas(x, y, len(matrix), len(matrix[0]))
            if ponto_dentro((x_norm, y_norm), edges_list):
                matrix[x][y] = 1

    return matrix