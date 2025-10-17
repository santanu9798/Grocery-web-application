import mysql.connector
from mysql.connector import Error

def create_database_and_tables():
    try:
        # Connect to MySQL server (without specifying database)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='098765'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS grocery_store")
            print("Database 'grocery_store' created successfully!")
            
            # Use the database
            cursor.execute("USE grocery_store")
            
            # Create uom table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS uom (
                    uom_id INT PRIMARY KEY AUTO_INCREMENT,
                    uom_name VARCHAR(45) NOT NULL
                )
            """)
            print("Table 'uom' created successfully!")
            
            # Create products table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    product_id INT PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(100) NOT NULL,
                    uom_id INT NOT NULL,
                    price_per_unit DECIMAL(10,2) NOT NULL,
                    FOREIGN KEY (uom_id) REFERENCES uom(uom_id)
                )
            """)
            print("Table 'products' created successfully!")
            
            # Create orders table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS orders (
                    order_id INT PRIMARY KEY AUTO_INCREMENT,
                    customer_name VARCHAR(100) NOT NULL,
                    total DECIMAL(10,2) NOT NULL,
                    datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            print("Table 'orders' created successfully!")
            
            # Create order_details table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS order_details (
                    order_id INT NOT NULL,
                    product_id INT NOT NULL,
                    quantity DECIMAL(10,2) NOT NULL,
                    total_price DECIMAL(10,2) NOT NULL,
                    FOREIGN KEY (order_id) REFERENCES orders(order_id),
                    FOREIGN KEY (product_id) REFERENCES products(product_id)
                )
            """)
            print("Table 'order_details' created successfully!")
            
            # Insert sample data into uom table
            uom_data = [
                ('Each',),
                ('Kg',),
                ('Liter',),
                ('Gram',),
                ('Dozen',)
            ]
            
            cursor.executemany("INSERT IGNORE INTO uom (uom_name) VALUES (%s)", uom_data)
            print("Sample UOM data inserted successfully!")
            
            # Insert sample data into products table
            products_data = [
                ('Banana', 2, 10.00),
                ('Apple', 2, 15.00),
                ('Tomato', 2, 20.00),
                ('Potato', 2, 8.00),
                ('Onion', 2, 12.00),
                ('Milk', 3, 25.00),
                ('Bread', 1, 30.00),
                ('Eggs', 5, 60.00)
            ]
            
            cursor.executemany("INSERT IGNORE INTO products (name, uom_id, price_per_unit) VALUES (%s, %s, %s)", products_data)
            print("Sample products data inserted successfully!")
            
            connection.commit()
            print("Database setup completed successfully!")
            
    except Error as e:
        print(f"Error: {e}")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database_and_tables()
