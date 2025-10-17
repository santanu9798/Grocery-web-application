-- Create the grocery_store database
CREATE DATABASE IF NOT EXISTS grocery_store;

-- Use the grocery_store database
USE grocery_store;

-- Create uom (unit of measurement) table
CREATE TABLE IF NOT EXISTS uom (
    uom_id INT PRIMARY KEY AUTO_INCREMENT,
    uom_name VARCHAR(45) NOT NULL
);

-- Create products table
CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    uom_id INT NOT NULL,
    price_per_unit DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (uom_id) REFERENCES uom(uom_id)
);

-- Create orders table
CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100) NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create order_details table
CREATE TABLE IF NOT EXISTS order_details (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity DECIMAL(10,2) NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert sample data into uom table
INSERT INTO uom (uom_name) VALUES
('Each'),
('Kg'),
('Liter'),
('Gram'),
('Dozen');

-- Insert sample data into products table
INSERT INTO products (name, uom_id, price_per_unit) VALUES
('Banana', 2, 10.00),
('Apple', 2, 15.00),
('Tomato', 2, 20.00),
('Potato', 2, 8.00),
('Onion', 2, 12.00),
('Milk', 3, 25.00),
('Bread', 1, 30.00),
('Eggs', 5, 60.00);
