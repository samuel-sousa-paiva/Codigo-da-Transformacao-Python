lista = []

print("=== LISTA DE COMPRAS ===")

item1 = input("Digite o primeiro item: ")
lista.append(item1)

item2 = input("Digite o segundo item: ")
lista.append(item2)

item3 = input("Digite o terceiro item: ")
lista.append(item3)

item4 = input("Digite o quarto item: ")
lista.append(item4)

item5 = input("Digite o quinto item: ")
lista.append(item5)

print("\nLista atual:")
print(lista)

remover = input("\nQual item deseja remover? ")

if remover in lista:
    lista.remove(remover)
    print("Item removido com sucesso!")
else:
    print("Item não encontrado!")

print("\nLista atualizada:")
print(lista)