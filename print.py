from utils import *


class Print:

    def __init__(self, general_model, color_model, custom_model, url=None, image_id=None):
        self.color_model = color_model
        self.general_model = general_model
        self.custom_model = custom_model
        if url or image_id:
            if image_id:
                url = f'https://drive.google.com/thumbnail?id={image_id}&sz=w400-h300-p-k-nu'
            self.url = url
            self.color_res = self.color_model.predict_by_url(url)
            self.general_res = self.general_model.predict_by_url(url)
            self.custom_model_res = self.custom_model.predict_by_url(url)

    def set_url(self, url):
        self.url = url
        self.color_res = self.color_model.predict_by_url(url)
        self.general_res = self.general_model.predict_by_url(url)
        self.custom_model_res = self.custom_model.predict_by_url(url)

    def set_image_id(self, image_id):
        url = f'https://drive.google.com/thumbnail?id={image_id}&sz=w400-h300-p-k-nu'
        self.set_url(url)

    def print_all(self, custom_only=False):
        if not self.url:
            raise ValueError('Image url needs to be set')
        if not custom_only:
            print(f'General: {get_concepts(self.general_res, as_string=True)}')
            print(f'Colors: {get_concepts(self.color_res, as_string=True, is_colors=True)}')
        print(f'Custom-general: {get_concepts(self.custom_model_res, as_string=True)}')

    def get_concepts(self, custom_only=False):
        custom_model_res = self.custom_model.predict_by_url(self.url)
        if custom_only:
            concept_list = get_names(get_concepts(custom_model_res))
        else:
            general_res = self.general_model.predict_by_url(self.url)
            concept_list = safe_combine(get_names(get_concepts(general_res)), get_names(get_concepts(custom_model_res)))
        concept_list.sort()
        return f'Concepts: {concept_list}'

    def get_colors(self):
        color_res = self.color_model.predict_by_url(self.url)
        color_list = get_colors(get_concepts(color_res, is_colors=True))
        color_list.sort()
        return f'Colors name: {color_list}'

    def get_colors_hex(self):
        color_res = self.color_model.predict_by_url(self.url)
        color_list = get_colors_hex(get_concepts(color_res, is_colors=True))
        color_list.sort()
        return f'Colors hex: {color_list}'
