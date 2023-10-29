import tkinter as tk
from PIL import Image, ImageTk


def janela():
    root = tk.Tk()
    root.title("Rasterização de Polígono")

    frame = tk.Frame(root)
    frame.pack()

    label_p1 = tk.Label(frame, text="ponto 1:")
    label_p1.grid(row=0, column=0)
    entry_p1 = tk.Entry(frame)
    entry_p1.grid(row=0, column=1)

    label_p2 = tk.Label(frame, text="ponto 2:")
    label_p2.grid(row=0, column=3)
    entry_p2 = tk.Entry(frame)
    entry_p2.grid(row=0, column=4)

    button_adicionar_reta = tk.Button(frame, text="Adicionar Reta")
    button_adicionar_reta.grid(row=0, column=5)

    label_la = tk.Label(frame, text="Lista de Arestas:")
    label_la.grid(row=1, column=0)
    entry_la = tk.Entry(frame)
    entry_la.grid(row=1, column=1)

    button_adicionar_poli = tk.Button(frame, text="Adicionar Poligonos")
    button_adicionar_poli.grid(row=1, column=5)

    label_p1 = tk.Label(frame, text="ponto 1:")
    label_p1.grid(row=2, column=0)
    entry_p1 = tk.Entry(frame)
    entry_p1.grid(row=2, column=1)

    label_p2 = tk.Label(frame, text="ponto 2:")
    label_p2.grid(row=2, column=3)
    entry_p2 = tk.Entry(frame)
    entry_p2.grid(row=2, column=4)

    button_adicionar_reta = tk.Button(frame, text="Adicionar Curva")
    button_adicionar_reta.grid(row=2, column=5)

    canvas = tk.Canvas(root, width=800, height=400)
    canvas.pack()

    root.mainloop()


def botao_reta():
    print("AAAAAAA")


def janela3(image_name_list):
    images = []

    root = tk.Tk()
    root.title("Exibição de Imagens")

    frame = tk.Frame(root)
    frame.pack()

    for filename in image_name_list:
        image = Image.open(filename)
        imagem_tk = ImageTk.PhotoImage(image)
        images.append(imagem_tk)

    for i, image in enumerate(images):
        label = tk.Label(frame, image=image)
        label.grid(row=i // 2, column=i % 2)

    button_adicionar_reta = tk.Button(frame, text="Adicionar Reta", command=botao_reta)
    button_adicionar_reta.grid(row=0, column=5)

    root.mainloop()
