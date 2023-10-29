import tkinter as tk

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

def janela2():
    root = tk.Tk()
    root.title("Mostrando Imagens")

    imagem1 = tk.PhotoImage(file="matrix1.png")
    imagem2 = tk.PhotoImage(file="matrix2.png")
    imagem3 = tk.PhotoImage(file="matrix3.png")
    imagem4 = tk.PhotoImage(file="matrix4.png")

    label1 = tk.Label(root, image=imagem1)
    label2 = tk.Label(root, image=imagem2)
    label3 = tk.Label(root, image=imagem3)
    label4 = tk.Label(root, image=imagem4)

    label1.grid(row=0, column=0)
    label2.grid(row=0, column=1)
    label3.grid(row=1, column=0)
    label4.grid(row=1, column=1)

    root.mainloop()

# def janela3():
#     root = tk.Tk()

#     imagem = tk.PhotoImage(file="matrix2.png")
#     w = tk.Label(root, image=imagem)
#     w.imagem = imagem
#     w.pack()

#     root.mainloop()
