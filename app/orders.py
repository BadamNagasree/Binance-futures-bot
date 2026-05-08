from app.client import BinanceFuturesClient

client = BinanceFuturesClient()


def create_market_order(symbol, side, quantity):

    params = {
        "symbol": symbol,
        "side": side,
        "type": "MARKET",
        "quantity": quantity
    }

    return client.place_order(params)


def create_limit_order(symbol, side, quantity, price):

    params = {
        "symbol": symbol,
        "side": side,
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": quantity,
        "price": price
    }

    return client.place_order(params)