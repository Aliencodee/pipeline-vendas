import sqlite3

conexao = sqlite3.connect('dataset.db')
cursor = conexao.cursor()

criar_table = """ 
      CREATE TABLE IF NOT EXISTS vendas (
      id INT PRIMARY KEY,
      mes VARCHAR(20),
      trimestre VARCHAR(2),
      vendedor VARCHAR(50),
      categoria VARCHAR(50),
      qtd INT,
      preco_unit DECIMAL(10,2)
      )
""" 

cursor.execute(criar_table)

conexao.commit()
conexao.close()
