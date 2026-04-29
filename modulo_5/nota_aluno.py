nota = calcular_media()

if nota >= 90:
    print("Aprovado (Excelente)")
elif nota >= 80:
    print("Aprovado (Muito bom)")
elif nota >= 70:
    print("Aprovado")
elif nota >= 60:
    print("Recuperação")
else:
    print("Reprovado")