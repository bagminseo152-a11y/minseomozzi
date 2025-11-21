from sonjiho import *
from leegunwoo import *

area_info = {}

params = get_params(numOfRows='50')

for lang in langs:
    areas = get_items(lang, "areaCode2", params)

    for area in areas:
        if area["code"] not in area_info:
            area_info[area["code"]] = {
                lang: area["name"]
            }
        else:
            area_info[area["code"]][lang] = area["name"]

write_file_from_json(area_info, 'code_info/area.json')