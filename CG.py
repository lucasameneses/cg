import matplotlib.pyplot as plt
import util
import interface
import raster


def main():
    matrix_list = util.gen_matrix()

    ponto1 = util.gen_point()
    ponto2 = util.gen_point()
    ponto3 = util.gen_point()
    ponto4 = util.gen_point()

    # edges_list = [(ponto1, ponto2), (ponto2, ponto3), (ponto3, ponto4), (ponto4, ponto1)]

    edges_list1 = [(-.2,-.2),(-.2,-.4),(-.4,-.4),(-.4,-.2)]

    ponto1 = util.gen_point()
    ponto2 = util.gen_point()
    ponto3 = util.gen_point()
    ponto4 = util.gen_point()

    edges_list2 = [(.2,.2),(.2,.4),(.4,.4),(.4,.2)]

    image_name_list = []
    for matrix in matrix_list:
        matrix = raster.plot_poli(matrix, edges_list1)
        matrix = raster.plot_poli(matrix, edges_list2)
        plt.imshow(matrix, cmap='gray', origin='lower')
        plt.grid()
        image_name = "matrix{}x{}.jpg".format(len(matrix[0]), len(matrix))
        image_name_list.append(image_name)
        plt.savefig(image_name)
        plt.close()

    interface.janela3(image_name_list)


if __name__ == "__main__":
    main()
