from models import Product
from connection import get_db_cursor

#responsiblel for product database operations
class ProductRepository :

    #give Product object, save it to PostgreSQL and returns a Product object
    def add(self, product : Product) -> Product :
        query = """
            INSERT INTO products (
                product_name,
                price,
                stock_quantity
            )
            VALUES (%s, %s, %s)
            RETURNING product_id;
        """

        with get_db_cursor() as cursor :
            cursor.execute(
                query,
                (product.product_name,
                 product.price,
                 product.stock_quantity)
            )

            product.product_id = cursor.fetchone()[0]

            return product

    def get_all(self) -> list[Product] :
        query = """
            SELECT 
                product_id,
                product_name,
                price,
                stock_quantity
            FROM products
        """

        with get_db_cursor() as cursor :
            cursor.execute(query)

            rows = cursor.fetchall()

            return [
                Product(
                    product_id=row[0],
                    product_name=row[1],
                    price=float(row[2]),
                    stock_quantity=row[3]
                )
                for row in rows 
            ]