class Atleta:
    aposentado = False
    peso = None
    def aposentar(self):
        self.aposentado = True
    def aquecer(self):
        print("aquecendo")

class Corredor(Atleta):
    def correr(self):
        print("correndo")
class Nadador(Atleta):
    def nadar(self):
        print("nadando")
class Ciclista(Atleta):
    def pedalar(self):
        print("pedalando")

class Triatleta(Corredor, Nadador, Ciclista):
    def __init__(self):
        self.nadar()
        self.pedalar()
        self.correr()


