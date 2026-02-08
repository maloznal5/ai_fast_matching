import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/inventory.db')

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Створюємо базу з повним набором полів
    cursor.execute('DROP TABLE IF EXISTS products')
    cursor.execute('''CREATE TABLE products 
        (sku TEXT PRIMARY KEY, name TEXT, category TEXT, diameter TEXT, length TEXT, din TEXT, strength TEXT, weight_1000 REAL, stock_qty INTEGER)''')
    
    # Розширений список (Болти, Гайки, Саморізи, Шурупи)
    items = [
        ('B-24-95-5.8', 'Болт М24х95 DIN 931', 'Болти', '24', '95', 'DIN 931', '5.8', 491.0, 500),
        ('B-16-80-8.8', 'Болт М16х80 DIN 933', 'Болти', '16', '80', 'DIN 933', '8.8', 161.0, 4000),
        ('N-16-8.0', 'Гайка М16 DIN 934', 'Гайки', '16', '-', 'DIN 934', '8.0', 33.0, 6000),
        ('S-4.2-19-PZ', 'Саморіз 4.2х19 для металу', 'Саморізи', '4.2', '19', 'DIN 7504', 'Сталь', 2.5, 50000),
        ('W-6.0-100-W', 'Шуруп по дереву 6.0х100', 'Шурупи', '6.0', '100', 'DIN 571', '4.8', 18.5, 15000),
        ('A-12-150', 'Анкер клиновий М12х150', 'Анкери', '12', '150', 'ETAG 001', 'Сталь', 145.0, 300)
    ]
    
    # Додаємо ще 100 імітованих позицій для масовості
    for i in range(1, 101):
        items.append((f'SKU-GEN-{i}', f'Болт М{8 + i%12}х{20 + i%50} DIN 933', 'Болти', str(8 + i%12), str(20 + i%50), 'DIN 933', '8.8', 15.0 + i, 1000 + i*2))

    cursor.executemany('INSERT OR REPLACE INTO products VALUES (?,?,?,?,?,?,?,?,?)', items)
    conn.commit()
    conn.close()
    print(f"✅ Каталог сайту розширено: {len(items)} позицій завантажено в пам'ять ШІ!")

if __name__ == "__main__":
    populate()
