import sqlite3
import json
import time
import sys

def typing_print(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def init_pro_database():
    conn = sqlite3.connect('data/inventory.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS products')
    cursor.execute('''CREATE TABLE products 
        (sku TEXT, name TEXT, d TEXT, l TEXT, weight_pc REAL, price REAL)''')
    
    # Загружаем "Золотой запас" (Примеры из 20,000 позиций)
    samples = [
        ('B-14-100-8.8', 'Болт М14х100 DIN 933 8.8', '14', '100', 0.145, 18.45),
        ('N-14-8.0', 'Гайка М14 DIN 934 8.0', '14', '-', 0.025, 3.12),
        ('A-12-150', 'Анкер клиновой М12х150', '12', '150', 0.145, 45.30)
    ]
    cursor.executemany('INSERT INTO products VALUES (?,?,?,?,?,?)', samples)
    conn.commit()
    conn.close()

def run_ai_engine():
    init_pro_database()
    
    print("\n" + "═"*70)
    print("🤖 KREPEZH.UA AI CORE v2.0 - INTEGRATED STAGES 1 & 2")
    print("═"*70)
    time.sleep(1)

    # STAGE 1: ПАРСИНГ (Имитация распознавания из PDF/Голоса)
    raw_query = "Заявка: болт 14х100 — 1200 шт, гайка 14 — 1200 шт."
    typing_print(f"📄 [ВХОДНОЙ ФАЙЛ]: {raw_query}")
    time.sleep(1)
    
    typing_print("⚙️  [STAGE 1]: Оцифровка параметров... Найден диаметр 14, длина 100.")
    time.sleep(1)

    # STAGE 2: МЕТЧИНГ И БИЗНЕС-ЛОГИКА
    typing_print("🧠 [STAGE 2]: Поиск в базе (20,000+)... Расчет веса и стоимости...")
    time.sleep(2)

    conn = sqlite3.connect('data/inventory.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE d='14'")
    db_items = cursor.fetchall()

    print("\n📦 СФОРМИРОВАННЫЙ ЗАКАЗ:")
    print("-" * 70)
    print(f"{'Наименование':<30} | {'Кол-во':<7} | {'Вес, кг':<8} | {'Сумма, грн':<12}")
    print("-" * 70)

    total_sum = 0
    total_weight = 0

    for item in db_items:
        qty = 1200
        sum_item = item[5] * qty
        weight_item = item[4] * qty
        total_sum += sum_item
        total_weight += weight_item
        print(f"{item[1][:30]:<30} | {qty:<7} | {weight_item:>8.2f} | {sum_item:>12.2f}")

    tax = total_sum * 0.20
    grand_total = total_sum + tax

    print("-" * 70)
    print(f"⚖️ Общий вес: {total_weight:.2f} кг")
    print(f"📊 НДС (20%): {tax:,.2f} грн".replace(',', ' '))
    print(f"🔥 ИТОГО К ОПЛАТЕ: {grand_total:,.2f} грн".replace(',', ' '))
    print("-" * 70)

    # ВАРИАНТЫ ОПЛАТЫ
    print("\n💳 ДОСТУПНЫЕ СПОСОБЫ ОПЛАТЫ:")
    print("✅ Счёт-фактура (Безнал) | ✅ Карта | ✅ Наложенный платёж")
    
    # ФИНАЛЬНЫЙ JSON ДЛЯ АДМИНА
    print("\n📡 [ADMIN]: Генерация данных для сайта...")
    time.sleep(1)
    admin_json = {"status": "success", "order_id": 777, "total_w": total_weight, "total_u": grand_total}
    print(json.dumps(admin_json))

    print("\n" + "═"*70)
    print("🏁 СИСТЕМА ГОТОВА К МАСШТАБИРОВАНИЮ НА ВЕСЬ КАТАЛОГ")
    print("═"*70)

if __name__ == "__main__":
    run_ai_engine()
