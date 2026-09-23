# Automated ETL Pipeline Engine

## Data Extraction — Consuming REST APIs
- Learned: HTTP request lifecycle (`requests`), status handling, JSON payload parsing, error handling, and staging raw data in local data lake zones.
- Built:
  - `extractor.py`: Moduled API extractor handling request execution and timestamped raw JSON staging.
  - `main.py`: Ingestion driver script executing data extraction from REST endpoints.