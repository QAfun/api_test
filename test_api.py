# -*- encoding=utf8 -*-

import requests

url = 'http://ip-api.com/json'

def test_check_country():

    res = requests.get(url)
    data = res.json()

    country = data.get('country')

    assert country == 'Belarus', 'Country is wrong!'
    






