class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False


def __str__(self):
    status = "ligado" if self._ligado else "desligado"
    return f"{self.marca} {self.modelo} - Status: {status}"


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas


def __str__(self):
    status = "ligado" if self._ligado else "desligado"
    return f"{self.marca} {self.modelo} - Portas: {self.portas} - Status: {status}"


class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo


def __str__(self):
    status = "ligado" if self._ligado else "desligado"
    return f"{self.marca} {self.modelo} - Tipo: {self.tipo} - Status: {status}"


from carros import Carro
from motos import Moto

carro1 = Carro("Toyota", "Corolla", 4)
carro2 = Carro("Honda", "Civic", 2)
carro3 = Carro("Ford", "Fusion", 4)

moto1 = Moto("Harley-Davidson", "Street 750", "Esportiva")
moto2 = Moto("Honda", "CB 500", "Casual")
moto3 = Moto("Yamaha", "MT-09", "Esportiva")


print(carro1)
print(carro2)
print(carro3)

print(moto1)
print(moto2)
print(moto3)
