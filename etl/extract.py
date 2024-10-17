# etl/extract.py
import json
import requests

def extract_data():
    base_url = "https://edhtop16.com/api/graphql"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    body = {
        "query": "query tournaments_TournamentsQuery(\n  $timePeriod: TimePeriod!\n  $sortBy: TournamentSortBy!\n  $minSize: Int!\n) {\n  tournaments(filters: {timePeriod: $timePeriod, minSize: $minSize}, sortBy: $sortBy) {\n    id\n    ...tournaments_TournamentCard\n  }\n}\n\nfragment tournaments_TournamentCard on Tournament {\n  TID\n  name\n  size\n  tournamentDate\n  entries {\n  standing\n  wins\n  losses\n  draws\n  decklist\n  player {\n      name\n      id\n    }\n    commander {\n   name\n   id\n    }\n    id\n  }\n}\n",
        "variables": {
            "timePeriod": "ONE_MONTH",
            "sortBy": "DATE",
            "minSize": 60
        }
    }

    # Realiza la solicitud POST
    response = requests.post(base_url, json=body, headers=headers)
    
    # Verificamos el código de estado
    if response.status_code == 200:
        try:
            data = response.json()
            print("OK: La solicitud fue exitosa.")
            
            # Guardar los datos en un archivo JSON temporal
            with open('temp_data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
                print("Datos guardados en 'temp_data.json'.")
        except json.JSONDecodeError:
            print("La respuesta no es un JSON válido.")
            print("Respuesta:", response.text)
    else:
        print(f"Error: {response.status_code} - {response.text}")  # Muestra un mensaje de error si la solicitud falla