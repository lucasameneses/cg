import math
import matplotlib.pyplot as plt
import util
import interface


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


def plot_poli(matrix):
    poli = [(.0, .0), (.2, .2), (.4, .0), (.2, -.2)]

    # for i in range(len(poli)):
    #     ponto1 = poli[i]
    #     ponto2 = poli[(i + 1) % len(poli)]
    #     plot_reta(matrix, ponto1, ponto2)

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            x_norm, y_norm = util.normalizar_coordenadas(x, y, len(matrix), len(matrix[0]))
            if ponto_dentro((x_norm, y_norm), poli):
                matrix[x][y] = 1


def main():
    matrix = [[0 for _ in range(100)] for _ in range(100)]
    plot_poli(matrix)

    matrix1 = [[0 for _ in range(100)] for _ in range(100)]
    matrix2 = [[0 for _ in range(300)] for _ in range(300)]
    matrix3 = [[0 for _ in range(800)] for _ in range(600)]
    matrix4 = [[0 for _ in range(1920)] for _ in range(1080)]

    ponto1 = util.gen_point()
    ponto2 = util.gen_point()

    matrix1 = plot_reta(matrix1, ponto1, ponto2)
    matrix2 = plot_reta(matrix2, ponto1, ponto2)
    matrix3 = plot_reta(matrix3, ponto1, ponto2)
    matrix4 = plot_reta(matrix4, ponto1, ponto2)

    plt.imshow(matrix1, cmap='Blues', origin='lower')
    plt.grid()
    plt.savefig("matrix1.png")

    plt.imshow(matrix2, cmap='Blues', origin='lower')
    plt.grid()
    plt.savefig("matrix2.png")

    plt.imshow(matrix3, cmap='Blues', origin='lower')
    plt.grid()
    plt.savefig("matrix3.png")

    plt.imshow(matrix4, cmap='Blues', origin='lower')
    plt.grid()
    plt.savefig("matrix4.png")

    plt.imshow(matrix, cmap='Blues', origin='lower')
    plt.grid()
    plt.savefig("matrix.png")

    interface.janela2()


if __name__ == "__main__":
    main()
