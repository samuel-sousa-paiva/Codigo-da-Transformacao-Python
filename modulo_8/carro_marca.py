# Classe principal
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

    def __str__(self):
        return f"{self.marca} - {self.modelo}"


# Classe filha usando herança
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        super().exibir_info()
        print(f"Autonomia da bateria: {self.autonomia_bateria} km")

    def __str__(self):
        return f"{self.marca} - {self.modelo} | Bateria: {self.autonomia_bateria} km"


# Criando objetos
carro1 = Carro("Toyota", "Corolla")
carro2 = CarroEletrico("Tesla", "Model S", 600)

# Exibindo informações
print("=== CARRO NORMAL ===")
carro1.exibir_info()

print("\n=== CARRO ELÉTRICO ===")
carro2.exibir_info()

# Testando __str__
print("\n=== TESTE __str__ ===")
print(carro1)
print(carro2)