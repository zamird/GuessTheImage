from requests import request
from bs4 import BeautifulSoup as bs


get_ids_from_folder_url = \
    'https://script.google.com/macros/s/AKfycbwTRBhATWFXJjIWiA9re0SjKkKXC-rGFySAxE8dz8e2Nwj2ClA/exec'


def _parser(resp):
    return str(bs(resp.content, "html.parser")
               .find('body')
               .text
               .split('userHtml')[1]
               .split(':')[1]).split('\\x22')[1].split('\\x22')[0].split(',')


def get_ids(folder_id):
    params = {'id': folder_id}
    res = request(method='GET', url=get_ids_from_folder_url, params=params)
    if res.status_code == 200:
        return _parser(res)
    else:
        return "Error: " + res.status_code

