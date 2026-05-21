from Model.booking import Booking
from datetime import datetime, timedelta

class Airline:
    def __init__(self, name: str):
        self._name = name
        self._flights = []
        self._bookings = []

    def add_flight(self, flight: 'Flight'):
        self._flights.append(flight)
    def add_booking(self, passenger_name: str, flight_number: str):

        flight = next((f for f in self._flights if f.flight_number == flight_number), None)
        
        if flight:
            new_booking = Booking(passenger_name, flight)
            self._bookings.append(new_booking)
            flight.add_booking(new_booking)
            return True
        return False

    def create_booking(self, passenger_name: str, flight_number: str):
        flight = next((f for f in self._flights if f.flight_number == flight_number), None)
        
        if flight:
            if flight.free_seats <= 0:
                raise ValueError(f"Sajnáljuk, a(z) {flight_number} járat már teltházas!")
            
            min_booking_time = datetime.now() + timedelta(hours=6)

            if flight.departure_time < min_booking_time:
                raise ValueError(f"Sajnáljuk, a(z) {flight_number} járatra a foglalás már nem lehetséges (kevesebb mint 6 óra van az indulásig).")
        
        
            self.add_booking(passenger_name,flight_number)
            print(f"Sikeres foglalás: {passenger_name} -> {flight_number}")
            return flight.price
        else:
            raise ValueError("A megadott járat nem található!")
        
    def cancel_booking(self, booking_id: str):
        booking_to_cancel = next((b for b in self._bookings if b.booking_id == booking_id), None)
        
        if booking_to_cancel:
            self._bookings.remove(booking_to_cancel)
            booking_to_cancel.flight.remove_booking(booking_to_cancel.passenger_name)
            print(f"Sikeres lemondás: {booking_id} azonosítójú foglalás törölve.")
        else:
            raise ValueError(F"A megadott azonosítóval ({booking_id}) nem található foglalás!")

    def list_bookings(self):
        for b in self._bookings:
            print(b)

    def __str__(self):
        flight_list = ", ".join([f.flight_number for f in self._flights])
        return f"Légitársaság: {self._name} | Járatok: {flight_list if flight_list else 'Nincs járat'}"
