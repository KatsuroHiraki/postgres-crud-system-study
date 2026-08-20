-- Insert - Seeding initial data

--Insert employees
insert into employees (first_name, last_name, email, department, hire_date) values
('Ahmad', 'Razak', 'ahmad.razak@gmail.com', 'Engineering', '2026-01-15'),
('Siti', 'Nurhaliza', 'siti.nur@yahoo.com', 'Sales', '2025-11-20'),
('Lee', 'Wei', 'lee.wei@gmail.com', 'Support', CURRENT_DATE);

select * from employees;

--Insert products
insert into products (product_name, price, stock_quantity) values 
('Mechanical Keyboard', 120.50, 45),
('Wireless Mouse', 35.00, 100),
('USB-C Docking Station', 85.00, 20);

--Insert customers
insert into customers (full_name, email) values
('Farid Ibrahim', 'farid@gmail.com'),
('Nurul Aini', 'nurul@gmail.com'),
('Chong Ming', 'chong@gmail.com');

--Insert orders
INSERT INTO orders (customer_id, total_amount, status) VALUES
(1, 120.50, 'Pending'),
(2, 35.00, 'Completed'),
(3, 205.50, 'Pending');


--Select (Read)

--retrieve all products with a price greater than 50
select *
from products
where price > 50.00;

--retrieve all employees hired in the current year
select * 
from employees
where extract(year from hire_date) = extract(year from current_date)


--Update 

--update the stock quantity of a product after a sale 
update products
set stock_quantity = stock_quantity - 1
where product_id = 1
 
--change order status from 'pending' to 'completed'
update orders
set status = 'Completed'
where order_id = 1;


--Delete
delete from employees
where employee_id = 3