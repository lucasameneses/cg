import util
import raster.raster_line as raster_line


def raster_polygon(matrix, edges_list):
    for i in range(len(edges_list)):
        edge = edges_list[i]
        dot1 = edge[0]
        dot2 = edge[1]
        raster_line.raster_line(matrix, dot1, dot2)

    edges_list = scale_edges(edges_list, len(matrix), len(matrix[0]))

    matriz = fill_polygon(matrix, edges_list)

    return matrix


def scale_edges(edges_list, width, height):
    edges_scaled = []
    for edge in edges_list:
        scaled_edge = [(util.scale_dot(x_norm, y_norm, width, height)) for x_norm, y_norm in edge]
        edges_scaled.append(scaled_edge)
    return edges_scaled


def fill_polygon(matrix, edges_list):
    for y in range(len(matrix)):
        intersection = get_intersection(y, edges_list)
        for i in range(0, len(intersection), 2):
            for x in range(int(intersection[i]), int(intersection[i + 1]) + 1):
                matrix[y][x] = 1

    return matrix


def get_intersection(y, edge_list):
    intersection_list = []
    for edge in edge_list:
        x1, y1 = edge[0]
        x2, y2 = edge[1]

        if y1 == y2:
            continue

        if y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        if y1 <= y < y2:
            x_intersection = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            intersection_list.append(x_intersection)

    return sorted(intersection_list)
