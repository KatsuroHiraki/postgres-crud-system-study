import psycopg
from contextlib import contextmanager

from config import DB_CONFIG

@contextmanager
def get_db_cursor() :
    conn = psycopg.connect(**DB_CONFIG)

    try : 
        with conn.cursor() as cursor : 
            yield cursor
            conn.commit()

    except Exception :
        conn.rollback()
        raise

    finally : conn.close()