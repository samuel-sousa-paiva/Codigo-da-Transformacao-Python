
with open("dados.txt", "w") as arquivo:
    arquivo.write("Nome: Samuel paiva\n")
    arquivo.write("Curso: programação\n")


with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()

print("Conteúdo do arquivo:")
print(conteudo)