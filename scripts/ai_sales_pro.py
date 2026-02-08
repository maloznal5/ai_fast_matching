import time
import json

def format_currency(amount):
    return f"{amount:,.2f} UAH".replace(',', ' ')

def run_sales_demo():
    print("\n" + "🚀 AI SALES AGENT: KREPEZH.UA (STAGE 1 + 2 COMPLETE)")
    print("="*65)
    time.sleep(1)

    # Імітація запиту
    print("👤 [КЛІЄНТ]: Порахуй мені 1200 болтів 14х100 і стільки ж гайок.")
    print("🤖 [AI]: Виконую розрахунок згідно з прайсом та вашими знижками...")
    time.sleep(2)

    # Дані про товари (Прайс-лист для прикладу)
    order_items = [
        {
            "name": "Болт М14х100 DIN 933 8.8",
            "sku": "B-14-100-8.8",
            "price": 18.45,  # Ціна за шт
            "qty": 1200,
            "w_pc": 0.145
        },
        {
            "name": "Гайка М14 DIN 934 8.0",
            "sku": "N-14-8.0",
            "price": 3.12,   # Ціна за шт
            "qty": 1200,
            "w_pc": 0.025
        }
    ]

    print("\n📦 ДЕТАЛІЗАЦІЯ ЗАМОВЛЕННЯ:")
    print("-" * 65)
    print(f"{'Товар':<25} | {'К-сть':<7} | {'Ціна/шт':<10} | {'Сума':<12}")
    print("-" * 65)

    total_amount = 0
    total_weight = 0

    for item in order_items:
        row_sum = item['price'] * item['qty']
        row_weight = item['w_pc'] * item['qty']
        total_amount += row_sum
        total_weight += row_weight
        print(f"{item['name'][:25]:<25} | {item['qty']:<7} | {item['price']:>7.2f} | {format_currency(row_sum):>12}")

    tax = total_amount * 0.20  # ПДВ 20%
    grand_total = total_amount + tax

    print("-" * 65)
    print(f"💰 Промпідсумок:      {format_currency(total_amount)}")
    print(f"📊 ПДВ (20%):         {format_currency(tax)}")
    print(f"🔥 РАЗОМ ДО СПЛАТИ:   {format_currency(grand_total)}")
    print(f"⚖️ ЗАГАЛЬНА ВАГА:     {total_weight:.2f} кг")
    print("-" * 65)

    print("\n💳 ВАРІАНТИ ОПЛАТИ ДЛЯ ВАС:")
    print("1. [Рахунок-фактура] - Безготівковий розрахунок (з ПДВ)")
    print("2. [Visa/Mastercard] - Оплата онлайн на сайті")
    print("3. [Накладений платіж] - При отриманні (Нова Пошта)")
    
    time.sleep(1)
    print("\n🤖 [AI]: Який варіант обрати? Можу миттєво згенерувати посилання.")
    print("\n" + "="*65)

if __name__ == "__main__":
    run_sales_demo()
