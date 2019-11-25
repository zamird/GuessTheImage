from requests import request
from bs4 import BeautifulSoup as bs
import json

update_image_description_url = \
    'https://script.google.com/macros/s/AKfycbwEA5-dGG_oP5qFWy31NTwi_PmS7Te0Phwi9TG98oKaYL5VWaT7/exec'


def _parser(resp):
    return str(bs(resp.content, "html.parser")
               .find('body')
               .text
               .split('userHtml')[1]
               .split(':')[1]).split('\\x22')[1].split('\\x22')[0]


def _advanced_parser(resp):
    return str(bs(resp.content.decode(), "html.parser")
               .find('body')
               .text
               .split('\\x22userHtml\\x22:')[1]
               .split('undefined')[0]
               .split('\"')[0]
               .replace('\\\\\\x22', "\"")
               .replace('\\x22\\x7b', "{")
               .replace('\\x7d\\x22', "}")
               .replace('\\\\u0027\\x5d', "\'")
               .replace('\\x5b\\\\u0027', "\'")
               .replace('\\/', '/')
               .split(',\\x22ncc\\x22')[0]
               .replace('\\\\u0027', '\''))


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
        return _advanced_parser(res)
    else:
        return "Error: " + res.status_code
