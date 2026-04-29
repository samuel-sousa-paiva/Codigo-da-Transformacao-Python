aluno = {}

while True:
    print("\n1 - Cadastrar aluno")
    print("2 - Ver dados do aluno")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        
        notas = []
        for i in range(3):
            nota = float(input(f"Digite a nota {i+1}: "))
            notas.append(nota)

        aluno["nome"] = nome
        aluno["idade"] = idade
        aluno["notas"] = notas

        print("Aluno cadastrado!")

    elif opcao == "2":
        if aluno:
            print("\n--- Dados do Aluno ---")
            print("Nome:", aluno["nome"])
            print("Idade:", aluno["idade"])
            print("Notas:", aluno["notas"])
        else:
            print("Nenhum aluno cadastrado!")

    elif opcao == "3":
        break

    else:
        print("Opção inválida!")