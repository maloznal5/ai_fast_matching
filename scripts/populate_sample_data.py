import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/inventory.db')

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Реальні позиції з файлів замовника (заявка.pdf, Додаток 3, Фото)
    samples = [
        ('933-14-100-8.8', 'Болт М14х100 DIN 933 8.8', '14', '100', 'DIN 933', 'Сталь 8.8', 0.145),
        ('933-16-80-8.8', 'Болт М16х80 DIN 933 8.8', '16', '80', 'DIN 933', 'Сталь 8.8', 0.165),
        ('934-16-8.0', 'Гайка М16 DIN 934 8.0', '16', '-', 'DIN 934', 'Сталь 8.0', 0.033),
        ('AN-10-120', 'Анкер однорозпірний М10/12х120', '10', '120', 'Анкер', 'Сталь', 0.110),
        ('975-16-1000', 'Шпилька різьбова М16х1000 DIN 975', '16', '1000', 'DIN 975', 'Сталь 8.8', 1.330)
    ]
    
    cursor.executemany('''
        INSERT OR REPLACE INTO inventory (sku, name, diameter, length, din_standard, material, weight_per_unit)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', samples)
    
    conn.commit()
    conn.close()
    print("✅ База даних наповнена прикладами з реальних файлів!")

if __name__ == "__main__":
    populate()
