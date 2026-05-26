# Sistema de login com try-except

usuario_correto = "admin"
senha_correta = "1234"

tentativas = 3

while tentativas > 0:

    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    try:
        if usuario != usuario_correto:
            raise Exception("Usuário incorreto.")

        if senha != senha_correta:
            raise Exception("Senha incorreta.")

        print("Login realizado com sucesso!")
        break

    except Exception as erro:
        tentativas -= 1

        print("Erro:", erro)
        print("Tentativas restantes:", tentativas)

if tentativas == 0:
    print("Conta bloqueada.")