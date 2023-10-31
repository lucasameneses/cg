import util
import interface
import gen_image


def main():
    matrix_list = util.gen_matrix()

    image_name_list = []
    for matrix in matrix_list:
        gen_image.gen_img(image_name_list, matrix)

    interface.window(image_name_list, matrix_list)


if __name__ == "__main__":
    main()
