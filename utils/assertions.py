def assert_status_code(response, expected):
    assert response.status_code == expected, (
        f"Expected {expected}, got {response.status_code}. "
        f"Response: {response.text}"
    )


def assert_has_key(data, key):
    assert key in data, f"Response missing key: {key}"
