import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/inventory.db')

def setup_pro_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 1. Каталог товарів (20 000+ позицій)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            sku TEXT PRIMARY KEY,
            name TEXT,
            diameter TEXT,
            length TEXT,
            din TEXT,
            strength TEXT,
            weight_1000 REAL,
            stock_qty INTEGER
        )
    ''')
    
    # 2. Пам'ять клієнтів
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            preferences TEXT,
            last_order TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
    print(f"✅ База даних SQLite оновлена під Етап 2: {DB_PATH}")

if __name__ == "__main__":
    setup_pro_db()
