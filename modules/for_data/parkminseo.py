from sonjiho import *
from ryuhyeyeon import *

f_json = get_json_from_file(f'spots/spots_{langs[0]}.json')

cats_codes = [set(), set(), set()]
for code in f_json:
    for i in range(3):
        cats_codes[i].add(f_json[code]["theme_code"][f"cat{i+1}"])
cats_codes = [list(cat_codes) for cat_codes in cats_codes]

for i in range(3):
    cats_codes[i].sort()

themes = {
    "cat1": {},
    "cat2": {},
    "cat3": {}
}

for i in range(3):
    for idx, code in enumerate(cats_codes[i]):
        themes[f"cat{i+1}"][code] = {}

        for lang in langs:
            themes[f"cat{i+1}"][code][lang] = get_theme_name(lang, code)

        print(f"{code} 완료")

write_file_from_json(themes, 'code_info/theme.json')