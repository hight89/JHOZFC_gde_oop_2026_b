import random
import string

class Booking:
    def __init__(self, passenger_name: str, flight: 'Flight'):
        self.passenger_name = passenger_name
        self.flight = flight    
        self.booking_id = self._generate_id()

    def _generate_id(self):
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choices(chars, k=6))

    def __str__(self):
        return f"ID: {self.booking_id} | Foglalás: {self.passenger_name} | Járat: {self.flight.flight_number} ({self.flight.departure} -> {self.flight.destination})"