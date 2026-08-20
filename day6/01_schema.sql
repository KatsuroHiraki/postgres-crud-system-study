CREATE TABLE employees (
	employee_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR(100) UNIQUE NOT NULL,
	department VARCHAR(50) DEFAULT 'General',
	hire_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE products (
	product_id SERIAL PRIMARY KEY,
	product_name VARCHAR(100) NOT NULL,
	price DECIMAL(10,2) NOT NULL,
	stock_quantity INT DEFAULT 0
);

CREATE TABLE customers (
	customer_id SERIAL primary KEY,
	full_name VARCHAR(100) NOT NULL,
	email varchar(100) UNIQUE NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
	order_id SERIAL PRIMARY KEY,
	customer_id INT REFERENCES customers(customer_id) ON DELETE CASCADE,
	order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	total_amount DECIMAL(10,2) NOT NULL,
	status VARCHAR(20) DEFAULT 'Pending'
);

drop table order;
drop table customers;
drop table products;
drop table employees;
