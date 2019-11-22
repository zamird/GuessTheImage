from clarifai.rest import ClarifaiApp
from print import Print as Ptr
from generate_tags_json import GenerateTagsJson as TagsJsn

app = ClarifaiApp(api_key='57c6104fb12f460db9674c3c86968020')
general_model = app.public_models.general_model
color_model = app.public_models.color_model
custom_model = app.models.get('object-recognition-model')
printer = Ptr(general_model, color_model, custom_model)
tags_json = TagsJsn(general_model, color_model, custom_model)


def guess_the_image_content(image_id):
    # image_id = '1eEqfdJyxXLIu1ApTEIFR10H5rv6Z1Guh'
    printer.set_image_id(image_id)
    tags_json.set_image_id(image_id)
    concepts = printer.get_concepts(custom_only=True)
    colors_hex = printer.get_colors_hex()
    return {'concepts': concepts, 'colors_hex': colors_hex}





