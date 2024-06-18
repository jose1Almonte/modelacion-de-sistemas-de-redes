import time
import shower
import validators

from city import City



def has_visa() -> bool:
    while True:
        question = input('''¿El pasajero tiene visa?
1.- Si, tiene visa
2.- No, no tiene visa
> ''')
        if question == "1":
            return True
        elif question == "2":
            return False
        
        print("por favor, ingrese un dato válido...\n")
        time.sleep(2)
        print("Cargando pregunta...\n")
        time.sleep(3)

def select_origin(cities: list[City]):
    return select_a_city("la ciudad origen:", cities)

def select_destination(cities: list[City]):
    return select_a_city("la ciudad destino:", cities)

def select_a_city(message: str, cities: list[City]):
    while True:
        try:
            if validators.is_empty(cities):
                print("No hay ciudades en el sistema")
                return False

            print(f'Por favor, seleccione {message}')
            shower.cities(cities)
            question = int(input("> "))

            return cities[question-1]
            

        except:
            print("Debe escribir un numero entero")

def is_shortest_route():
    while True:
        question = input('''¿Que quieres hacer?:
1.- Ruta menos costosa
2.- Ruta con menos escalas
> ''')
        if question == "1":
            return True
        elif question == "2":
            return False
        
        print("Seleccione una de las dos opciones...\n")
        time.sleep(4)

def continue_program(question: str):
    while True:
        question = input(f'''\n{question}
1. Si
2.- No
> ''')
        if question == "1":
            return False
        elif question == "2":
            return True
