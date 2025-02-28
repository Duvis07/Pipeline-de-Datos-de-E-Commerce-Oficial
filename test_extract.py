from src import config
from src.extract import extract

def main():
    print("Iniciando prueba de extracción de datos...")
    
    # 1. Obtener las rutas y configuraciones
    csv_folder = config.DATASET_ROOT_PATH
    public_holidays_url = config.PUBLIC_HOLIDAYS_URL
    csv_table_mapping = config.get_csv_to_table_mapping()
    
    print(f"\nCarpeta de datos: {csv_folder}")
    print(f"URL de días festivos: {public_holidays_url}")
    print(f"Mapeo de archivos: {csv_table_mapping}")
    
    # 2. Extraer los datos
    print("\nExtrayendo datos...")
    csv_dataframes = extract(csv_folder, csv_table_mapping, public_holidays_url)
    
    # 3. Verificar resultados
    print("\nResultados:")
    for name, df in csv_dataframes.items():
        print(f"  - {name}: {len(df)} filas")

if __name__ == "__main__":
    main()
