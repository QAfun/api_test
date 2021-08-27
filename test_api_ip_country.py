# -*- encoding=utf8 -*-

import requests


def test_check_country():
    url = 'http://ip-api.com/json'
    res = requests.get(url)
    data = res.json()

    country = data.get('country')

    assert country == 'Belarus', 'Country is wrong!'

