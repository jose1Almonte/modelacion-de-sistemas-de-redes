from city import City

def cities(cities: list[City]):
    index = 1
    for city in cities:
        print(f'{str(index)}.- {city.name}')
        index += 1