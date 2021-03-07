import psycopg2

# Conecta no Banco de Dados #
con = psycopg2.connect(
    database="pycodebr",
    user="postgres",
    password="1234",
    host="127.0.0.1",
    port="5432"
)

# Cria a Query #
cur = con.cursor()

# Insere registros #
cur.execute("INSERT INTO clientes (nome, email) VALUES ('FELIPE', 'pycodebr@gmail.com')")
cur.execute("INSERT INTO clientes (nome, email) VALUES ('MARCOS', 'marcos@gmail.com')")
cur.execute("INSERT INTO clientes (nome, email) VALUES ('JOANA', 'joana@gmail.com')")

# Salva registros #
con.commit()
print("Registros salvos com sucesso!")
con.close()