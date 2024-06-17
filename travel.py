class Travel():
    def  __init__(self, origin: str, destination: str, price: float, was_traveled: bool) -> None:
        self.origin = origin
        self.destination = destination
        self.price = price
        self.was_traveled = was_traveled
    
    def loader():
        data = [
            ["CCS","AUA",40.00,False],
            ["CCS","CUR",35.00,False],
            ["CCS","BON",60.00,False],
            ["CCS","SXM",300.00,False],
            ["AUA","CUR",15.00,False],
            ["AUA","BON",15.00,False],
            ["CUR","BON",15.00,False],
            ["CCS","SDQ",180.00,False],
            ["SDQ","SXM",50.00,False],
            ["SXM","SBH",45.00,False],
            ["CCS","POS",150.00,False],
            ["CCS","BGI",180.00,False],
            ["POS","BGI",35.00,False],
            ["POS","SXM",90.00,False],
            ["BGI","SXM",70.00,False],
            ["POS","PTP",80.00,False],
            ["POS","FDF",75.00,False],
            ["PTP","SXM",100.00,False],
            ["PTP","SBH",80.00,False],
            ["CUR","SXM",80.00,False],
            ["AUA","SXM",85.00,False],
        ]
        travels = []
        for element in data:
            new_travel = Travel(element[0],element[1],element[2],element[3])
            travels.append(new_travel)
        return travels