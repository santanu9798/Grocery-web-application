import sqlite3
import os

__cnx = None

def get_sql_connection():
    print("Opening SQLite connection")
    global __cnx
    
    if __cnx is None:
        # Create database file in the backend directory
        db_path = os.path.join(os.path.dirname(__file__), 'grocery_store.db')
        __cnx = sqlite3.connect(db_path, check_same_thread=False)
        __cnx.row_factory = sqlite3.Row  # This allows accessing columns by name
        
        # Initialize database if it doesn't exist
        initialize_database(__cnx)
    
    return __cnx

def initialize_database(connection):
    cursor = connection.cursor()
    
    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS uom (
            uom_id INTEGER PRIMARY KEY AUTOINCREMENT,
            uom_name VARCHAR(45) NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            uom_id INTEGER NOT NULL,
            price_per_unit DECIMAL(10,2) NOT NULL,
            FOREIGN KEY (uom_id) REFERENCES uom(uom_id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name VARCHAR(100) NOT NULL,
            total DECIMAL(10,2) NOT NULL,
            datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS order_details (
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity DECIMAL(10,2) NOT NULL,
            total_price DECIMAL(10,2) NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    ''')
    
    # Check if sample data already exists
    cursor.execute("SELECT COUNT(*) FROM uom")
    if cursor.fetchone()[0] == 0:
        # Insert sample data
        cursor.executemany("INSERT INTO uom (uom_name) VALUES (?)", [
            ('Each',), ('Kg',), ('Liter',), ('Gram',), ('Dozen',)
        ])
        
        cursor.executemany("INSERT INTO products (name, uom_id, price_per_unit) VALUES (?, ?, ?)", [
            ('Banana', 2, 10.00),
            ('Apple', 2, 15.00),
            ('Tomato', 2, 20.00),
            ('Potato', 2, 8.00),
            ('Onion', 2, 12.00),
            ('Milk', 3, 25.00),
            ('Bread', 1, 30.00),
            ('Eggs', 5, 60.00)
        ])
    
    connection.commit()
    print("Database initialized successfully")
