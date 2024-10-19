# scraper.py
from playwright.sync_api import sync_playwright

def run_deck_scraper():
    url = "https://www.moxfield.com/embed/uklsacOJvE-3n6Uu2ntpUQ"
    
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)  # Abre Chromium para ver la acción
        page = browser.new_page()
        page.goto(url)
        
        # Espera a que las tablas carguen
        page.wait_for_selector('.table.table-sm.table-deck.table-condensed.mb-3')

        # Extrae todas las tablas
        tables = page.query_selector_all('.table.table-sm.table-deck.table-condensed.mb-3')
        
        deck_info = []
        
        for table in tables:
            # Obtén el encabezado de la tabla, que contiene el tipo de carta (Commander, Enchantment, etc.)
            header = table.query_selector('th').inner_text()
            
            # Extrae todas las filas (cartas)
            rows = table.query_selector_all('tbody tr')
            cards = []
            for row in rows:
                # Número de cartas y nombre de la carta
                quantity = row.query_selector('td.text-end').inner_text()
                card_name = row.query_selector('td a').inner_text()
                cards.append(f"{quantity} {card_name}")
            
            # Formatea la sección del deck
            deck_info.append(f"{header}:\n" + "\n".join(cards))
        
        # Formatea todo el deck
        print("\n\n".join(deck_info))
        
        browser.close()