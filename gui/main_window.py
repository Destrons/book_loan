import tkinter as tk
from tkinter import messagebox
from utils.book_manager import cadastrar_livro, buscar_livro, emprestar_livro, devolver_livro, listar_livros
from models.book import Book

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestão de Biblioteca")
        
        # Widgets
        self.create_widgets()

    def create_widgets(self):
        self.titulo_label = tk.Label(self.root, text="Título")
        self.titulo_label.grid(row=0, column=0)
        
        self.titulo_entry = tk.Entry(self.root)
        self.titulo_entry.grid(row=0, column=1)

        self.autor_label = tk.Label(self.root, text="Autor")
        self.autor_label.grid(row=1, column=0)
        
        self.autor_entry = tk.Entry(self.root)
        self.autor_entry.grid(row=1, column=1)

        self.ano_label = tk.Label(self.root, text="Ano")
        self.ano_label.grid(row=2, column=0)
        
        self.ano_entry = tk.Entry(self.root)
        self.ano_entry.grid(row=2, column=1)

        self.add_button = tk.Button(self.root, text="Cadastrar Livro", command=self.cadastrar_livro)
        self.add_button.grid(row=3, column=0, columnspan=2)

        self.buscar_button = tk.Button(self.root, text="Buscar Livro", command=self.buscar_livro)
        self.buscar_button.grid(row=4, column=0, columnspan=2)

        self.livros_listbox = tk.Listbox(self.root, height=10, width=50)
        self.livros_listbox.grid(row=5, column=0, columnspan=2)

    def cadastrar_livro(self):
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        ano = self.ano_entry.get()

        if not titulo or not autor or not ano:
            messagebox.showerror("Erro", "Preencha todos os campos")
            return

        book = Book(titulo, autor, int(ano))
        cadastrar_livro(book)
        messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")

    def buscar_livro(self):
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        
        livros = buscar_livro(titulo, autor)
        
        self.livros_listbox.delete(0, tk.END)
        
        for livro in livros:
            self.livros_listbox.insert(tk.END, str(livro))

    def emprestar_livro(self):
        pass

    def devolver_livro(self):
        pass

    def listar_livros(self):
        livros = listar_livros()
        for livro in livros:
            self.livros_listbox.insert(tk.END, str(livro))

def main():
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
