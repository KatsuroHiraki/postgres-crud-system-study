from db import (
    fetch_all_customers,
    add_new_customer,
    get_customer_orders,
)


def run_demo() :

    print('1. Fetching Existing Customers ')

    customers = fetch_all_customers()

    for customer in customers :
        print(customer)

    print('2. Adding New Customer ')

    new_id = add_new_customer("Akio Marc", "kio@chester.edu.uk")

    print(f'Created Customer ID : {new_id}')


    print('3. Fetching Customer Orders ')

    customer_order_id = 2

    orders = get_customer_orders(customer_order_id)

    print(f'Orders for ID {customer_order_id} : {orders}')

run_demo()