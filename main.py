from Model.flights import DomesticFlight, InternationalFlight

def main():
    print("--- Repülőjáratok Inicializálása (1. Nap Teszt) ---\n")

    try:
        flight1 = DomesticFlight("W6101", "Budapest", "Debrecen", 12500, 120)
        flight2 = InternationalFlight("W6230", "Budapest", "London-Luton", 38900, 230)
        flight3 = InternationalFlight("FR4501", "Budapest", "Róma-Fiumicino", 29500, 189)

        flights = [flight1, flight2, flight3]

        for flight in flights:
            print(flight.flight_info())
            
    except ValueError as error:
        print(f"Hiba történt az adatok betöltése során: {error}")

if __name__ == "__main__":
    main()