print('\Calculadora simples - Python')
num_um = input('Digite o primeiro número: ')
num_dois = input('Digite o segundo número: ')
operacao = input('Escolha a operação: 1-> +, 2-> -, 3-> *, 4-> /')


# result = int(num_um) / int(num_dois)  #1 divisão
# result = int(num_um) * int(num_dois)  #2 multiplicação
# result = int(num_um) + int(num_dois)  #3 soma
# result = int(num_um) - int(num_dois)  #4 subtração

if operacao == '1':
    result = int(num_um) + int(num_dois) 
    print(f'O resultado da soma é: {result}')

elif operacao == '2':
    result = int(num_um) - int(num_dois)  # Subtração
    print(f'O resultado da subtração é: {result}')

elif operacao == '3':
    result = int(num_um) * int(num_dois) # Multiplicação
    print(f'O resultado da multiplicação é: {result}')

elif operacao == '4':
    result = int(num_um) / int(num_dois) # Divisão
    print(f'O resultado da divisão é: {result}')

else:
    print("Número não é válido, tente novamente!")
