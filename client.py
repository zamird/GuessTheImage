from flask import Flask
import get_ids_from_folder
from app import guess_the_image_content

client = Flask(__name__)


@client.route('/')
def home():
    image_id = get_ids_from_folder.get_ids('1W9QPPgnXqJkY4pk0Wcx0m427JNT1Hwer')[0]
    res = f'<!DOCTYPE html><html><body>First file in folder "1W9QPPgnXqJkY4pk0Wcx0m427JNT1Hwer": "{image_id}"<br>'
    res = res + f'The app will now try to guess the content of the image: <br>{guess_the_image_content(image_id)}<br>'
    res = res + f'<img src="https://drive.google.com/thumbnail?id={image_id}' \
                f'&sz=w400-h300-p-k-nu" alt="Image" height="100" width="100"></body></html>'

    return res
    # return 'hello world!'


client.run()
