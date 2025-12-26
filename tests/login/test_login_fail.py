from config.settings import LOGIN_ENDPOINT
from data.users import INVALID_USER
from utils.assertions import assert_status_code

def test_login_fail(api_client):
    

