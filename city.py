class City():
    def __init__(self, code: str, name: str, visa_required: bool) -> None:
        self.code = code
        self.name = name
        self.visa_required = visa_required

    def loader():
        data = [
            [
                "CCS","Caracas",False
            ], 
            [
                "AUA","Aruba",True
            ],
            [
                "BON","Bonaire",True
            ],
            [
                "CUR","Curazao",True
            ],
            [
                "SXM","San Martín",True
            ],
            [
                "SDQ","Santo Domingo",True
            ],
            [
                "SBH","San Bartolomé",False
            ],
            [
                "POS","Puerto España (Trinidad)",False
            ],
            [
                "BGI","Barbados",False
            ],
            [
                "FDF","Fort de France (Martinica)",False
            ],
            [
                "PTP","Point a Pitre (Guadalupe)",False
            ],
        ]
        cities = []
        for element in data:
            new_city = City(element[0], element[1], element[2])
            cities.append(new_city)
        return cities
