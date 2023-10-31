import math

import util


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


def ponto_dentro(ponto, edges_list):
    x, y = ponto
    dentro = False

    for edge in edges_list:
        ponto1, ponto2 = edge
        x1, y1 = ponto1
        x2, y2 = ponto2

        if ((y1 < y <= y2) or (y2 < y <= y1)) and (x1 + (y - y1) / (y2 - y1) * (x2 - x1) < x):
            dentro = not dentro

    return dentro


def plot_poli2(matrix, edges_list):

    for i in range(len(edges_list)):
        edge = edges_list[i]
        ponto1 = edge[0]
        ponto2 = edge[1]
        plot_reta(matrix, ponto1, ponto2)

    edges_list = escalar_arestas(edges_list, len(matrix), len(matrix[0]))

    matriz = preencher_poligono(matrix, edges_list)

    return matrix


def preencher_poligono(matrix, edges_list):
    def get_intersecoes(y, arestas):
        intersecoes = []
        for aresta in arestas:
            x1, y1 = aresta[0]
            x2, y2 = aresta[1]

            if y1 == y2:
                continue

            if y1 > y2:
                x1, y1, x2, y2 = x2, y2, x1, y1

            if y1 <= y < y2:
                x_intersecao = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                intersecoes.append(x_intersecao)

        return sorted(intersecoes)

    for y in range(len(matrix)):
        intersecoes = get_intersecoes(y, edges_list)
        for i in range(0, len(intersecoes), 2):
            for x in range(int(intersecoes[i]), int(intersecoes[i + 1]) + 1):
                matrix[y][x] = 1

    return matrix


def escalar_arestas(edges_list, largura, altura):
    edges_scaled = []
    for edge in edges_list:
        scaled_edge = [(util.denormalizar_coordenadas(x_norm, y_norm, largura, altura)) for x_norm, y_norm in edge]
        edges_scaled.append(scaled_edge)
    return edges_scaled


def generate_hermite_pts(matrix, p1, p2, t1, t2, step=.1, qtn: int = None):
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
        x1, y1 = util.denormalizar_coordenadas(*vec[0], len(matrix), len(matrix[0]))
        x2, y2 = util.denormalizar_coordenadas(*vec[1], len(matrix), len(matrix[0]))
        ts = rasterize(x1, y1, x2, y2)
        ptx.extend(ts)
    return ptx


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
