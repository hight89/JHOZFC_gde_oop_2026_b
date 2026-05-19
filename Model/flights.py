from abc import ABC

class Flight(ABC):
    def __init__(self, flight_number: str, departure: str, destination: str, price: int, capacity: int):
        self.flight_number = flight_number
        self.departure = departure
        self.destination = destination
        self.price = price
        self.capacity = capacity

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
        return f"{self.flight_type} | Szám: {self.flight_number} | Indulás: {self.departure} | Cél: {self.destination} | Ár: {self.price} Ft | Férőhely: {self.capacity}"


class DomesticFlight(Flight):
    flight_type = "Belföldi járat"

    def __init__(self, flight_number: str, departure: str, destination: str, price: int, capacity: int):
        super().__init__(flight_number, departure, destination, price, capacity)

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, value: int):
        if 12500 <= value <= 20000:
            self._price = value
        else:
            raise ValueError("A belföldi járat jegyára 12500 és 20000 Ft között kell, hogy legyen!")


class InternationalFlight(Flight):
    flight_type = "Nemzetközi járat"

    def __init__(self, flight_number: str, departure: str, destination: str, price: int, capacity: int):
        super().__init__(flight_number, departure, destination, price, capacity)

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, value: int):
        if 20000 <= value <= 60000:
            self._price = value
        else:
            raise ValueError("A nemzetközi járat jegyára 20000 és 60000 Ft között kell, hogy legyen!")