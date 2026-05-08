import time
import hmac
import hashlib
import requests

from urllib.parse import urlencode

from app.config import API_KEY, API_SECRET, BASE_URL
from app.logger import logger


class BinanceFuturesClient:

    def __init__(self):

        self.base_url = BASE_URL
        self.api_key = API_KEY
        self.api_secret = API_SECRET

    def generate_signature(self, params):

        query_string = urlencode(params)

        return hmac.new(
            self.api_secret.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()

    def place_order(self, params):

        endpoint = "/fapi/v1/order"

        params["timestamp"] = int(time.time() * 1000)

        signature = self.generate_signature(params)

        params["signature"] = signature

        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        url = self.base_url + endpoint

        logger.info(f"REQUEST -> {params}")

        try:

            response = requests.post(
                url,
                headers=headers,
                params=params,
                timeout=10
            )

            logger.info(f"RESPONSE -> {response.text}")

            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError as e:

            logger.error(f"HTTP ERROR -> {e}")
            logger.error(response.text)

            raise Exception(response.text)

        except requests.exceptions.ConnectionError:

            logger.error("NETWORK ERROR")

            raise Exception("Network connection error.")

        except requests.exceptions.Timeout:

            logger.error("TIMEOUT ERROR")

            raise Exception("Request timeout.")

        except Exception as e:

            logger.error(f"UNKNOWN ERROR -> {str(e)}")

            raise Exception(str(e))