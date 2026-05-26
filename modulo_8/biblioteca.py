# Classe Livro
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        return f"{self.titulo} - {self.autor}"


# Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado!")

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and livro.disponivel:
                livro.disponivel = False
                print(f"Livro '{titulo}' emprestado!")
                return

        print("Livro não disponível.")

    def listar_livros(self):
        print("\n=== LIVROS DA BIBLIOTECA ===")

        for livro in self.livros:
            status = "Disponível" if livro.disponivel else "Emprestado"
            print(f"{livro} | Status: {status}")


# Criando biblioteca
biblioteca = Biblioteca()

# Criando livros
livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("Harry Potter", "J.K Rowling")

# Adicionando livros
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

# Listando livros
biblioteca.listar_livros()

# Emprestando livro
biblioteca.emprestar_livro("Harry Potter")

# Listando novamente
biblioteca.listar_livros()