from bot.validators import validate_order_input

def create_order_payload(symbol, side, order_type, quantity, price, stop_price=None):
    validate_order_input(symbol, side, order_type, quantity, price, stop_price)

    payload = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    if order_type == "LIMIT":
        payload["price"] = price
        payload["timeInForce"] = "GTC"

    if order_type == "STOP":
        payload["price"] = price
        payload["stopPrice"] = stop_price
        payload["timeInForce"] = "GTC"

    return payload
