class Booking:
    def __init__(self, passenger_name: str, flight: 'Flight'):
        self.passenger_name = passenger_name
        self.flight = flight

    def __str__(self):
        return f"Foglalás: {self.passenger_name} | Járat: {self.flight.flight_number} ({self.flight.destination})"