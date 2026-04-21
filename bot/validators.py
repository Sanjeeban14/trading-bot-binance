VALID_SIDES = ["BUY","SELL"]
VALID_ORDER_TYPES = ["MARKET","LIMIT","STOP"];

def validate_symbol(symbol):
    if not symbol or not isinstance(symbol, str):
        raise ValueError("symbol must be a non-empty string")
    return symbol.upper()

def validate_side(side):
    side = side.upper()
    if side not in VALID_SIDES:
        raise ValueError(f"Invalid side. Must be one of {VALID_SIDES}")
    return side

def validate_order_type(order_type):
    order_type = order_type.upper()
    if order_type not in VALID_ORDER_TYPES:
        raise ValueError(f"Invalid order type. Must be one of {VALID_ORDER_TYPES}")
    return order_type

def validate_quantity(quantity):
    try:
        quantity = float(quantity)
        if quantity<=0:
            raise ValueError
        return quantity
    except:
        raise ValueError("Quantity must be a positive number")
    
def validate_price(price, order_type):
    if order_type in  ["LIMIT","STOP"]:
        if price is None:
            raise ValueError("Price is required for LIMIT and STOP orders")
        try:
            price = float(price)
            if price<=0:
                raise ValueError
            return price
        except:
            raise ValueError("Price must be a positive number")
        return price
    
def validate_stop_price(stop_price, order_type):
    if order_type == "STOP":
        if stop_price is None:
            raise ValueError("stopPrice is required for STOP orders")
        try:
            stop_price = float(stop_price)
            if stop_price<=0:
                raise ValueError
            return stop_price
        except:
            raise ValueError("stopPrice must be a positive number")
    return stop_price