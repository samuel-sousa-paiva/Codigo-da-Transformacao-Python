import json

clientes = {
    "cliente1": {"nome": "Carlos", "idade": 35, "email": "carlos@email.com"},
    "cliente2": {"nome": "Ana", "idade": 29, "email": "ana@email.com"}
}

# Salvar dicionário em arquivo JSON
with open("clientes.json", "w", encoding="utf-8") as arquivo:
    json.dump(clientes, arquivo, indent=4, ensure_ascii=False)

# Carregar e exibir os dados
with open("clientes.json", "r", encoding="utf-8") as arquivo:
    dados_carregados = json.load(arquivo)

print("=== Dados dos clientes (JSON) ===")
print(dados_carregados)