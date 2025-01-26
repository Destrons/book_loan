from database.db_connection import conectar
from models.book import Book

def cadastrar_livro(book):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO livros (titulo, autor, ano) VALUES (%s, %s, %s)",
                   (book.titulo, book.autor, book.ano))
    conn.commit()
    conn.close()

def buscar_livro(titulo=None, autor=None):
    conn = conectar()
    cursor = conn.cursor()
    
    query = "SELECT * FROM livros WHERE 1"
    params = []
    
    if titulo:
        query += " AND titulo LIKE %s"
        params.append(f"%{titulo}%")
    
    if autor:
        query += " AND autor LIKE %s"
        params.append(f"%{autor}%")
    
    cursor.execute(query, params)
    livros = cursor.fetchall()
    conn.close()
    
    return [Book(livro[1], livro[2], livro[3]) for livro in livros]

def emprestar_livro(id_livro):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE livros SET disponivel = FALSE WHERE id = %s", (id_livro,))
    conn.commit()
    conn.close()

def devolver_livro(id_livro):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE livros SET disponivel = TRUE WHERE id = %s", (id_livro,))
    conn.commit()
    conn.close()

def listar_livros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    conn.close()
    
    return [Book(livro[1], livro[2], livro[3]) for livro in livros]
