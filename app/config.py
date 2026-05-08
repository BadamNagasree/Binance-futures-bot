import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://fapi.binance.com"

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")