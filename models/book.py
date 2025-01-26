class Book:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def __str__(self):
        return f"{self.titulo} de {self.autor} ({self.ano})"
