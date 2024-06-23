from city import City
from travel import Travel

def __separator_variable():
    return " #$%&/()=??=)=)(/&%$#) "

def __name_travels():
    return "travels"

def __name_cities():
    return "cities"

def write_travels(travels: list[Travel]):
    name_txt = __name_travels()
    data = ""
    for travel in travels:
        row = travel.origin + __separator_variable() + travel.destination + __separator_variable() + str(travel.price) + __separator_variable() + str(travel.was_traveled) + "\n"
        data = data + row
    
    __write_txt(data, name_txt)

def write_cities(cities: list[City]):
    name_txt = __name_cities()
    data = ""
    for city in cities:
        row = city.code + __separator_variable() + city.name + __separator_variable() + str(city.visa_required) + "\n"
        data = data + row
    
    __write_txt(data,name_txt)

def __write_txt(data: str, name_txt: str):
    file = open(f'txt\{name_txt}.txt', 'w')
    file.write(data)
    file.close()

def __read_txt(name_txt: str):
    file = open(f'txt\{name_txt}.txt', 'r')
    readed = file.read()
    file.close()
    return readed

def read_travels():
    rows = __read_txt(__name_travels()).split("\n")
    travels = []
    travels: list[Travel]
    while "" in rows:
        rows.remove("") 
    for travel_string in rows:
        travel_in_list = travel_string.split(__separator_variable())
        travel = Travel(travel_in_list[0],travel_in_list[1],float(travel_in_list[2]),bool(travel_in_list[3]))
        travels.append(travel)
    return travels

def read_cities():
    rows = __read_txt(__name_cities()).split("\n")
    cities = []
    cities: list[City]
    rows.remove("")
    for city_string in rows:
        city_in_list = city_string.split(__separator_variable())
        city = City(city_in_list[0],city_in_list[1],city_in_list[2])
        cities.append(city)
    return cities

