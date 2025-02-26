class Concentrado:
    def __init__(self, nombre: str, precio: float, num_calorias: float, reg_invima: str):
        self.__nombre = nombre
        self.__precio = precio
        self.__num_calorias = num_calorias
        self.__reg_invima = reg_invima

    def dar_informacion(self) -> str:
        return f"{self.__nombre} ($ {self.__precio})"
    
    def calcular_rentabilidad(self) -> float:
        return round(self.precio / self.num_calorias, 2)
    
    # Getters y setters con property
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
    @property  
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, precio):
        self.__precio = precio
        
    @property
    def num_calorias(self):
        return self.__num_calorias
    @num_calorias.setter
    def num_calorias(self, num_calorias):
        self.__num_calorias = num_calorias