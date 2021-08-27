import pytest
import requests
from requests.auth import HTTPBasicAuth

user = 'test_user'
password = 'test_password'


@pytest.fixture()
def auth_cookie():
    url = 'http://0.0.0.0:7000/login'
    result = requests.get(url, auth=HTTPBasicAuth(user, password))
    data = result.json()

    yield data['auth_cookie']


def test_check_login(auth_cookie):
    url = 'http://0.0.0.0:7000/login'
    result = requests.get(url, auth=HTTPBasicAuth(user, password))
    data = result.json()

    print('Status code: ', result.status_code)
    print(result)
    print(data)

    assert result.status_code == 200
    assert 'auth_cookie' in data
    assert data['auth_cookie'] > ''


def test_add_book(auth_cookie):
    url = 'http://0.0.0.0:7000/add_book'
    result = requests.post(url,
                           cookies={'my_cookie': auth_cookie},
                           data={'title': 'Book about QA',
                                 'author': 'Me'})
    assert result.status_code == 200
    result2 = requests.get('http://0.0.0.0:7000/books')
    data = result2.json()

    assert data != []


def test_check_list_of_books(auth_cookie):
    # TODO: rewrite
    url = 'http://0.0.0.0:7000/books'
    result = requests.get(url, cookies={'my_cookie': auth_cookie})

    print(result.text)

    assert result.status_code == 200
