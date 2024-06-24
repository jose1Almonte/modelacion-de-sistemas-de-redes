import shower
import validators
import animated
from city import City

def has_visa() -> bool:
    while True:
        question = input('''¿El pasajero tiene visa?
1.- Sí, tiene visa
2.- No, no tiene visa
> ''')
        if question == "1":
            return True
        elif question == "2":
            return False
        animated.animated_message("Por favor, ingrese un dato válido")        

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
        except (ValueError, IndexError):
            print("Debe escribir un número entero dentro del rango que se le indica\n")

def is_shortest_route():
    while True:
        question = input('''¿Qué quieres hacer?:
1.- Ruta menos costosa
2.- Ruta con menos escalas
> ''')
        if question == "1":
            return True
        elif question == "2":
            return False
        animated.animated_message("Seleccione una de las dos opciones")

def continue_program(question: str):
    while True:
        answer = input(f'''\n{question}
1. Sí
2.- No
> ''')
        if answer == "1":
            return False
        elif answer == "2":
            return True
