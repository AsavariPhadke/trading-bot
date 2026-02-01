import argparse
from dotenv import load_dotenv

from bot.client import MockBinanceClient
from bot.orders import create_order_payload
from bot.logging_config import setup_logging

# Load env (safe even if .env does not exist)
load_dotenv()

# Toggle execution mode
USE_MOCK = True


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)
    parser.add_argument("--stop-price", type=float)

    args = parser.parse_args()

    # Client selection
    if USE_MOCK:
        client = MockBinanceClient()
    else:
        raise RuntimeError("Real API mode disabled")

    payload = create_order_payload(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price,
        args.stop_price,
    )

    response = client.place_order(**payload)

    print("\n✅ Order placed successfully!")
    print(f"Order ID: {response['orderId']}")
    print(f"Status: {response['status']}")
    print(f"Executed Qty: {response.get('executedQty')}")
    print(f"Avg Price: {response.get('avgPrice', 'N/A')}")


if __name__ == "__main__":
    main()
