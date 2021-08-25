# -*- encoding=utf8 -*-

import requests

def test_check_country():
    res = requests.get('http://ip-api.com/json')
    data = res.json()

    country = data.get('country')

    assert country == 'Belarus', 'Country is wrong!'






