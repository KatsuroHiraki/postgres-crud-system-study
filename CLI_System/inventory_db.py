import psycopg
from config import DB_CONFIG

def get_connection() :
    return psycopg.connect(**DB_CONFIG)

def create_product(name : str, price : float, stock : int) :
    with get_connection() as conn :
        with conn.cursor() as cursor :

            cursor.execute("""
                INSERT INTO products (product_name, price, stock_quantity) VALUES
                (%s, %s, %s)
                RETURNING product_id;
                """, 
                (name, price, stock)
            )

            product_id = cursor.fetchone()[0]

            print(f'Product ID : {product_id}')

            return product_id

def get_all_products() :
    with get_connection() as conn :
        with conn.cursor() as cursor :

            cursor.execute("""
                SELECT product_id, product_name, price, stock_quantity
                FROM products
                ORDER BY product_id
            """)

            return cursor.fetchall()


def get_product_by_id(product_id : int) -> tuple | None :
    with get_connection() as conn : 
        with conn.cursor() as cursor :

            cursor.execute("""
                SELECT product_id, product_name, price, stock_quantity
                FROM products 
                WHERE product_id = %s;
            """, (product_id,))

            return cursor.fetchone()

def update_product_stock(product_id: int, new_stock: int):
    with get_connection() as conn:
        with conn.cursor() as cursor:

            cursor.execute("""
                UPDATE products
                SET stock_quantity = %s
                WHERE product_id = %s;
            """, (new_stock, product_id))

            return cursor.rowcount > 0


def delete_product(product_id : int) -> bool :
    with get_connection() as conn :
        with conn.cursor() as cursor :

            cursor.execute("""
                DELETE FROM products
                where product_id = %s;
            """, (product_id,)
            )

            return cursor.rowcount > 0
