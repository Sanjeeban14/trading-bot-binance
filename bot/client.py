from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

def get_client():
    client = Client(API_KEY, API_SECRET, testnet=True)
    client.API_URL = "https://testnet.binancefuture.com/fapi"
    return client

if __name__ == "__main__":
    client = get_client()
    print(client.futures_account_balance())