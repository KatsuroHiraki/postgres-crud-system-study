from extractor import APIExtractor

def main() : 
    BASE_URL = "https://dummyjson.com"
    extractor = APIExtractor(base_url=BASE_URL)

    print("Starting data extraction sprint..")
    raw_payload = extractor.fetch_products(limit=50, skip = 0)

    if "products" in raw_payload :
        product_count = len(raw_payload["products"])
        filepath = extractor.save_raw_staging(raw_payload)
        print(f"Extracted {product_count} raw records.")
        print(f"Staged raw file to : {filepath}")
    else :
        print("Extraction completed with empty payload")

main()