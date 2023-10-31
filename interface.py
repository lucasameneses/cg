import tkinter as tk
from PIL import Image, ImageTk
import CG


def importante(val):
    string = val.replace(" ", "")
    string = string.replace(",", " ")
    valores = string.split()
    return tuple(float(valor) for valor in valores)


def atualizar_imagens(image_name_list, images, imagem_label):
    for i, image_name in enumerate(image_name_list):
        imagem_tk = ImageTk.PhotoImage(Image.open(image_name))
        images[i] = imagem_tk  # Atualize a lista de imagens
        label = tk.Label(imagem_label, image=imagem_tk)
        label.grid(row=i // 2, column=i % 2)


def reta_control(root, matrix_list, image_name_list, images, imagem_label):
    def botao_reta():
        p1 = importante(entry_p1.get())
        p2 = importante(entry_p2.get())
        CG.plot_reta(matrix_list, p1, p2)
        atualizar_imagens(image_name_list, images, imagem_label)

    reta_frame = tk.Frame(root, padx=10, pady=20)
    reta_frame.grid(row=0, column=0)

    label_reta = tk.Label(reta_frame, text="Retas")
    label_reta.grid(row=0, column=0)

    label_p1 = tk.Label(reta_frame, text="ponto 1:")
    label_p1.grid(row=1, column=0)
    entry_p1 = tk.Entry(reta_frame)
    entry_p1.grid(row=1, column=1)

    label_p2 = tk.Label(reta_frame, text="ponto 2:")
    label_p2.grid(row=1, column=2)
    entry_p2 = tk.Entry(reta_frame)
    entry_p2.grid(row=1, column=3)

    button_adicionar_reta = tk.Button(reta_frame, text="Adicionar Reta", command=botao_reta)
    button_adicionar_reta.grid(row=1, column=4)


def poli_control(root, image_name_list, images, imagem_label):
    def botao_poli():
        print(entry_el.get())
        # TODO: coisa os negocios aqui pra poder ler do jeito certo
        atualizar_imagens(image_name_list, images, imagem_label)

    poli_frame = tk.Frame(root, padx=10, pady=20)
    poli_frame.grid(row=1, column=0)

    label_poli = tk.Label(poli_frame, text="Poligonos")
    label_poli.grid(row=0, column=0)

    label_el = tk.Label(poli_frame, text="Lista de Arestas:")
    label_el.grid(row=1, column=0)
    entry_el = tk.Entry(poli_frame)
    entry_el.grid(row=1, column=1)

    button_adicionar_poli = tk.Button(poli_frame, text="Adicionar Poligonos", command=botao_poli)
    button_adicionar_poli.grid(row=1, column=4)


def curva_control(root, matrix_list, image_name_list, images, imagem_label):
    def botao_curva():
        p1 = importante(entry_p1.get())
        p2 = importante(entry_p2.get())
        t1 = importante(entry_t1.get())
        t2 = importante(entry_t2.get())
        t = int(entry_t.get())
        CG.plot_curva(matrix_list, p1, p2, t1, t2, t)
        atualizar_imagens(image_name_list, images, imagem_label)

    curva_frame = tk.Frame(root, padx=10, pady=20)
    curva_frame.grid(row=2, column=0)

    label_curva = tk.Label(curva_frame, text="Curva")
    label_curva.grid(row=0, column=0)

    label_p1 = tk.Label(curva_frame, text="ponto 1:")
    label_p1.grid(row=1, column=0)
    entry_p1 = tk.Entry(curva_frame)
    entry_p1.grid(row=1, column=1)

    label_t1 = tk.Label(curva_frame, text="tangente 1:")
    label_t1.grid(row=2, column=0)
    entry_t1 = tk.Entry(curva_frame)
    entry_t1.grid(row=2, column=1)

    label_p2 = tk.Label(curva_frame, text="ponto 2:")
    label_p2.grid(row=1, column=2)
    entry_p2 = tk.Entry(curva_frame)
    entry_p2.grid(row=1, column=3)

    label_t2 = tk.Label(curva_frame, text="tangente 2:")
    label_t2.grid(row=2, column=2)
    entry_t2 = tk.Entry(curva_frame)
    entry_t2.grid(row=2, column=3)

    label_t = tk.Label(curva_frame, text="T:")
    label_t.grid(row=3, column=0)
    entry_t = tk.Entry(curva_frame)
    entry_t.grid(row=3, column=1)

    button_adicionar_curva = tk.Button(curva_frame, text="Adicionar Curva", command=botao_curva)
    button_adicionar_curva.grid(row=3, column=4)




def janela(image_name_list, matrix_list):

    def rolar(event):
        canvas.configure(scrollregion=canvas.bbox("all"), yscrollincrement=20, xscrollincrement=20)

    root = tk.Tk()
    root.title("Trabalho do DIABO")

    canvas = tk.Canvas(root)
    canvas.pack(fill="both", expand=True)

    scrollbar = tk.Scrollbar(root, orient="horizontal", command=canvas.xview)
    scrollbar.pack(side="bottom", fill="x")
    canvas.configure(xscrollcommand=scrollbar.set)

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    frame_img = tk.Frame(frame)
    frame_img.grid(row=0, column=0)
    imagem_label = tk.Label(frame_img)
    imagem_label.pack()

    images = []
    for filename in image_name_list:
        imagem_tk = ImageTk.PhotoImage(Image.open(filename))
        images.append(imagem_tk)

    for i, imageh in enumerate(images):
        label = tk.Label(imagem_label, image=imageh)
        label.grid(row=i // 2, column=i % 2)

    frame_control = tk.Frame(frame)
    frame_control.grid(row=0, column=1)

    reta_control(frame_control, matrix_list, image_name_list, images, imagem_label)

    poli_control(frame_control, image_name_list, images, imagem_label)

    curva_control(frame_control, matrix_list, image_name_list, images, imagem_label)

    canvas.bind("<Configure>", rolar)

    root.mainloop()
