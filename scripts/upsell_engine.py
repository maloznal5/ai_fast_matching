def suggest_related_items(main_item):
    suggestions = {
        "Болт": ["Гайка відповідного діаметру", "Шайба плоска", "Гровер"],
        "Шпилька": ["Гайка подовжена", "Шайба посилена"],
        "Анкер": ["Бур по бетону"]
    }
    
    for key in suggestions:
        if key in main_item:
            return suggestions[key]
    return []

# Демонстрація
item = "Болт М14х100 DIN 933"
print(f"🛒 У кошику: {item}")
related = suggest_related_items(item)
if related:
    print(f"🤖 AI рекомендує додати: {', '.join(related)}")
