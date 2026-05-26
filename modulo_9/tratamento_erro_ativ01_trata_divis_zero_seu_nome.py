# Calculadora com try-except

print("=== CALCULADORA ===")

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    operador = input("Digite o operador (+, -, *, /): ")

    if operador == "+":
        resultado = num1 + num2

    elif operador == "-":
        resultado = num1 - num2

    elif operador == "*":
        resultado = num1 * num2

    elif operador == "/":
        resultado = num1 / num2

    else:
        print("Operador inválido!")
        resultado = None

    if resultado is not None:
        print("Resultado:", resultado)

except ValueError:
    print("Erro: digite apenas números.")

except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")