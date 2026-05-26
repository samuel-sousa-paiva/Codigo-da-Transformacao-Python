import requests

print("=== PREVISÃO DO TEMPO ===")

cidade = input("Digite a cidade: ")

api_key = "SUA_CHAVE_API"

url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"

try:

    resposta = requests.get(url)

    resposta.raise_for_status()

    dados = resposta.json()

    print("\n=== RESULTADO ===")
    print("Cidade:", dados["name"])
    print("Temperatura:", dados["main"]["temp"], "°C")
    print("Clima:", dados["weather"][0]["description"])

except requests.exceptions.HTTPError:
    print("Erro HTTP na requisição.")

except requests.exceptions.ConnectionError:
    print("Erro de conexão com a API.")

except requests.exceptions.Timeout:
    print("Tempo de conexão esgotado.")

except requests.exceptions.RequestException:
    print("Erro na requisição.")