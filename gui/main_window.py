import tkinter as tk
from tkinter import messagebox

def adicionar_livro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    ano = entry_ano.get()
    if titulo and autor and ano:
        cadastrar_livro(titulo, autor, ano)
        messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
    else:
        messagebox.showwarning("Erro", "Todos os campos são obrigatórios!")

root = tk.Tk()
root.title("Sistema de Biblioteca")

label_titulo = tk.Label(root, text="Título")
label_titulo.grid(row=0, column=0)
entry_titulo = tk.Entry(root)
entry_titulo.grid(row=0, column=1)

label_autor = tk.Label(root, text="Autor")
label_autor.grid(row=1, column=0)
entry_autor = tk.Entry(root)
entry_autor.grid(row=1, column=1)

label_ano = tk.Label(root, text="Ano")
label_ano.grid(row=2, column=0)
entry_ano = tk.Entry(root)
entry_ano.grid(row=2, column=1)

btn_adicionar = tk.Button(root, text="Adicionar Livro", command=adicionar_livro)
btn_adicionar.grid(row=3, column=0, columnspan=2)

root.mainloop()
