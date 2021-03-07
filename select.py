import psycopg2

# Conecta no Banco de Dados #
con = psycopg2.connect(
    database="pycodebr",
    user="postgres",
    password="1234",
    host="127.0.0.1",
    port="5432"
)

# Cria e executa a Query #
cur = con.cursor()
cur.execute("SELECT cliente_id, nome, email FROM clientes")
rows = cur.fetchall()

# Mostra resultados do SELECT #
print(rows)
for row in rows:
    print("CLIENTE_ID =", row[0])
    print("NOME =", row[1])
    print("EMAIL =", row[2])
con.close()