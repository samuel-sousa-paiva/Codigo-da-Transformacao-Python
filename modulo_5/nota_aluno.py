nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 9:
    print("Aprovado (Excelente)")
elif media >= 8:
    print("Aprovado (Muito bom)")
elif media >= 7:
    print("Aprovado")
elif media >= 6:
    print("Recuperação")
elif media >= 5:
    print("Recuperação")        
else:
    print("Reprovado")