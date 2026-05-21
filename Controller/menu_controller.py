import inquirer
from Model.airline import Airline

class MenuController:
    def __init__(self, airlines: list):
        self.airlines = airlines

    def run(self):
        while True:
            questions = [
                inquirer.List('action',
                              message="Válasszon egy műveletet:",
                              choices=['Jegy foglalása', 'Foglalás lemondása', 'Foglalások listázása', 'Kilépés'],
                ),
            ]
            choice = inquirer.prompt(questions)['action']

            if choice == 'Jegy foglalása':
                self._handle_booking()
            elif choice == 'Foglalás lemondása':
                self._handle_cancellation()
            elif choice == 'Foglalások listázása':
                self._handle_listing()
            elif choice == 'Kilépés':
                print("Kilépés...")
                break

    def _handle_booking(self):
        print(self.airlines)
        all_flights = [f for a in self.airlines for f in a._flights]
        if not all_flights:
            print("Nincs elérhető járat.")
            return

        choices = all_flights + ["Vissza"]
        selection = inquirer.prompt([inquirer.List('flight', message="Válasszon járatot:", choices=choices)])['flight']
        
        if selection == "Vissza": return

        name = input("Utas neve: ")
        try:
            for airline in self.airlines:
                if selection in airline._flights:
                    airline.create_booking(name, selection.flight_number)
                    break
        except ValueError as e:
            print(f"Hiba: {e}")

    def _handle_cancellation(self):
        all_bookings = [b for a in self.airlines for b in a._bookings]
        if not all_bookings:
            print("Nincs lemondható foglalás.")
            return

        choices = all_bookings + ["Vissza"]
        selection = inquirer.prompt([inquirer.List('booking', message="Válassza ki a törlendőt:", choices=choices)])['booking']
        
        if selection == "Vissza": return

        try:
            found = False
            for airline in self.airlines:
                if selection in airline._bookings:
                    airline.cancel_booking(selection.booking_id)
                    found = True
                    break
            
            if not found:
                print("Hiba: A foglalás nem található egyik légitársaságnál sem.")
        except ValueError as e:
            print(f"Hiba: {e}")

    def _handle_listing(self):
        print("\n--- Aktuális foglalások ---")
        for airline in self.airlines:
            airline.list_bookings()
        
        action = inquirer.prompt([inquirer.List('next', message="Művelet:", choices=['Vissza', 'Foglalás lemondása'])])['next']
        if action == 'Foglalás lemondása':
            self._handle_cancellation()