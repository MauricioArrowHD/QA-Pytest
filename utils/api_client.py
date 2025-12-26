import requests
from config.settings import BASE_URL, TIMEOUT

class APIClient:

    def post(self, endpoint, json=None, headers=None):
        return requests.post(
            url=f"{BASE_URL}{endpoint}",
            json=json,
            headers=headers,
            timeout=TIMEOUT
        )
