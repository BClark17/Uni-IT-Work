from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, fanciness, flagfall=4.5, price_per_km=1.23):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel, price_per_km)
        self.flagfall = flagfall
        self.price_per_km = price_per_km * fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance + self.flagfall

    def __str__(self):
        fare = self.get_fare()
        price = self.price_per_km
        """Return a string like a Car but with current fare distance."""
        return "{}, fuel={}, odo={}km, {}km on current fare, ${}/km plus flagfall of ${}"\
            .format(self.name, self.fuel, self.current_fare_distance,
                    fare, price, self.flagfall)