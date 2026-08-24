import psycopg 
from config import DB_CONFIG

def get_connection() :
    return psycopg.connect(**DB_CONFIG)

def fetch_all_customers() :
    with get_connection() as conn :
        with conn.cursor() as cursor : 

            cursor.execute("""
                SELECT customer_id, full_name, email
                FROM customers
                ORDER BY customer_id;    
            """)

            return cursor.fetchall()


def add_new_customer(full_name : str, email : str) :
    with get_connection() as conn :
        with conn.cursor() as cursor :

            cursor.execute("""
                INSERT INTO customers (full_name, email) VALUES 
                (%s, %s)
                RETURNING customer_id;  
            """, (full_name, email)
            ) #returning means postgresql will give the id of the new customer

            new_id = cursor.fetchone()[0]
            #the first element in the customer tuple is the customer_id

            return new_id

def get_customer_orders(customer_id : int) :
    with get_connection() as conn :
            with conn.cursor() as cursor :

                cursor.execute("""
                    SELECT 
                        o.order_id,
                        o.order_date,
                        o.total_amount
                    FROM orders AS o
                    INNER JOIN customers AS c
                        ON o.customer_id = c.customer_id
                    WHERE c.customer_id = %s
                    ORDER BY o.order_date;
                """, (customer_id,)
                )

                return cursor.fetchall()
