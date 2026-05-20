import inquirer
from Utils.data_manager import DataManager

def main():
    try:
        all_airlines = DataManager.load_data('Data/flights_data.json')
    except Exception as e:
        print(f"Hiba az adatok betöltésekor: {e}")
        return

    while True:
        # Menüpontok definiálása
        questions = [
            inquirer.List('action',
                          message="Válasszon egy műveletet:",
                          choices=['Jegy foglalása', 'Foglalás lemondása', 'Foglalások listázása', 'Kilépés'],
            ),
        ]
        
        # Felhasználói választás beolvasása
        answers = inquirer.prompt(questions)
        choice = answers['action']

        if choice == 'Jegy foglalása':
            # Itt kérhetjük be az adatokat
            name = input("Utas neve: ")
            f_num = input("Járat száma: ")
            try:
                all_airlines[0].create_booking(name, f_num)
            except ValueError as e:
                print(f"Hiba: {e}")

        elif choice == 'Foglalás lemondása':
            name = input("Utas neve: ")
            f_num = input("Járat száma: ")
            try:
                all_airlines[0].cancel_booking(name, f_num)
            except ValueError as e:
                print(f"Hiba: {e}")

        elif choice == 'Foglalások listázása':
            print("\n--- Aktuális foglalások ---")
            for airline in all_airlines:
                airline.list_bookings()

        elif choice == 'Kilépés':
            print("Kilépés...")
            break

if __name__ == "__main__":
    main()