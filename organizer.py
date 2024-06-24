from city import City
from travel import Travel

def cities_without_visa(cities: list[City]):
    return [city for city in cities if not city.visa_required]

def travels_without_visa(cities_without_visa: list[City], travels: list[Travel]):
    visa_free_codes = {city.code for city in cities_without_visa}
    return [travel for travel in travels if travel.origin in visa_free_codes and travel.destination in visa_free_codes]
