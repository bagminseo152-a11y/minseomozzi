import numpy as np
import cv2
import requests
from PIL import Image, ImageTk
import os
import sys
import json 

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_json_from_file(dir):
    sys_dir = resource_path(f"DB/{dir}")

    with open(sys_dir, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_image_from_url(url, size):
    if url == "":
        return None
    
    try:
        res = requests.get(url)

        if res.status_code == 200:
            arr = np.asarray(bytearray(res.content), np.uint8)
            img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
            img = cv2.resize(img, size)

            return ImageTk.PhotoImage(Image.fromarray(img[:,:,::-1]))
        else:
            print(f"API 요청 실패: 상태 코드 {res.status_code}")
            return None
        
    except Exception as e:
        print(f"오류 발생: {e}")
        return None


