import json

def send_to_admin(client_name, order_items):
    print(f"📡 ОТПРАВКА ЗАКАЗА АДМИНИСТРАТОРУ (Сайт krepezh.ua)...")
    
    order_data = {
        "client": client_name,
        "items": order_items,
        "total_weight_kg": sum(item['weight'] for item in order_items),
        "status": "NEW_ORDER_FROM_AI"
    }
    
    # Имитация передачи в админку через JSON
    print("\n📦 ДАННЫЕ ДЛЯ АДМИН-ПАНЕЛИ:")
    print(json.dumps(order_data, indent=4, ensure_ascii=False))
    print("\n✅ Уведомление успешно отправлено админу!")

if __name__ == "__main__":
    # Пример сформированного заказа после общения AI с клиентом
    sample_items = [
        {"sku": "933-14-100-8.8", "name": "Болт М14х100", "qty": 1200, "weight": 174.0},
        {"sku": "934-14-8", "name": "Гайка М14", "qty": 1200, "weight": 30.0}
    ]
    send_to_admin("Евгений (ID: 001)", sample_items)
