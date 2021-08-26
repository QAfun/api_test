import requests
from requests.auth import HTTPBasicAuth

user = 'test_user'
password = 'test_password'


def test_check_login():
    url = 'http://0.0.0.0:7000/login'
    result = requests.get(url, auth=HTTPBasicAuth(user, password))

    data = result.json()

    print('Status code: ', result.status_code)
    print(result)
    print(data)

    assert result.status_code == 200
    assert 'auth_cookie' in data
