from Utils.data_manager import DataManager

def main():    
    try:
        all_airlines = DataManager.load_data('Data/flights_data.json')

        for airline in all_airlines:
            print(f"\nLégitársaság: {airline._name}")
            
    except Exception as error:
        print(f"Hiba történt az adatok betöltése során: {error}")

if __name__ == "__main__":
    main()