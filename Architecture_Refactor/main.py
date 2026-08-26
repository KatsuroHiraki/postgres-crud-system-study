from models import Product
from repositories import ProductRepository

def main() :
    repo = ProductRepository()

    new_product = Product(
        product_name="SteelSeries Headphones",
        price = 359.00,
        stock_quantity=13
    )

    saved_product = repo.add(new_product)

    print(f'Product saved to database..')
    print(f'with ID : {saved_product.product_id}')

    products = repo.get_all()

    print('Retrieved {len(products)} products.')

    for product in products :
        print(
            f" -- [{product.product_id}]"
            f"{product.product_name}"
            f"{product.price}"
            f"{product.stock_quantity}"
        )


main()



