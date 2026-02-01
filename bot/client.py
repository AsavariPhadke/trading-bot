import logging
import uuid
from datetime import datetime

logger = logging.getLogger(__name__)


class MockBinanceClient:
    """
    Mock Binance Futures client used when API access is unavailable.
    """

    def place_order(self, **kwargs):
        logger.info(f"MOCK REQUEST: {kwargs}")

        response = {
            "orderId": str(uuid.uuid4()),
            "status": "FILLED",
            "symbol": kwargs.get("symbol"),
            "side": kwargs.get("side"),
            "type": kwargs.get("type"),
            "executedQty": kwargs.get("quantity"),
            "avgPrice": kwargs.get("price", "MARKET"),
            "updateTime": datetime.utcnow().isoformat(),
        }

        logger.info(f"MOCK RESPONSE: {response}")
        return response
