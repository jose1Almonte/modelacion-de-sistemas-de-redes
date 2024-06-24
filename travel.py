class Travel():
    def __init__(self, origin: str, destination: str, price: float, was_traveled: bool) -> None:
        self.origin = origin
        self.destination = destination
        self.price = price
        self.was_traveled = was_traveled

    @classmethod
    def loader(cls):
        data = open("paths.txt", "r")
        fix_data = [line.split(',') for line in data.readlines()]

        return [cls(element[0], element[1], float(element[2]), element[3]) for element in fix_data]
