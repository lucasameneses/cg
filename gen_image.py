import matplotlib.pyplot as plt
import raster.raster_line as raster_line
import raster.raster_polygon as raster_polygon
import raster.raster_hermite as raster_hermite
from util import gen_matrix


def plot_reta(matrix_list, p1, p2):
    image_name_list = []
    for matrix in matrix_list:
        matrix = raster_line.raster_line(matrix, p1, p2)
        gen_img(image_name_list, matrix)


def plot_poli(matrix_list, edges_list):
    image_name_list = []
    for matrix in matrix_list:
        matrix = raster_polygon.raster_polygon(matrix, edges_list)
        gen_img(image_name_list, matrix)


def plot_curva(matrix_list, p1, p2, t1, t2, t):
    image_name_list = []
    for matrix in matrix_list:
        matrix = raster_hermite.generate_hermite(matrix, p1, p2, t1, t2, qtn=t)
        gen_img(image_name_list, matrix)


def reset_images(matrix_list):
    mxs = gen_matrix()
    for i in range(len(matrix_list)):
        matrix_list[i] = mxs[i]
        gen_img([], matrix_list[i])


def gen_img(image_name_list, matrix):
    plt.imshow(matrix, cmap="gray", origin="lower")
    plt.title("matrix {}x{}".format(len(matrix[0]), len(matrix)))
    image_name = "img/matrix{}x{}.jpg".format(len(matrix[0]), len(matrix))
    image_name_list.append(image_name)
    plt.savefig(image_name)
    plt.close()
