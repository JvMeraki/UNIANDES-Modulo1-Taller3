class Perro:
    def __init__(self, nombre: str, raza: str, peso: float, edad: int, concentrado_preferido: str = None):
        self.__nombre = nombre
        self.__raza = raza
        self.__peso = peso
        self.__edad = edad
        self.__concentrado_preferido = concentrado_preferido
        
    def ladrar(self) -> str:
        return "guau guau"
    
    def modificar_peso(self, nuevo_peso) -> float:
        self.__peso = nuevo_peso
        
    def dar_nombre(self) -> str:
        return self.__nombre
    
    def dar_concentrado_preferido(self) -> str:
        return self.__concentrado_preferido

    def dar_informacion(self) -> str:
        return f"Nombre: {self.__nombre}, Raza: {self.__raza}, Peso: {self.__peso} kg, Edad: {self.__edad} años, Concentrado preferido: {self.__concentrado_preferido or 'Ninguno'}"
        
        # Diferentes formas de imprimir la información
        # return "Nombre: {}, Raza: {}, Peso: {}, Edad: {}, Concentrado preferido: {}".format(self.__nombre, self.__raza, self.__peso, self.__edad, self.__concentrado_preferido)
        # return self.__nombre + ": ("+ self.__raza + ") - " + str(self.__peso) + "kg - " + str(self.__edad) + " años"
        # return self.__nombre + "(" + self.__raza + "):" + str(self.__peso) + "|" + str(self.__edad)