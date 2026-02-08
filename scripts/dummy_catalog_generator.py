import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/inventory.db')

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Створюємо таблицю з 8 колонками, якщо вона не існує
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products 
        (sku TEXT PRIMARY KEY, name TEXT, diameter TEXT, length TEXT, din TEXT, strength TEXT, weight_1000 REAL, stock_qty INTEGER)
    ''')
    
    # Дані на основі ваших документів (додано 8-й параметр - залишок на складі)
    products = [
        ('B-24-95-5.8', 'Болт М24х95 DIN 931', '24', '95', 'DIN 931', '5.8', 491.0, 500),
        ('B-16-80-8.8', 'Болт М16х80 DIN 933', '16', '80', 'DIN 933', '8.8', 161.0, 4050),
        ('B-14-100-8.8', 'Болт М14х100 DIN 933', '14', '100', 'DIN 933', '8.8', 145.0, 1200),
        ('B-10-60-10.9', 'Болт М10х60 DIN 933', '10', '60', 'DIN 933', '10.9', 51.0, 700),
        ('N-16-8.0', 'Гайка М16 DIN 934', '16', '-', 'DIN 934', '8.0', 33.0, 6840),
        ('A-10-120', 'Анкер М10/12х120', '10', '120', 'Анкер', 'Сталь', 110.0, 50)
    ]
    
    # Видаляємо стару таблицю, якщо структура конфліктує
    cursor.execute('DROP TABLE IF EXISTS products')
    cursor.execute('CREATE TABLE products (sku TEXT PRIMARY KEY, name TEXT, diameter TEXT, length TEXT, din TEXT, strength TEXT, weight_1000 REAL, stock_qty INTEGER)')
    
    cursor.executemany('INSERT OR REPLACE INTO products VALUES (?,?,?,?,?,?,?,?)', products)
    conn.commit()
    conn.close()
    print("✅ База даних синхронізована та заповнена прикладами!")

if __name__ == "__main__":
    populate()
