from clarifai.rest import ClarifaiApp
from print import Print as Ptr
from generate_tags_json import GenerateTagsJson as TagsJsn
from update_image_description import *


class Client:
    def __init__(self, image_id):
        self.app = ClarifaiApp(api_key='57c6104fb12f460db9674c3c86968020')
        general_model = self.app.public_models.general_model
        color_model = self.app.public_models.color_model
        custom_model = self.app.models.get('object-recognition-model')
        self.printer = Ptr(general_model, color_model, custom_model)
        self.tags_json = TagsJsn(general_model, color_model, custom_model)
        self.image_id = image_id

    def guess_the_image_content(self):
        self.printer.set_image_id(self.image_id)
        self.tags_json.set_image_id(self.image_id)
        concepts = self.printer.get_concepts(custom_only=True)
        colors_hex = self.printer.get_colors_hex()
        return {'concepts': concepts, 'colors_hex': colors_hex}

    def set_cache(self):
        set_description(self.image_id, self.guess_the_image_content())

    def get_cache(self):
        cache = get_description(self.image_id)
        if 'concepts' in cache:
            return cache
        return ''

    def clear_cache(self):
        set_description(self.image_id, "")
