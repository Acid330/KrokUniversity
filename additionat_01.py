class Car:

    def __init__(self, speed=5, time=20):
        self.distance = None
        self.speed = speed
        self.time = time

    def way(self):
        self.distance = self.speed * self.time
        return self.distance

    def fastway(self):
        self.time = self.time / 2
        return int(self.distance / self.time)


car = Car()
print(car.way(), "Distance meters", "\n", car.fastway(), "Speed for distance if time less than 2 times")
