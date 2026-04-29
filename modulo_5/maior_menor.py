def maior_menor(lista):
    maior = lista[0]
    menor = lista[0]

    for num in lista:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    return maior, menor