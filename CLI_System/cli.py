from inventory_db import (
    create_product,
    get_all_products,
    get_product_by_id,
    update_product_stock,
    delete_product
)

def print_menu():
    print("\n" + "=" * 35)
    print("📦 INVENTORY MANAGER")
    print("=" * 35)
    print("1. View All Products")
    print("2. Search Product by ID")
    print("3. Add New Product")
    print("4. Update Product Stock")
    print("5. Delete Product")
    print("6. Exit")
    print("=" * 35)

while True :
    print_menu()

    try : 
        choice = int(input('Select : '))
    except ValueError :
        print('Enter a valid choice (int)')

    if choice == 6 :
        break

    elif choice == 1 :

        products = get_all_products()

        for p in products :
            print(f'ID : {p[0]}')
            print(f'Name : {p[1]}')
            print(f'Price : {p[2]}')
            print(f'Stock Left : {p[3]}')

    elif choice == 2 :

        try :
            product_id = int(input('Enter Product ID : '))
        except ValueError :
            print('Enter a valid ID')   

        product = get_product_by_id(product_id)

        if product:
            print(f"ID : {product[0]}")
            print(f"Name : {product[1]}")
            print(f"Price : {product[2]}")
            print(f"Stock : {product[3]}")
        else:
            print("Product not found.")

    elif choice == 3 : 

        name = str(input("Enter Product Name: "))

        try:
            price = float(input("Enter Price: "))
            stock = int(input("Enter Initial Stock: "))

            if price < 0:
                print("Price cannot be negative.")
                continue

            if stock < 0:
                print("Stock cannot be negative.")
                continue

            product_id = create_product(name, price, stock)

            print(f"New product ID {product_id} has been created.")

        except ValueError:
            print("Please enter valid numbers.")

    elif choice == 4:
        try:
            product_id = int(input("Enter product ID: "))
            new_stock = int(input("Enter new stock quantity: "))

            if new_stock < 0:
                print("Stock cannot be negative.")
                continue

            updated = update_product_stock(product_id, new_stock)

            if updated:
                print(f"Product {product_id} stock updated to {new_stock}.")
            else:
                print(f"Product with ID {product_id} not found.")

        except ValueError:
            print("Please enter valid whole numbers.")


    elif choice == 5:
        try:
            product_id = int(input("Enter product ID to delete: "))

            deleted = delete_product(product_id)

            if deleted:
                print(f"Product {product_id} deleted successfully.")
            else:
                print(f"Product with ID {product_id} not found.")

        except ValueError:
            print("Please enter a valid product ID.")



