# Classe principal
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo}"


# Classe filha
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def __str__(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo} | Autonomia: {self.autonomia_bateria} km"


# Criando objetos
carro1 = Carro("Honda", "Civic")
carro2 = CarroEletrico("Tesla", "Model X", 550)

# Exibindo objetos
print(carro1)
print(carro2)