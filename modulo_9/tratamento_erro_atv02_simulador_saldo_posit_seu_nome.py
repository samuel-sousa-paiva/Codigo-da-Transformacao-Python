# Simulação de conta bancária

class SaldoInsuficienteError(Exception):
    pass


saldo = 1000

try:
    saque = float(input("Digite o valor do saque: "))

    if saque > saldo:
        raise SaldoInsuficienteError

    saldo -= saque

    print("Saque realizado com sucesso!")
    print("Saldo restante:", saldo)

except SaldoInsuficienteError:
    print("Erro: saldo insuficiente.")

except ValueError:
    print("Erro: digite um número válido.")