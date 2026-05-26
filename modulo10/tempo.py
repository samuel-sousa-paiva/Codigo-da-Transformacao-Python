import requests

print("=== PREVISÃO DO TEMPO ===")

cidade = input("Digite o nome da cidade: ")

api_key = "SUA_CHAVE_API"

url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric"

resposta = requests.get(url)

dados = resposta.json()

if resposta.status_code == 200:

    print("\n=== RESULTADO ===")
    print("Cidade:", dados["name"])
    print("Temperatura:", dados["main"]["temp"], "°C")
    print("Clima:", dados["weather"][0]["description"])

else:
    print("Erro ao buscar cidade.")
    print("Verifique o nome da cidade ou a chave da API.")