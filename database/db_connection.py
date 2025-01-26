import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        port="3306",
        user="pypthon",
        password="123456789",
        database="book_loan"
    )