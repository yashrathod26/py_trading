from bot import BasicBot
from binance.enums import *

def main():
    api_key = input("Enter your API Key: ")
    api_secret = input("Enter your API Secret: ")
    bot = BasicBot(api_key, api_secret)

    while True:
        print("\n=== Trading Bot ===")
        symbol = input("Symbol (e.g., BTCUSDT): ").upper()
        side = input("Side (BUY/SELL): ").upper()
        order_type = input("Order type (MARKET/LIMIT): ").upper()
        quantity = float(input("Quantity: "))
        price = None

        if order_type == "LIMIT":
            price = input("Limit price: ")

        order = bot.place_order(symbol, side, order_type, quantity, price)
        if order:
            print("Order placed successfully.")
        else:
            print("Order failed.")

        again = input("Place another order? (y/n): ")
        if again.lower() != 'y':
            break

if __name__ == "__main__":
    main()