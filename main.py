from Utils.data_manager import DataManager
from Controller.menu_controller import MenuController

def main():
    try:
        all_airlines = DataManager.load_data('Data/flights_data.json')
    except Exception as e:
        print(f"Hiba az adatok betöltésekor: {e}")
        return
    
    try:           
        menu = MenuController(all_airlines)    
        menu.run()
    except Exception as e:
        print(f"Végzetes hiba történt: {e}")

if __name__ == "__main__":
    main()