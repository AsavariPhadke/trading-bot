def validate_order_input(symbol, side, order_type, quantity, price, stop_price=None):
    if side not in {"BUY", "SELL"}:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in {"MARKET", "LIMIT", "STOP"}:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT orders")

    if order_type == "STOP":
        if price is None or stop_price is None:
            raise ValueError("STOP orders require price and stop_price")
