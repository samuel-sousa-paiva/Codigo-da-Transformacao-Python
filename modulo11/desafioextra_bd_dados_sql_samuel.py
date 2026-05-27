import sqlite3

def conectar_tarefas():
    return sqlite3.connect('tarefas.db')

def criar_tabela():
    conexao = conectar_tarefas()
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'Pendente'
    )
    ''')
    conexao.commit()
    conexao.close()
    print("Sistema de tarefas pronto!")

def adicionar(descricao):
    conexao = conectar_tarefas()
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO Tarefas (descricao) VALUES (?)', (descricao,))
    conexao.commit()
    conexao.close()
    print("Tarefa adicionada!")

def listar():
    conexao = conectar_tarefas()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM Tarefas')
    tarefas = cursor.fetchall()
    conexao.close()
    return tarefas

def excluir(id_tarefa):
    conexao = conectar_tarefas()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM Tarefas WHERE id = ?', (id_tarefa,))
    if cursor.rowcount > 0:
        print("Tarefa removida!")
    else:
        print("Tarefa não encontrada.")
    conexao.commit()
    conexao.close()

# Menu
if __name__ == "__main__":
    criar_tabela()
    while True:
        print("\n==== GERENCIADOR DE TAREFAS ====")
        print("1. Adicionar Tarefa")
        print("2. Ver Todas")
        print("3. Excluir Tarefa")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar(input("Descrição da tarefa: "))
        elif opcao == "2":
            for t in listar():
                print(f"ID {t[0]} | {t[1]} | Status: {t[2]}")
        elif opcao == "3":
            try:
                excluir(int(input("ID da tarefa: ")))
            except ValueError:
                print("Digite um número válido.")
        elif opcao == "4":
            break