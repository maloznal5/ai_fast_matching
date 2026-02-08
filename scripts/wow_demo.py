import time
import json

def typing_effect(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def generate_invoice(order):
    print("\n" + "═"*55)
    print("              📑 РАХУНОК-ФАКТУРА №" + str(int(time.time()))[-5:])
    print("                 ПОСТАЧАЛЬНИК: KREPEZH.UA")
    print("═"*55)
    print(f" Клієнт: {order['client']} | Компанія: {order['company']}")
    print("-" * 55)
    print(f" {'Назва товару':<30} | {'К-сть':<8} | {'Вага':<8}")
    print("-" * 55)
    
    for item in order['items']:
        name = item['name']
        qty = item['qty']
        weight = item['w_pc'] * qty
        print(f" {name[:30]:<30} | {qty:<8} | {weight:>6.2f} кг")
    
    print("-" * 55)
    print(f" РАЗОМ ВАГА ЗАМОВЛЕННЯ: {order['total_w']:.2f} кг")
    print(f" СТАТУС: ✅ ПЕРЕВІРЕНО AI-АСИСТЕНТОМ")
    print("═"*55)
    print("\n🔗 Посилання на оплату: https://krepezh.ua/pay/inv_" + str(int(time.time()))[-4:])

def run_wow_demo():
    print("\n" + "🚀 ЗАПУСК AI-КОНСУЛЬТАНТА KREPEZH.UA (V.2.0 SENIOR)")
    print("="*55)
    time.sleep(1)

    typing_effect("👤 [КЛІЄНТ]: Привіт! Потрібно 2000 болтів 14х100 і гайки до них.")
    time.sleep(1)
    
    print("\n🤖 [AI ПАМ'ЯТЬ]: Вітаю, Євгене! Пам'ятаю ваш стандарт: DIN 933, міцність 8.8.")
    typing_effect("⚙️  [Етап 1+2]: Оцифровка заявки + Метчинг з базою 20,000 позицій...")
    time.sleep(2)

    order_data = {
        "client": "Євген",
        "company": "Metiz-Trade",
        "items": [
            {"name": "Болт М14х100 DIN 933 8.8", "qty": 2000, "w_pc": 0.145},
            {"name": "Гайка М14 DIN 934 8.0", "qty": 2000, "w_pc": 0.025}
        ],
        "total_w": 340.00
    }

    print("\n✅ ТОВАРИ ЗНАЙДЕНО. ФОРМУЮ ФІНАЛЬНИЙ ДОКУМЕНТ...")
    time.sleep(1.5)
    
    generate_invoice(order_data)
    
    print("\n" + "="*55)
    print("🏁 ДЕМО ЗАВЕРШЕНО: ВІД ПЕРШОГО СЛОВА ДО ГОТОВОГО РАХУНКУ")
    print("="*55)

if __name__ == "__main__":
    run_wow_demo()
