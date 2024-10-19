#! C:\Users\XPC\Documents\GitHub\PavsCR\MTG_CEDH_Data\venv\Scripts\python.exe 

from etl.extract import extract_data
from etl.transform import transform_data
from etl.deck.extract import run_deck_scraper

def main():
    #extract_data()
    #transform_data()
    run_deck_scraper()

if __name__ == "__main__":
    main()
