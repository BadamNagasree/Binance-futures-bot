from app.orders import create_market_order, create_limit_order

from app.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

SUPPORTED_SYMBOLS = {
    "BTCUSDT": "Bitcoin",
    "ETHUSDT": "Ethereum",
    "BNBUSDT": "Binance Coin",
    "XRPUSDT": "Ripple",
    "SOLUSDT": "Solana",
    "ADAUSDT": "Cardano",
    "DOGEUSDT": "Dogecoin",
    "LTCUSDT": "Litecoin",
    "TRXUSDT": "Tron",
    "AVAXUSDT": "Avalanche",
    "DOTUSDT": "Polkadot",
    "LINKUSDT": "Chainlink",
    "MATICUSDT": "Polygon",
    "ATOMUSDT": "Cosmos"
}


def display_symbols():

    print("\n====== SUPPORTED COINS ======\n")

    print(f"{'SYMBOL':<12} ASSET")
    print("-" * 35)

    for symbol, asset in SUPPORTED_SYMBOLS.items():
        print(f"{symbol:<12} {asset}")

    print("\n=============================\n")


def print_response(response):

    print("\n========== ORDER RESPONSE ==========")

    print(f"Order ID      : {response.get('orderId')}")
    print(f"Symbol        : {response.get('symbol')}")
    print(f"Status        : {response.get('status')}")
    print(f"Side          : {response.get('side')}")
    print(f"Type          : {response.get('type')}")
    print(f"Executed Qty  : {response.get('executedQty')}")
    print(f"Average Price : {response.get('avgPrice')}")

    print("====================================\n")


def run_cli():

    print("\n===== Binance Futures Testnet Bot =====")

    display_symbols()

    try:

        symbol = validate_symbol(
            input("Enter Symbol: ")
        )

        if symbol not in SUPPORTED_SYMBOLS:
            raise ValueError("Unsupported trading pair.")

        side = validate_side(
            input("Enter Side (BUY/SELL): ")
        )

        order_type = validate_order_type(
            input("Enter Order Type (MARKET/LIMIT): ")
        )

        quantity = validate_quantity(
            input("Enter Quantity: ")
        )

        print("\n========== ORDER REQUEST ==========")

        print(f"Asset      : {SUPPORTED_SYMBOLS[symbol]}")
        print(f"Symbol     : {symbol}")
        print(f"Side       : {side}")
        print(f"Order Type : {order_type}")
        print(f"Quantity   : {quantity}")

        if order_type == "MARKET":

            response = create_market_order(
                symbol,
                side,
                quantity
            )

        else:

            price = validate_price(
                input("Enter Price: ")
            )

            print(f"Price      : {price}")

            response = create_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        print("===================================\n")

        print_response(response)

        print("SUCCESS: Order placed successfully.")

    except ValueError as ve:

        print(f"VALIDATION ERROR: {ve}")

    except Exception as e:

        print(f"ERROR: {e}")