import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/inventory.db')

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Таблиця клієнтів (Пам'ять системи)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            client_id INTEGER PRIMARY KEY,
            name TEXT,
            contact_info TEXT,
            preferences TEXT,
            last_order_date TEXT
        )
    ''')
    
    # Таблиця товарів (20к позицій з вагою)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY,
            sku TEXT,
            name TEXT,
            diameter TEXT,
            length TEXT,
            din_standard TEXT,
            weight_per_unit REAL
        )
    ''')
    
    # Таблиця замовлень (Історія для навчання ШІ)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            client_id INTEGER,
            items_json TEXT,
            total_weight REAL,
            FOREIGN KEY (client_id) REFERENCES clients (client_id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print(f"✅ Senior-архітектура з пам'яттю клієнтів готова: {DB_PATH}")

if __name__ == "__main__":
    init_db()
