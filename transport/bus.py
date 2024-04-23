class Bus:
    def __init__(self, distance, speed, fuel_cost, passengers):
        self.distance = distance
        self.speed = speed
        self.fuel_cost = fuel_cost
        self.passengers = passengers

    def calculate_cost(self):
        return (self.distance * self.fuel_cost) + (0.05 * self.passengers)

    def calculate_time(self):
        return self.distance / self.speed
