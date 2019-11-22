from utils import *
import json


class GenerateTagsJson:

    def __init__(self, general_model, color_model, custom_model, url=None, image_id=None):
        self.color_model = color_model
        self.general_model = general_model
        self.custom_model = custom_model
        if url or image_id:
            if image_id:
                url = f'https://drive.google.com/thumbnail?id={image_id}&sz=w400-h300-p-k-nu'
            self.set_url(url)

    def set_url(self, url):
        self.url = url
        self.color_res = self.color_model.predict_by_url(url)
        self.general_res = self.general_model.predict_by_url(url)
        self.custom_model_res = self.custom_model.predict_by_url(url)

    def set_image_id(self, image_id):
        url = f'https://drive.google.com/thumbnail?id={image_id}&sz=w400-h300-p-k-nu'
        self.set_url(url)

    def get(self):
        tags_json = {}
        keywords = {}
        colors = {}
        keywords['custom'] = self.get_keywords(custom_only=True)
        keywords['all'] = self.get_keywords()
        colors['names'] = self.get_color_names()
        colors['hex'] = self.get_color_hex()
        tags_json['keywords'] = keywords
        tags_json['colors'] = colors
        return json.dumps({'tags': tags_json}, indent=4, sort_keys=False)

    def get_keywords(self, custom_only=False):
        custom_model_res = self.custom_model.predict_by_url(self.url)
        if custom_only:
            concept_list = get_names(get_concepts(custom_model_res))
        else:
            general_res = self.general_model.predict_by_url(self.url)
            concept_list = safe_combine(get_names(get_concepts(general_res)), get_names(get_concepts(custom_model_res)))
        concept_list.sort()
        return concept_list

    def get_color_names(self):
        color_res = self.color_model.predict_by_url(self.url)
        color_list = get_colors(get_concepts(color_res, is_colors=True))
        color_list.sort()
        return color_list

    def get_color_hex(self):
        color_res = self.color_model.predict_by_url(self.url)
        hex_list = get_colors_hex(get_concepts(color_res, is_colors=True))
        hex_list.sort()
        return hex_list
