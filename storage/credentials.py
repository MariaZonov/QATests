import os
from dotenv import load_dotenv

load_dotenv()


class CatApiUser:
    X_API_KEY = f"{os.getenv('X_API_KEY')}"
