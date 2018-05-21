from prac_08.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, reliability=50):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        if random.randint(1, 101) < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            print('Car Failed to start')
