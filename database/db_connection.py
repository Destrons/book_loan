import mysql.connector

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="pypthon",
        password="123456789",
        database="book_loan"
    )