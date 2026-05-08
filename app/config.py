import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://testnet.binancefuture.com"

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")