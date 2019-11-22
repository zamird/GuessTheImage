from flask import Flask
import get_ids_from_folder
from app import guess_the_image_content

client = Flask(__name__)


@client.route('/')
def home():
    res = f'<!DOCTYPE html><html><body><h1>Welcome to Guess The Image App!</h1><br>'
    res = res + f'<p><b>Currently supported requests: </b><br>'
    res = res + f'<b>1. Get list of files within folder: </b> GET /folder/<i>folder_id</i> <br>'
    res = res + f'<b>2. Guess content of image, based on file_id: </b>' \
                f'GET /folder/<i>folder_id</i>/file/<i>file_id</i>'
    res = res + f'</p></body></html>'
    return res


@client.route('/folder/<string:folder_id>')
def get_files_for_folder(folder_id):
    file_list = get_ids_from_folder.get_ids(folder_id)
    res = f'<!DOCTYPE html><html><body><p>Files in folder: <br>'
    res = res + f'{file_list}'
    res = res + f'</p></body></html>'
    return res


@client.route('/folder/<string:folder_id>/file/<string:file_id>')
def get_concepts_for_file(folder_id, file_id):
    file_list = get_ids_from_folder.get_ids(folder_id)
    if file_id not in file_list:
        res = f'<!DOCTYPE html><html><body><p>'
        res = res + f'File {file_id} is not in folder {folder_id}'
        res = res + f'</p></body></html>'
        return res
    res = f'<!DOCTYPE html><html><body><p>The app will try to guess the content of the image: <br>'
    res = res + f'<br>{guess_the_image_content(file_id)}</p><br>'
    res = res + f'<img src="https://drive.google.com/thumbnail?id={file_id}' \
                f'&sz=w400-h300-p-k-nu" alt="Image" height="100" width="100"></body></html>'
    return res


client.run()
