import math
import matplotlib.pyplot as plt
import util
import interface
import raster


def insert_points(mx, points):
    for x, y in points:
        x = math.floor(x)
        y = math.floor(y)

        if (y > 0 and x > 0) and (y < len(mx) and x < len(mx[0])):
            mx[y][x] = 1


def plot_reta(matrix_list, p1, p2):
    image_name_list = []
    for matrix in matrix_list:
        matrix = raster.plot_reta(matrix, p1, p2)
        gen_img(image_name_list, matrix)


def plot_poli(matrix_list, edges_list):
    image_name_list = []
    for matrix in matrix_list:
        matrix = raster.plot_poli2(matrix, edges_list)
        gen_img(image_name_list, matrix)


def plot_curva(matrix_list, p1, p2, t1, t2, t):
    image_name_list = []
    for matrix in matrix_list:
        pts = raster.generate_hermite_pts(matrix, p1, p2, t1, t2, qtn=t)
        insert_points(matrix, pts)
        gen_img(image_name_list, matrix)


def gen_img(image_name_list, matrix):
    plt.imshow(matrix, cmap='gray', origin='lower')
    plt.grid()
    image_name = "matrix{}x{}.jpg".format(len(matrix[0]), len(matrix))
    image_name_list.append(image_name)
    plt.savefig(image_name)
    plt.close()


def main():
    matrix_list = util.gen_matrix()

    p1, p2 = (-.6, 0), (.6, 0)
    t1, t2 = (.5, 6), (0, 0)

    image_name_list = []
    for matrix in matrix_list:
        gen_img(image_name_list, matrix)

    interface.janela(image_name_list, matrix_list)


if __name__ == "__main__":
    main()
