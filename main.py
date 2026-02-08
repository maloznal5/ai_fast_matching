import os
import json
import pandas as pd
from scripts.parser import parse_text

def create_excel_report(raw_data_list, output_filename="data/output/report_v1.xlsx"):
    # Создаем папку для вывода, если её нет
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    
    parsed_results = []
    
    print(f"Обработка {len(raw_data_list)} позиций...")
    
    for text in raw_data_list:
        result_json = parse_text(text)
        data = json.loads(result_json)
        # Добавляем исходный текст для отчета
        data['original_text'] = text
        parsed_results.append(data)
    
    # Создаем таблицу
    df = pd.DataFrame(parsed_results)
    
    # Переименовываем колонки для презентабельности перед заказчиком
    column_mapping = {
        'original_text': 'Товар в заявке',
        'diameter': 'Диаметр',
        'length': 'Длина',
        'standard': 'Стандарт (DIN)',
        'material': 'Материал',
        'coating': 'Покрытие',
        'qty': 'Кол-во',
        'unit': 'Ед. изм.',
        'confidence': 'Уверенность AI'
    }
    df = df.rename(columns=column_mapping)
    
    # Сохраняем
    df.to_excel(output_filename, index=False)
    print(f"Отчет успешно создан: {output_filename}")

if __name__ == "__main__":
    # Тестовый набор данных (имитация заявки клиента)
    sample_order = [
        "болт 10х50 DIN 933 оцинкованный 100 шт",
        "гайка М6 8.0 без покрытия 500 штук",
        "шуруп самонарезающий 4.2х19 со сверлом 1000 шт"
    ]
    create_excel_report(sample_order)
