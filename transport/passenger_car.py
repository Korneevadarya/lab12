class PassengerCar:
    def __init__(self, distance, speed, fuel_cost):
        self.distance = distance
        self.speed = speed
        self.fuel_cost = fuel_cost

    def calculate_cost(self):
        return self.distance * self.fuel_cost

    def calculate_time(self):
        return self.distance / self.speed