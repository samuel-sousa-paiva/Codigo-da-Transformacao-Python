import sqlite3

def conectar():
    return sqlite3.connect('clientes.db')

# Filtrar por letra inicial
def filtrar_por_inicial(letra):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM Clientes WHERE nome LIKE ?', (f'{letra}%',))
    resultado = cursor.fetchall()
    conexao.close()
    return resultado

# Contar total
def total_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT COUNT(*) FROM Clientes')
    total = cursor.fetchone()[0]
    conexao.close()
    return total

# Ordenar por nome
def ordenar_por_nome():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM Clientes ORDER BY nome ASC')
    ordenados = cursor.fetchall()
    conexao.close()
    return ordenados

# Testes
if __name__ == "__main__":
    print("\nClientes com nome começando em 'A':")
    for c in filtrar_por_inicial("A"):
        print(c)

    print(f"\nTotal de clientes: {total_clientes()}")

    print("\nClientes ordenados:")
    for c in ordenar_por_nome():
        print(c)