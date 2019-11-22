import json


def safe_combine(list1, list2):
    return list(dict.fromkeys(list1 + list2))


def get_names(concepts):
    return list([con['name'].lower() for con in concepts])


def get_colors(colors):
    return list([dict(col['w3c'])['name'] for col in colors])


def get_colors_hex(colors):
    return list([f'https://www.color-hex.com/color/' + dict(col['w3c'])['hex'].split('#')[1] for col in colors])


def filter_concepts(concepts, thres=0.9):
    return list(filter((lambda con: con['value'] >= thres), concepts))


def get_concepts(response, as_string=False, is_colors=False):
    assert response['status']['description'] == 'Ok', f'Failed with status {response["status"]}'
    if is_colors:
        assert response["outputs"][0]["model"]["name"] == 'color', 'The model is not a color model'
    data_type = 'concepts' if not is_colors else 'colors'
    concepts = response["outputs"][0]['data'][data_type]
    concepts = filter_concepts(concepts, thres=0.3) if data_type == 'concepts' else filter_concepts(concepts, thres=0.1)
    return f'Concepts: {json.dumps(concepts, indent=4, sort_keys=False)}' if as_string else concepts
