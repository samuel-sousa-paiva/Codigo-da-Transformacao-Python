import random
import math

print("Bem-vindo ao Jogo da Adivinhação!")
print("Eu escolhi uma letra entre a e z.")
print("Tente adivinhá-lo!")

letra_secreta = random.randint(ord('a'), ord('z'))
tentativas = 0

while True:
    try:
        palpite = input("\nDigite seu palpite (uma letra): ").lower()
        
        if len(palpite) != 1 or not palpite.isalpha():
            print("Entrada inválida. Por favor, digite apenas uma letra.")
            continue

        tentativas += 1
        palpite_num = ord(palpite)
        diferenca = math.fabs(palpite_num - letra_secreta)

        if palpite_num == letra_secreta:
            print(f"\nParabéns! Você acertou a letra em {tentativas} tentativas!")
            break

        elif palpite_num < letra_secreta:
            print(f"Muito baixo! A diferença para a letra secreta é de aproximadamente {int(diferenca)} posições.")
        else:
            print(f"Muito alto! A diferença para a letra secreta é de aproximadamente {int(diferenca)} posições.")

    except:
        print("Erro inesperado, tente novamente.")