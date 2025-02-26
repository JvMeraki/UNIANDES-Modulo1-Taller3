from concentrado import Concentrado
from perro import Perro


class Guarderia:
    def __init__(self):
        self._nombre = "Guarderia de Perros"
        self.concentrados = ["Taste of the wild", "Royal Canin", "Pro Plan", "Hills", "Eukanuba", "Pedigree", "Pro Pac", "Nutram", "Purina", "Orijen"]
        self.inventario_concentrados = []
        
    def agregar_concentrado(self,concentrado: Concentrado):
        self.inventario_concentrados.append(concentrado)
    
concentrados = [
    Concentrado("Taste of the Wild", 100000, 500, "INVIMA-123"),
    Concentrado("Royal Canin", 80000, 400, "INVIMA-124"),
    Concentrado("Pro Plan", 120000, 600, "INVIMA-125"),
    Concentrado("Hills", 90000, 450, "INVIMA-126"),
    Concentrado("Eukanuba", 95000, 475, "INVIMA-127"),
    Concentrado("Pedigree", 70000, 350, "INVIMA-128"),
    Concentrado("Pro Pac", 75000, 375, "INVIMA-129"),
    Concentrado("Nutram", 85000, 425, "INVIMA-130"),
    Concentrado("Purina", 110000, 550, "INVIMA-131"),
    Concentrado("Orijen", 130000, 650, "INVIMA-132"),
]

guarderia = Guarderia()
for concentrado in concentrados:
    guarderia.agregar_concentrado(concentrado)

perro_1 = Perro("Zeus", "Rottweiler", 45.8, 3, "Pro Plan")
perro_2 = Perro("Nala", "Golden Retriever", 8.4, 1, "Royal Canin")
perro_3 = Perro("Atila", "Alabai", 58.9, 5, "Taste of the wild")


# Para probar vamos a inicializar una variable para que sea dínamica
perro_prueba = perro_2 # Remplazamos perro_1 por el perro a consultar


# Probar código, imprimir información del perro X
print(perro_prueba.dar_informacion())
# Buscaremos los datos del concentrado favorito, del perro en cuestión
concentrado_favorito = next(
    (concentrado for concentrado in guarderia.inventario_concentrados if concentrado.nombre == perro_prueba.dar_concentrado_preferido()),
    None
)
# Ahora la información será impresa
if concentrado_favorito:
    print(f"El concentrado preferido de '{perro_prueba.dar_nombre()}' es: {concentrado_favorito.dar_informacion()}")
    print(f"Rentabilidad: {concentrado_favorito.calcular_rentabilidad()}")
else:
    print(f"El concentrado {perro_prueba.concentrado_preferido} no se encuentra en el inventario de la guardería")