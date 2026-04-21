import argparse

from bot.orders import place_market_order, place_limit_order, place_stop_limit_order
from bot.validators import (
    validate_order_type,
    validate_price,
    validate_quantity,
    validate_side,
    validate_symbol,
    validate_stop_price
)

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument("--symbol", required=True, help="Trading symbol (eg: BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", required=False, help="Price (required for LIMIT)")
    parser.add_argument("--stop_price", required=False, help="Stop price for STOP orders")

    args = parser.parse_args()

    try:
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)
        stop_price = validate_stop_price(args.stop_price,order_type)

        print("\n---Order Summary---")
        print("Symbol: ",symbol)
        print("side: ",side)
        print("Type: ",order_type)
        print("Quantity: ",quantity)
        if order_type == "LIMIT":
            print("Price: ",price)
        if order_type == "STOP":
            print(f"Stop price: {stop_price}")
            print(f"Limit price: {price}")


        if order_type == "MARKET":
            response = place_market_order(symbol, side, quantity)
        elif order_type == "LIMIT":
            response = place_limit_order(symbol, side, quantity, price)
        else:
            response = place_stop_limit_order(symbol, side, quantity, price, stop_price)

        print("\n---Response---")

        if "error" in response:
            print("Error: ",response['error'])
        else:
            print(f"Order ID: {response.get('orderId')}")
            print(f"Status: {response.get('status')}")
            print(f"Executed Qty: {response.get('executedQty')}")
            print(f"Avg Price: {response.get('avgPrice', 'N/A')}")
            print("\n Order placed successfully")

    except Exception as e:
        print(f"\n Validation/Error: {e}")
    

if __name__=="__main__":
    main()