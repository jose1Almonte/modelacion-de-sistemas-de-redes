# La Agencia de Viajes Metro Travel desea adquirir un programa que le permita
# optimizar los costos de los viajes que realizan sus clientes. En este momento, Metro Travel
# se especializa en viajes desde el Aeropuerto de Maiquetía hacia las diversas islas
# del Mar Caribe.

# Algunos de los destinos requieren que los venezolanos tengan una visa. Para simplificar
# el ejercicio, cualquiera que posea una visa aceptable para una de las islas que la
# requieren puede ingresar en cualquier otra isla que requiera visa. No se permite empezar el viaje
# en un destino que requiere visa si el viajero no la posee.
# Los destinos a contemplar son:

# CCS	Caracas		                    No Requiere Visa
# AUA	Aruba		                    Requiere Visa
# BON	Bonaire		                    Requiere Visa
# CUR	Curazao		                    Requiere Visa
# SXM	San Martín		                Requiere Visa
# SDQ	Santo Domingo		            Requiere Visa
# SBH	San Bartolomé		            No Requiere Visa
# POS	Puerto España (Trinidad)		No Requiere Visa
# BGI	Barbados		                No Requiere Visa
# FDF	Fort de France (Martinica)		No Requiere Visa
# PTP	Point a Pitre (Guadalupe)		No Requiere Visa

# Las tarifas en los vuelos existentes se muestran en la tabla que sigue. El monto a pagar
# por volar en sentido contrario es el mismo. No interesan los horarios de salida ni llegada …
# tampoco importa la duración de una escala aburrida en un aeropuerto intermedio …
# solo se desea minimizar, a opción del usuario:

# . El costo del viaje entre 2 puntos
# . El número de escalas para un viaje entre 2 puntos

# Origen	Destino	    Precio del pasaje
# CCS	      AUA	        $ 40,00
# CCS	      CUR	        $ 35,00
# CCS	      BON	        $ 60,00
# CCS	      SXM	        $ 300,00
# AUA	      CUR	        $ 15,00
# AUA	      BON	        $ 15,00
# CUR	      BON	        $ 15,00
# CCS	      SDQ	        $ 180,00
# SDQ	      SXM	        $ 50,00
# SXM	      SBH	        $ 45,00
# CCS	      POS	        $ 150,00
# CCS	      BGI	        $ 180,00
# POS	      BGI	        $ 35,00
# POS	      SXM	        $ 90,00
# BGI	      SXM	        $ 70,00
# POS	      PTP	        $ 80,00
# POS	      FDF	        $ 75,00
# PTP	      SXM	        $ 100,00
# PTP	      SBH	        $ 80,00
# CUR	      SXM	        $ 80,00
# AUA	      SXM	        $ 85,00

# El usuario deberá introducir los códigos del aeropuerto origen y del aeropuerto destino,
# y responder si el pasajero tiene visa o no … el programa calculará la ruta más barata o bien
# la que tenga la menor cantidad de escalas y se la mostrará.

import time
from city import City
from travel import Travel
import search_alghoritms
import questions
import organizer

def main():
    cities = City.loader()
    travels = Travel.loader()
    run = True
    for i in range(10):
        print(f"Bienvenidos a mi sistema 🤨 METRO TRAVEL{"."*i}", end = "\r")
        time.sleep(0.5)
    print("\n")
    
    while run:
        has_visa = questions.has_visa()

        cities_to_apply = cities.copy() if has_visa else organizer.cities_without_visa(cities)
        travels_to_apply = travels.copy() if has_visa else organizer.travels_without_visa(organizer.cities_without_visa(cities),travels)
        origin = questions.select_origin(cities_to_apply)
        cities_to_apply.remove(origin)
        destination = questions.select_destination(cities_to_apply)
        cities_to_apply.append(origin)

        origin = origin.code
        destination = destination.code
        bucle = True
        while bucle:
            if questions.is_shortest_route():
                shortest_path_cost, shortest_path_route = search_alghoritms.dijkstra(cities_to_apply, travels_to_apply, origin, destination)
                print(f"La ruta más barata desde {origin} hasta {destination} cuesta {shortest_path_cost} y es {shortest_path_route}")
            else:
                hops, path = search_alghoritms.dijkstra_min_cities(cities_to_apply, travels_to_apply, origin, destination)
                print(f"El número mínimo de ciudades a pasar es: {hops} y la ruta es {path}")
            bucle = not questions.continue_program("¿Quiere ver mas información?")
        
        run = questions.continue_program("¿Terminar el programa?")
    
    print("Nos vemos 😜")



main()