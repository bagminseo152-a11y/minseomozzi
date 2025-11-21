from sonjiho import *
from leegunwoo import *


def get_theme_name(lang, cat):
    page_no = 1

    while True:
        params = get_params(numOfRows='50', pageNo=str(page_no))
        cat_params = {}

        if len(cat) >= 5:
            cat_params["cat1"] = cat[:3]
        if len(cat) >= 9:
            cat_params["cat2"] = cat[:5]

        params.update(cat_params)


        items = get_items(lang, "categoryCode2", params)
        filtered_items = [item for item in items if item["code"] == cat]

        if len(filtered_items) == 0:
            page_no += 1
        else:
            return filtered_items[0]["name"]