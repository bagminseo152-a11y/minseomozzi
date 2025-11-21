from sonjiho import *
from leegunwoo import *

for lang in langs:
    print(f"{lang} 시작")
    
    area_codes = [item['code'] for item in get_items(lang, "areaCode2", get_params(numOfRows='50'))]
    all_spots = {}

    cats_codes = [[], [], []]

    for area_code in area_codes:
        counted_unfiltered_area_len = 0
        page_no = 1
        total_count = get_data_total_count(lang, "areaBasedList2", get_params(areaCode=area_code, numOfRows='50'))

        while True:
            data = get_items(lang, "areaBasedList2", get_params(areaCode=area_code, numOfRows='50', pageNo=str(page_no)))

            if data is None:
                continue

            unfiltered_data_len = len(data)
            
            data = [item for item in data if (item["cat1"] in ["A01", "A02", "A03"])]

            for item in data:
                for i in range(len(cats_codes)):
                    if item[f"cat{i+1}"] not in cats_codes[i]:
                        cats_codes[i].append(item[f"cat{i+1}"])

                all_spots[item["contentid"]] = {
                    "title": item["title"],
                    "addr": item["addr1"],
                    "img_url": item["firstimage2"],
                    "theme_code": {
                        "cat1": item["cat1"],
                        "cat2": item["cat2"],
                        "cat3": item["cat3"],
                    },
                    "area_code": item["areacode"]
                }

            counted_unfiltered_area_len += unfiltered_data_len

            if counted_unfiltered_area_len >= total_count:
                print(f"{area_code}번 지역 완료")
                break
            
            page_no += 1

            print(f"{area_code}번 지역: {round((counted_unfiltered_area_len/total_count)*100, 2)}% 완료")
    
    write_file_from_json(all_spots, f"spots/spots_{lang}.json")