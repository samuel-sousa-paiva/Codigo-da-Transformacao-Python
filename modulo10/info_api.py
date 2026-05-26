import requests

print("=== PREVISÃO DO TEMPO ===")

cidade = input("Digite a cidade: ")

api_key = "SUA_CHAVE_API"

url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"

resposta = requests.get(url)

dados = resposta.json()

if resposta.status_code == 200:

    temperatura = dados["main"]["temp"]
    clima = dados["weather"][0]["description"]

    print("\n=== RESULTADO ===")
    print("Cidade:", dados["name"])
    print("Temperatura:", temperatura, "°C")
    print("Condição climática:", clima)

else:
    print("Erro ao buscar informações da cidade.")