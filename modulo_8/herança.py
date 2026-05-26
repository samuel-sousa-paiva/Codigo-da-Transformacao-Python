# Classe principal
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")


# Classe com herança
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        super().exibir_info()
        print(f"Autonomia da bateria: {self.autonomia_bateria} km")


# Criando objeto
tesla = CarroEletrico("Tesla", "Model 3", 500)

# Exibindo informações
tesla.exibir_info()