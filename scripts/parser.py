import os
import json
from openai import OpenAI
from dotenv import load_dotenv
import sys

# Додаємо шлях до конфігів
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from config.prompts import SYSTEM_PROMPT

# Завантаження ключа з правильним шляхом
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(base_dir, 'security/.env'))

# Ініціалізація без зайвих аргументів
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def parse_text(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            response_format={ "type": "json_object" }
        )
        return response.choices[0].message.content
    except Exception as e:
        return json.dumps({"error": str(e)})

if __name__ == "__main__":
    test_text = "болт 10х50 DIN 933 оцинкований 100 шт"
    print(parse_text(test_text))
