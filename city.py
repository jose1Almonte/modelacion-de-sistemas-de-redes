class City():
    def __init__(self, code: str, name: str, visa_required: bool) -> None:
        self.code = code
        self.name = name
        self.visa_required = visa_required

    def __str__(self) -> str:
        return f"code: {self.code} | name: {self.name} | VISA: {'yes' if self.visa_required else 'no'}"

    def loader():
        data = open("data.txt", "r")
        cities = []
        for line in data:
            txt = line.split(",")
            new_city = City(txt[0], txt[1], False if txt[2] == "False" or txt[2] == "False\n" else True)
            cities.append(new_city)

        return cities
    

