# Validação de entrada

try:
    idade = int(input("Digite sua idade: "))

    if idade <= 0:
        print("A idade deve ser um número positivo.")

    else:
        print("Idade válida!")

except ValueError:
    print("Erro: digite apenas números.")