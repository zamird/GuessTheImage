from requests import request
from bs4 import BeautifulSoup as bs
import json

update_image_description_url = \
    'https://script.google.com/macros/s/AKfycbwEA5-dGG_oP5qFWy31NTwi_PmS7Te0Phwi9TG98oKaYL5VWaT7/exec'


def _parser(resp):
    return str(bs(resp.content, "html.parser")
               .find('body')
               .text
               .split('userHtml')[1]).split('\\x22')[1].split('\\x22')[0]


def set_description(file_id, description):
    params = {'id': file_id, 'description': json.dumps(description)}
    res = request(method='GET', url=update_image_description_url, params=params)
    if res.status_code == 200:
        return _parser(res)
    else:
        return "Error: " + res.status_code


def get_description(file_id):
    params = {'id': file_id}
    res = request(method='GET', url=update_image_description_url, params=params)
    if res.status_code == 200:
        return _parser(res)
    else:
        return "Error: " + res.status_code
