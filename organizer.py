from city import City
from travel import Travel


def cities_without_visa(cities: list[City]):
    cities_to_return = []

    for city in cities:
        if not city.visa_required:
            cities_to_return.append(city)
    
    return cities_to_return

def travels_without_visa(cities_without_visa: list[City], travels: list[Travel]):
    travels_to_return = []
    travels_to_return: list[Travel]

    for travel in travels:
        origin_needs_visa = True
        destination_needs_visa = True
        for city in cities_without_visa:
            if travel.origin == city.code:
                origin_needs_visa = False
            if travel.destination == city.code:
                destination_needs_visa = False
        
        if not origin_needs_visa and not destination_needs_visa:
            travels_to_return.append(travel)
    
    return travels_to_return