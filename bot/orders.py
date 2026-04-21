from bot.client import get_client
from bot.logging_config import setup_logger

logger = setup_logger()

def place_market_order(symbol, side, quantity):
    client = get_client()

    try:
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        logger.info(f"Response: {response}")
        return response
    except Exception as e:
        logger.error(f"Error placing MARKET order: {e}")
        return {"error": str(e)}
    
def place_limit_order(symbol, side, quantity, price):
    client = get_client()

    try:
        response = client.futures_create_order(
            symbol = symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
        logger.info(f"Response: {response}")
        return response
    except Exception as e:
        logger.error(f"Error placing LIMIT order: {e}")
        return {"error": str(e)}

def place_stop_limit_order(symbol, side, quantity, price, stop_price):
    client = get_client()
    try:
        logger.info(f"Placing STOP-LIMIT order: {symbol} {side} {quantity} price={price} stop={stop_price}")

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP",
            quantity=quantity,
            price=price,
            stopPrice = stop_price,
            timeInForce="GTC"
        )
        logger.info(f"Response: {response}")
        return response
    except Exception as e:
        logger.error(f"Error placing STOP order: {e}")
        return {"error": str(e)}

if __name__=="__main__":
    print(place_market_order("BTCUSDT", "BUY", 0.001))