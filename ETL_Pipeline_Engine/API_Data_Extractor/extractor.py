import os
import requests
import json
from datetime import datetime

class APIExtractor : 
    def __init__(self, base_url : str) :
        self.base_url = base_url

    def fetch_products(self, limit : int = 30, skip : int = 0) -> dict :
        url = f"{self.base_url}/products?limit={limit}&skip={skip}"
        try : 
            response = requests.get(url, timeout=10)
            response.raise_for_status() #raise http error if present
            return response.json()
        except requests.exceptions.RequestException as e :
            print(f"Error fetching data from API : {e}")
            return {} 

    def save_raw_staging(self, data: dict, output_dir : str = "raw_data") -> str :
        os.makedirs(output_dir, exist_ok = True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = os.path.join(output_dir, f"raw_products_{timestamp}.json")

        with open(filepath, "w", encoding="utf-8") as f : 
            json.dump(data, f, indent = 4)

        return filepath
