import psycopg2

conexao = psycopg2.connect(
    dbname="conecteste",
    user="postgres",
    password="Watanabe#13031003",
    host="localhost",
    port="5432"
)

cursor = conexao.cursor()

cursor.execute(
    "INSERT INTO veiculos (placa, marcaModelo, tipo) VALUES (%s, %s, %s)",
    ("TST1234", "Teste Modelo", "carro")
)

conexao.commit()

cursor.close()
conexao.close()
print("Veículo inserido!")