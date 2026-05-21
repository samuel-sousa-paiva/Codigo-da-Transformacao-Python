import csv

# Função para adicionar notas
def adicionar_nota(nome, disciplina, nota):
    # Abre o arquivo no modo de adição
    with open("notas_alunos.csv", "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, disciplina, nota])

# Função para carregar e exibir notas
def exibir_notas():
    with open("notas_alunos.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        print("=== Notas dos Alunos ===")
        for linha in leitor:
            print(f"Aluno: {linha[0]} | Disciplina: {linha[1]} | Nota: {linha[2]}")

# Execução
adicionar_nota("Lucas", "Matemática", 8.5)
adicionar_nota("Beatriz", "Português", 9.0)
exibir_notas()