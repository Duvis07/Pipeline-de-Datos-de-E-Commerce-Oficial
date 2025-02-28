from typing import Dict
import requests
from pandas import DataFrame, read_csv, read_json, to_datetime

def temp() -> DataFrame:
    """Get the temperature data.
    Returns:
        DataFrame: A dataframe with the temperature data.
    """
    return read_csv("data/temperature.csv")

# TODO: SE IMPLEMENTO LA FUNCION get_public_holidays, PERO FALLA CUANDO CORRO EL PROJECT.IPYNB
# VERIFICAR QUE EL CODIGO FUNCIONE CORRECTAMENTE HAY LES DEJO LA GUIA DE LA FUNCION get_public_holidays
# NO SE PORQUE FALLA HICE EL TEST EXTRACT Y FUNCIONA CORRECTAMENTE REVISEN BIEN EL CODIGO.


def get_public_holidays(public_holidays_url: str, year: str) -> DataFrame:
    """Get the public holidays for the given year for Brazil.
    Args:
        public_holidays_url (str): url to the public holidays.
        year (str): The year to get the public holidays for.
    Raises:
        SystemExit: If the request fails.
    Returns:
        DataFrame: A dataframe with the public holidays.
    """
    print(f"Obteniendo días festivos para Brasil del año {year}")
    url = f"{public_holidays_url}/{year}/BR"
    print(f"URL: {url}")
    
    try:
        print("Haciendo petición HTTP...")
        response = requests.get(url)
        response.raise_for_status()
        print("Petición exitosa!")
        
        print("Procesando datos...")
        holidays_df = DataFrame(response.json())
        print(f"Columnas originales: {holidays_df.columns.tolist()}")
        
        # Eliminar columnas innecesarias si existen
        if 'types' in holidays_df.columns:
            holidays_df = holidays_df.drop('types', axis=1)
        if 'counties' in holidays_df.columns:
            holidays_df = holidays_df.drop('counties', axis=1)
        print(f"Columnas después de limpieza: {holidays_df.columns.tolist()}")
        
        # Convertir la columna date a datetime
        holidays_df['date'] = to_datetime(holidays_df['date'])
        print("Fechas convertidas a datetime")
        
        print(f"Total de días festivos encontrados: {len(holidays_df)}")
        return holidays_df
        
    except requests.RequestException as e:
        print(f"Error al obtener los días festivos: {str(e)}")
        raise SystemExit(f"Error al obtener los días festivos: {str(e)}")

def extract(
    csv_folder: str, csv_table_mapping: Dict[str, str], public_holidays_url: str
) -> Dict[str, DataFrame]:
    """Extract the data from the csv files and load them into the dataframes.
    Args:
        csv_folder (str): The path to the csv's folder.
        csv_table_mapping (Dict[str, str]): The mapping of the csv file names to the
        table names.
        public_holidays_url (str): The url to the public holidays.
    Returns:
        Dict[str, DataFrame]: A dictionary with keys as the table names and values as
        the dataframes.
    """
    dataframes = {
        table_name: read_csv(f"{csv_folder}/{csv_file}")
        for csv_file, table_name in csv_table_mapping.items()
    }

    holidays = get_public_holidays(public_holidays_url, "2017")

    dataframes["public_holidays"] = holidays

    return dataframes
