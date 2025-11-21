import requests
from leegunwoo import *


def get_spot_detail(lang, contentId):
    params = get_params(contentId=contentId)

    try:
        response = requests.get(f"http://apis.data.go.kr/B551011/{lang}Service2/detailCommon2", params=params)

        if response.status_code == 200:
            data = response.json()
            items = data.get('response', {}).get('body', {}).get('items', {})
            items = items.get('item', []) if items != '' else []
            return items[0]["overview"] if len(items) > 0 else ""
        else:
            print(f"API 요청 실패: 상태 코드 {response.status_code}")
            return None
            
    except Exception as e:
        print(f"오류 발생: {e}")
        print(data, end="\n")


# 테스트
print(get_spot_detail("Jpn", "3085375"))