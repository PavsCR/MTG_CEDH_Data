import json

def transform_data():
    # Cargar datos desde el archivo temporal
    try:
        with open('temp_data.json', 'r') as f:
            data = json.load(f)
            print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("El archivo temp_data.json no fue encontrado.")
    except json.JSONDecodeError:
        print("Error al decodificar el JSON. Asegúrate de que el archivo contenga un JSON válido.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        
    # Transformar los datos
    # Agregar aqui la logica para transformar los datos con spark
