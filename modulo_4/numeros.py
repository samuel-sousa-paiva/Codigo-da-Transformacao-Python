numeros = []
pares = []
impares = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
        print("O número é par")

    else:
        impares.append(numero)
        print("O número é ímpar")

print("\nNúmeros pares:")
print(pares)

print("\nNúmeros ímpares:")
print(impares)