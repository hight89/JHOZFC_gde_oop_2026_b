import json
from Model.flights import DomesticFlight, InternationalFlight
from Model.airline import Airline
from Model.booking import Booking

class DataManager:
    @staticmethod
    def load_data(filename: str):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        airlines = []
        for a_data in data['airlines']:
            airline = Airline(a_data['name'])
            
            for f_data in a_data['flights']:
                flight_class = DomesticFlight if f_data['type'] == "Domestic" else InternationalFlight
                flight = flight_class(
                    f_data['flight_number'], f_data['departure'], 
                    f_data['destination'], f_data['price'], f_data['capacity']
                )
                airline.add_flight(flight)
            
            for b_data in a_data.get('bookings', []):
                airline.create_booking(b_data['passenger'], b_data['flight_number'])
                
            airlines.append(airline)
        return airlines