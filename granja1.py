import time 

class Granja:
    def __init__(self):
        self.cultivos = []
        self.animales = []

    def agregar_cultivo(self, cultivo):
        self.cultivos.append(cultivo)

    def eliminar_cultivo(self, nombre_cultivo):
        for cultivo in self.cultivos:
            if cultivo.nombre == nombre_cultivo:
                self.cultivos.remove(cultivo)
                return True
        return False

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def eliminar_animal(self, especie, raza):
        for animal in self.animales:
            if animal.especie == especie and animal.raza == raza:
                self.animales.remove(animal)
                return True
        return False

    def calcular_produccion_total_cultivos(self):
        produccion_total = 0
        for cultivo in self.cultivos:
            produccion_total += cultivo.area * cultivo.rendimiento
        return produccion_total

    def calcular_produccion_total_ganado(self):
        produccion_total = 0
        for animal in self.animales:
            produccion_total += animal.peso
        return produccion_total

    def generar_reporte_produccion_total(self):
        produccion_cultivos = self.calcular_produccion_total_cultivos()
        produccion_ganado = self.calcular_produccion_total_ganado()

        produccion_total = produccion_cultivos + produccion_ganado

        # Formatear los valores a dos decimales después del punto
        produccion_cultivos = "{:.2f}".format(produccion_cultivos)
        produccion_ganado = "{:.2f}".format(produccion_ganado)
        produccion_total = "{:.2f}".format(produccion_total)

        reporte = f"Reporte de producción total de la granja:\n"
        reporte += f"Producción total de cultivos: {produccion_cultivos} unidades\n"
        reporte += f"Producción total de ganado: {produccion_ganado} kg\n"
        reporte += f"Producción total de la granja: {produccion_total} \n"
        return reporte


class Cultivo:
    def __init__(self, nombre, tipo, area, rendimiento):
        self.nombre = nombre
        self.tipo = tipo
        self.area = area
        self.rendimiento = rendimiento

class Animal:
    def __init__(self, especie, raza, edad, peso):
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.peso = peso

# Función para mostrar el menú de cultivos y ganadería
def mostrar_menu():
    print("\nMenú:")
    print("1. cultivos")
    print("2. ganadería")
    print("3. reporte de producción total de la granja")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

# Función para mostrar el menú de gestión de cultivos
def mostrar_menu_cultivos():
    print("\nMenú - Gestión de cultivos:")
    print("1. Agregar cultivo")
    print("2. Eliminar cultivo")
    print("3. Calcular producción total de cultivos")
    print("4. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    return opcion

# Función para mostrar el menú de gestión de ganadería
def mostrar_menu_ganaderia():
    print("\nMenú - Gestión de ganadería:")
    print("1. Agregar animal")
    print("2. Eliminar animal")
    print("3. Calcular producción total de ganado")
    print("4. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    return opcion

# Función principal
def main():
    granja = Granja()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":  # Gestión de cultivos
            while True:
                opcion_cultivos = mostrar_menu_cultivos()

                if opcion_cultivos == "1":
                    nombre = input("Ingrese el nombre del cultivo: ")
                    tipo = input("Ingrese el tipo de cultivo: ")
                    area = float(input("Ingrese el área de cultivo en hectáreas: "))
                    rendimiento = float(input("Ingrese el rendimiento por hectárea: "))
                    cultivo = Cultivo(nombre, tipo, area, rendimiento)
                    granja.agregar_cultivo(cultivo)
                    print("Cultivo agregado con éxito.")
                    time.sleep(2)

                elif opcion_cultivos == "2":
                    nombre = input("Ingrese el nombre del cultivo que desea eliminar: ")
                    if granja.eliminar_cultivo(nombre):
                        print("Cultivo eliminado con éxito.")
                        time.sleep(2)
                    else:
                        print("No se encontró el cultivo con ese nombre.")
                        time.sleep(2)

                elif opcion_cultivos == "3":
                    produccion_total = granja.calcular_produccion_total_cultivos()
                    if produccion_total:
                        print("Producción total de cultivos:", produccion_total)
                        time.sleep(2)
                    else:
                        print("No hay cultivos agregados para calcular la producción.")
                        time.sleep(2)

                elif opcion_cultivos == "4":
                    break

                else:
                    print("Opción no válida. Por favor, seleccione una opción válida.")
                    time.sleep(2)

        elif opcion == "2":  # Gestión de ganadería
            while True:
                opcion_ganaderia = mostrar_menu_ganaderia()

                if opcion_ganaderia == "1":
                    especie = input("Ingrese la especie del animal: ")
                    raza = input("Ingrese la raza del animal: ")
                    edad = int(input("Ingrese la edad del animal en meses: "))
                    peso = float(input("Ingrese el peso del animal en kilogramos: "))
                    animal = Animal(especie, raza, edad, peso)
                    granja.agregar_animal(animal)
                    print("Animal agregado con éxito.")
                    time.sleep(2)

                elif opcion_ganaderia == "2":
                    especie = input("Ingrese la especie del animal que desea eliminar: ")
                    raza = input("Ingrese la raza del animal que desea eliminar: ")
                    if granja.eliminar_animal(especie, raza):
                        print("Animal eliminado con éxito.")
                        time.sleep(2)
                    else:
                        print("No se encontró el animal con esa especie y raza.")
                        time.sleep(2)

                elif opcion_ganaderia == "3":
                    produccion_total = granja.calcular_produccion_total_ganado()
                    if produccion_total:
                        print("Producción total del ganado:", produccion_total)
                        time.sleep(2)
                    else:
                        print("No hay animales agregados para calcular la producción.")
                        time.sleep(2)

                elif opcion_ganaderia == "4":
                    break

                else:
                    print("Opción no válida. Por favor, seleccione una opción válida.")
                    time.sleep(2)

        elif opcion == "3":
            reporte = granja.generar_reporte_produccion_total()
            print(reporte)
            time.sleep(2)

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            time.sleep(2)

if __name__ == "__main__":
    main()
