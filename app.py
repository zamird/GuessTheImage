from flask import Flask
import get_ids_from_folder
from client import *

app = Flask(__name__)


@app.route('/')
def home():
    example_file = '1uIDZvtEKvVIUak8wv_qrE-wNTSb3cf4a'
    example_folder = '1W9QPPgnXqJkY4pk0Wcx0m427JNT1Hwer'

    res = f'<!DOCTYPE html><html><body><h1>Welcome to Guess The Image App!</h1><br>'

    res = res + f'<p><b>Example file (tiger): </b><br> {example_file} </p><br>'
    res = res + f'<p><b>Example folder (DDG): </b><br> {example_folder} </p><br>'

    res = res + f'<p><b>Currently supported requests: </b><br><ul>'
    res = res + f'<b><li>Get list of files within folder: </b> GET /folder/<i>folder_id</i> </li><br>'
    res = res + f'<b><li>Guess content of image, based on file_id: </b>' \
                f'GET /folder/<i>folder_id</i>/file/<i>file_id</i></li>'
    res = res + f'</ul></p>'

    res = res + f'<p><b>Demo:</b><br>'
    res = res + f'<iframe width="560" height="315" src="https://www.youtube.com/embed/H8DGac_hHEs" ' \
                f'frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; ' \
                f'picture-in-picture" allowfullscreen></iframe></p>'

    res = res + f'</body></html>'

    return res


@app.route('/folder/<string:folder_id>')
def get_files_for_folder(folder_id):
    file_list = get_ids_from_folder.get_ids(folder_id)
    res = f'<!DOCTYPE html><html><body><p>Files in folder: <br>'
    res = res + f'{file_list}'
    res = res + f'</p></body></html>'
    return res


@app.route('/file/<string:file_id>/thumbnail')
def get_thumbnail(file_id):
    res = f'<!DOCTYPE html><html><body>'
    res = res + f'<img src="https://drive.google.com/thumbnail?id={file_id}' \
                f'&sz=w400-h300-p-k-nu" alt="Thumbnail" height="100" width="100"></body></html>'
    return res


@app.route('/file/<string:file_id>/cache')
def get_cache(file_id):
    client = Client(file_id)
    res = f'<!DOCTYPE html><html><body>'
    res = res + str(client.get_cache())
    res = res + f'</body></html>'
    return res


@app.route('/file/<string:file_id>/cache/clear')
def clear_cache(file_id):
    client = Client(file_id)
    client.clear_cache()
    res = f'<!DOCTYPE html><html><body>'
    res = res + client.get_cache()
    res = res + f'</body></html>'
    return res


@app.route('/file/<string:file_id>')
def get_file(file_id):
    res = f'<!DOCTYPE html><html><body><p>The app will try to guess the content of the image: <br>'
    client = Client(file_id)
    if '' == client.get_cache():
        res = res + f'<br>{client.guess_the_image_content()}</p><br>'
        res = res + f'</body></html>'
        client.set_cache()
        return res
    res = res + f'<br>{client.get_cache()}</p><br>'
    res = res + f'</body></html>'
    return res


@app.route('/folder/<string:folder_id>/file/<string:file_id>')
def get_concepts_for_file(folder_id, file_id):
    file_list = get_ids_from_folder.get_ids(folder_id)
    if file_id not in file_list:
        res = f'<!DOCTYPE html><html><body><p>'
        res = res + f'File {file_id} is not in folder {folder_id}'
        res = res + f'</p></body></html>'
        return res

    client = Client(file_id)
    res = f'<!DOCTYPE html><html><body><p>The app will try to guess the content of the image: <br>'
    res = res + f'<br>{client.guess_the_image_content()}</p><br>'
    res = res + f'<img src="https://drive.google.com/thumbnail?id={file_id}' \
                f'&sz=w400-h300-p-k-nu" alt="Thumbnail" height="100" width="100">'
    res = res + f'</body></html>'
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
