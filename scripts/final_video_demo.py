import json
import time

def run_demo():
    print("\n" + "="*60)
    print("🚀 AI FAST MATCHING SYSTEM - KREPEZH.UA (STAGE 1 + 2)")
    print("="*60)
    time.sleep(1)

    print("\n[STEP 1] 📄 Оцифровка заявки (Етап 1)...")
    time.sleep(1)
    print("📥 Розпізнано: Болт М14х100 (1200 шт) + Гайка М14 (1200 шт)")
    time.sleep(1.5)

    print("\n[STEP 2] 🧠 Пошук у базі 20,000+ позицій (Етап 2)...")
    time.sleep(1)
    order_items = [
        {"sku": "B-14-100-8.8", "name": "Болт М14х100 DIN 933 8.8", "qty": 1200, "weight": 0.145},
        {"sku": "N-14-8.0", "name": "Гайка М14 DIN 934 8.0", "qty": 1200, "weight": 0.025}
    ]
    
    total_weight = 0
    for item in order_items:
        w = item['qty'] * item['weight']
        total_weight += w
        print(f"✅ Знайдено: {item['name']} | SKU: {item['sku']}")
        time.sleep(1)

    print(f"\n[STEP 3] ⚖️ Авто-розрахунок ваги замовлення: {total_weight:.2f} кг")
    time.sleep(1.5)

    print("\n[STEP 4] 📡 Формування JSON для адмін-панелі...")
    final_order = {
        "status": "SUCCESS",
        "client": "Evgen_Senior",
        "total_weight_kg": round(total_weight, 2),
        "items_count": len(order_items),
        "data_ready": True
    }
    time.sleep(1)
    print(json.dumps(final_order, indent=4, ensure_ascii=False))
    
    print("\n" + "="*60)
    print("✅ ЕТАПИ 1 ТА 2 УСПІШНО ОБ'ЄДНАНІ ТА ГОТОВІ!")
    print("="*60)

if __name__ == "__main__":
    run_demo()
