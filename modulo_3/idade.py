idade = int(input("Digite sua idade: "))

if idade <= 12:
    print("Você é Criança")

elif idade <= 17:
    print("Você é Adolescente")

elif idade <= 59:
    print("Você é Adulto")

else:
    print("Você é Idoso")