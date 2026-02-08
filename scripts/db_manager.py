import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/inventory.db')

def init_db():
    # Переконуємось, що папка data існує
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Таблиця нашої номенклатури (20к позицій)
    # В SQLite INTEGER PRIMARY KEY автоматично є автоінкрементом
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY,
            internal_id TEXT,
            name TEXT,
            diameter TEXT,
            length TEXT,
            standard TEXT,
            material TEXT,
            coating TEXT,
            unit TEXT
        )
    ''')
    
    # Таблиця відповідностей (Match history)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS match_history (
            id INTEGER PRIMARY KEY,
            client_text TEXT,
            inventory_id INTEGER,
            confidence REAL,
            FOREIGN KEY (inventory_id) REFERENCES inventory (id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print(f"✅ База даних успішно ініціалізована: {DB_PATH}")

if __name__ == "__main__":
    init_db()
