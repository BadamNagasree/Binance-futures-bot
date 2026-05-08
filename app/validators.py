VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_symbol(symbol):

    symbol = symbol.upper()

    if not symbol.isalnum():
        raise ValueError("Invalid symbol format.")

    return symbol


def validate_side(side):

    side = side.upper()

    if side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL.")

    return side


def validate_order_type(order_type):

    order_type = order_type.upper()

    if order_type not in VALID_ORDER_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT.")

    return order_type


def validate_quantity(quantity):

    try:
        qty = float(quantity)

        if qty <= 0:
            raise ValueError

        return qty

    except:
        raise ValueError("Quantity must be positive.")


def validate_price(price):

    try:
        p = float(price)

        if p <= 0:
            raise ValueError

        return p

    except:
        raise ValueError("Price must be positive.")