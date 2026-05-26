# Busca de filmes usando API TMDB

import requests

print("=== BUSCA DE FILMES ===")

filme = input("Digite o nome do filme: ")

api_key = "SUA_CHAVE_API"

url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={filme}&language=pt-BR"

try:

    resposta = requests.get(url)

    resposta.raise_for_status()

    dados = resposta.json()

    resultado = dados["results"][0]

    print("\n=== RESULTADO ===")
    print("Título:", resultado["title"])
    print("Sinopse:", resultado["overview"])
    print("Data de lançamento:", resultado["release_date"])

except IndexError:
    print("Filme não encontrado.")

except requests.exceptions.RequestException:
    print("Erro ao acessar a API.")