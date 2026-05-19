from Model.booking import Booking

class Airline:
    def __init__(self, name: str):
        self._name = name
        self._flights = []
        self._bookings = []

    def add_flight(self, flight: 'Flight'):
        self._flights.append(flight)

    def create_booking(self, passenger_name: str, flight_number: str):
        flight = next((f for f in self._flights if f.flight_number == flight_number), None)
        
        if flight:
            # Ellenőrizzük, van-e szabad hely
            if flight.free_seats > 0:
                new_booking = Booking(passenger_name, flight)
                self._bookings.append(new_booking)
                flight.add_booking(new_booking) # Itt adjuk hozzá a járat foglalásaihoz
                print(f"Sikeres foglalás: {passenger_name} -> {flight_number}")
                return flight.price
            else:
                raise ValueError("Nincs több szabad hely ezen a járaton!")
        else:
            raise ValueError("A megadott járat nem található!")

    def list_bookings(self):
        for b in self._bookings:
            print(b)