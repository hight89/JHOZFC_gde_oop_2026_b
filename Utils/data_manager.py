import json
from datetime import datetime, timedelta
from Model.flights import DomesticFlight, InternationalFlight
from Model.airline import Airline
from Model.booking import Booking

class DataManager:
    @staticmethod
    def load_data(filename: str):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        airlines = []
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        
        for a_data in data['airlines']:
            airline = Airline(a_data['name'])
            
            # --- JÁRATOK GENERÁLÁSA ---
            temp_flights = []
            hours = [8, 12, 16, 20]
            days = [today, today + timedelta(days=1)]
            
            for f_data in a_data['flights']:
                for day in days:
                    for hour in hours:
                        dep_time = day.replace(hour=hour)
                        base_num = f_data['flight_number']
                        new_num = f"{base_num}-{dep_time.strftime('%m%d-%H%M')}"
                        
                        cls = DomesticFlight if f_data['type'] == "Domestic" else InternationalFlight
                        flight = cls(new_num, f_data['departure'], f_data['destination'], f_data['price'], f_data['capacity'], dep_time)
                        temp_flights.append(flight)
            
            # --- JÁRATOK RENDEZÉSE DÁTUM SZERINT ---
            temp_flights.sort(key=lambda x: x.departure_time)
            for f in temp_flights:
                airline.add_flight(f)
            
            # --- FOGLALÁSOK HOZZÁRENDELÉSE ---            
            for b_data in a_data.get('bookings', []):
                base_num = b_data['flight_number']
              
                for f in airline._flights:
                    if base_num in f.flight_number:
                        try:
                            airline.add_booking(b_data['passenger'], f.flight_number)
                        except Exception as e:
                            return
                    
                        break
                
            airlines.append(airline)
        return airlines