from abc import ABC
from datetime import datetime

class Flight(ABC):
    def __init__(self, flight_number: str, departure: str, destination: str, price: int, capacity: int, departure_time: datetime):
        self.flight_number = flight_number
        self.departure = departure
        self.destination = destination
        self.price = price
        self.capacity = capacity
        self.departure_time = departure_time
        self._bookings = []
    
    @property
    def flight_number(self) -> str:
        return self._flight_number

    @flight_number.setter
    def flight_number(self, value: str):
        if not value:
            raise ValueError("A járatszám nem lehet üres!")
        self._flight_number = value

    @property
    def departure(self) -> str:
        return self._departure

    @departure.setter
    def departure(self, value: str):
        if not value:
            raise ValueError("Az indulási állomás nem lehet üres!")
        self._departure = value

    @property
    def destination(self) -> str:
        return self._destination

    @destination.setter
    def destination(self, value: str):
        if not value:
            raise ValueError("A célállomás nem lehet üres!")
        self._destination = value

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, value: int):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("A jegyár nem lehet negatív!")

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, value: int):
        if value > 0:
            self._capacity = value
        else:
            raise ValueError("A férőhelyek száma csak pozitív egész szám lehet!")

    def flight_info(self) -> str:
        time_str = self.departure_time.strftime("%Y-%m-%d %H:%M")
        return (f"{self.flight_number} | "
                f"{time_str} | {self.departure}->{self.destination} | "
                f"Szabad helyek: {self.free_seats} ({self.flight_type})"
                )
    
    def add_booking(self, booking: 'Booking'):
        self._bookings.append(booking)

    def remove_booking(self, passenger_name: str):
        # Eltávolítjuk a foglalást a név alapján
        self._bookings = [b for b in self._bookings if b.passenger_name != passenger_name]

    @property
    def free_seats(self) -> int:
        # Férőhely - eddigi foglalások száma
        return self.capacity - len(self._bookings)
 
    
    def __str__(self):
        return self.flight_info()

class DomesticFlight(Flight):
    flight_type = "Belföldi járat"

    @Flight.price.setter
    def price(self, value: int):
        if 12500 <= value <= 20000:
            self._price = value
        else:
            raise ValueError("A belföldi járat jegyára 12500 és 20000 Ft között kell, hogy legyen!")

class InternationalFlight(Flight):
    flight_type = "Nemzetközi járat"

    @Flight.price.setter
    def price(self, value: int):
        if 20000 <= value <= 60000:
            self._price = value
        else:
            raise ValueError("A nemzetközi járat jegyára 20000 és 60000 Ft között kell, hogy legyen!")