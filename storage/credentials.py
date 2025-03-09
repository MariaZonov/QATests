"""
Файл с константами логинов, паролей. Данные тестовых учетных записей хранятся в переменных ci-сборки
или локальном evn-файле
"""
import os
from dotenv import load_dotenv

load_dotenv()


class CatApiUser:
    X_API_KEY = f"{os.getenv('X_API_KEY')}"
