class CargoTruck:
    def __init__(self, distance, speed, fuel_cost, cargo_weight):
        self.distance = distance
        self.speed = speed
        self.fuel_cost = fuel_cost
        self.cargo_weight = cargo_weight

    def calculate_cost(self):
        return (self.distance * self.fuel_cost) + (0.1 * self.cargo_weight)

    def calculate_time(self):
        return self.distance / self.speed