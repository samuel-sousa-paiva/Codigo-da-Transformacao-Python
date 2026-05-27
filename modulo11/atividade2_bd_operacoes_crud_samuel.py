import sqlite3

def conectar():
    return sqlite3.connect('clientes.db')

# Inserir
def inserir_cliente(nome, email):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute('INSERT INTO Clientes (nome, email) VALUES (?, ?)', (nome, email))
        conexao.commit()
        print(f"Cliente {nome} cadastrado!")
    except sqlite3.IntegrityError:
        print("E-mail já cadastrado.")
    finally:
        conexao.close()

# Consultar
def consultar_todos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM Clientes')
    return cursor.fetchall()

# Atualizar
def atualizar_cliente(id_cliente, novo_nome=None, novo_email=None):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT nome, email FROM Clientes WHERE id = ?', (id_cliente,))
    atual = cursor.fetchone()
    if not atual:
        print("Cliente não encontrado.")
        conexao.close()
        return
    nome = novo_nome if novo_nome else atual[0]
    email = novo_email if novo_email else atual[1]
    cursor.execute('UPDATE Clientes SET nome = ?, email = ? WHERE id = ?', (nome, email, id_cliente))
    conexao.commit()
    print(f"Cliente {id_cliente} atualizado!")
    conexao.close()

# Deletar
def deletar_cliente(id_cliente):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM Clientes WHERE id = ?', (id_cliente,))
    if cursor.rowcount > 0:
        print(f"Cliente {id_cliente} removido!")
    else:
        print("Cliente não encontrado.")
    conexao.commit()
    conexao.close()

# Testes
if __name__ == "__main__":
    inserir_cliente("Ana Silva", "ana@email.com")
    inserir_cliente("Bruno Costa", "bruno@email.com")

    print("\nTodos os clientes:")
    for c in consultar_todos():
        print(c)

    atualizar_cliente(1, novo_nome="Ana Carolina Silva")

    deletar_cliente(2)

    print("\nApós alterações:")
    for c in consultar_todos():
        print(c)