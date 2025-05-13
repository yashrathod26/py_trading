import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException
import time

# Setup logging
logging.basicConfig(filename='trading_bot.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == "MARKET":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )
            elif order_type == "LIMIT":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    timeInForce='GTC',
                    quantity=quantity,
                    price=price
                )
            else:
                raise ValueError("Unsupported order type.")

            logging.info(f"Order successful: {order}")
            return order
        except BinanceAPIException as e:
            logging.error(f"Binance API error: {e}")
            return None
        except Exception as e:
            logging.error(f"General error: {e}")
            return None