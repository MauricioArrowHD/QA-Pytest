import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://interview.quickarrowshd.com")
LOGIN_ENDPOINT = "/interview/api/v1/login"
TIMEOUT = 10
