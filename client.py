from flask import Flask
import get_ids_from_folder
from  app import guess_the_image_content

client = Flask(__name__)


@client.route('/')
def home():
    image_id = get_ids_from_folder.get_ids('1W9QPPgnXqJkY4pk0Wcx0m427JNT1Hwer')[0]
    res = f'First file in folder "1W9QPPgnXqJkY4pk0Wcx0m427JNT1Hwer": {image_id}'
    res = res + f'The app will now try to guess the conent of the image: {guess_the_image_content(image_id)}'

    return res
    # return 'hello world!'


client.run()
