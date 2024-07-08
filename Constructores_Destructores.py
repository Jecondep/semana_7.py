# Definición de la clase Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        print(f"Se ha creado un nuevo vehículo {self.marca} {self.modelo}.")

    def __del__(self):
        print(f"El vehículo {self.marca} {self.modelo} ha sido eliminado.")

    def acelerar(self):
        print(f"El vehículo {self.marca} {self.modelo} está acelerando.")

# Definición de la clase Coche, que hereda de Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    def girar_derecha(self):
        print(f"El coche {self.marca} {self.modelo} está girando a la derecha.")

# Definición de la clase Moto, que hereda de Vehiculo
class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def girar_izquierda(self):
        print(f"La moto {self.marca} {self.modelo} está girando a la izquierda.")

# Creación de instancias de las clases
coche = Coche("Ford", "Focus", "Rojo")
moto = Moto("Honda", "CBR", 1000)

# Llamada a los métodos de las instancias
coche.acelerar()
moto.acelerar()

# Eliminación de las instancias al finalizar el programa
