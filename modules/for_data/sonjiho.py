import requests

service_key = "4ac31ff38e6643243c894f2f02466b9cc2fb6d0f9068bcba197b29cc9b44575f"
base_req_url = "http://apis.data.go.kr/B551011"

langs = ["Kor", "Eng", "Jpn", "Chs", "Cht", "Fre", "Ger", "Spn", "Rus"]


def get_items(lang, end_point, params):
    try:
        response = requests.get(f"{base_req_url}/{lang}Service2/{end_point}", params=params)

        if response.status_code == 200:
            data = response.json()
            items = data.get('response', {}).get('body', {}).get('items', {})
            items = items.get('item', []) if items != '' else []
            return items
        else:
            print(f"API 요청 실패: 상태 코드 {response.status_code}")
            
    except Exception as e:
        print(f"오류 발생1: {e}")
        print(data, end="\n")


def get_data_total_count(lang, end_point, params):
    try:
        response = requests.get(f"{base_req_url}/{lang}Service2/{end_point}", params=params)

        if response.status_code == 200:
            data = response.json()
            count = data.get('response', {}).get('body', {}).get('totalCount', 0)
            return int(count)
        else:
            print(f"API 요청 실패: 상태 코드 {response.status_code}")
            
    except Exception as e:
        print(f"오류 발생2: {e}")