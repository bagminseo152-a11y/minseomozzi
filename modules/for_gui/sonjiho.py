import tkinter as tk
import tkinter.font as tkfont
from modules.for_gui.choijiwon import *
from modules.for_data.choijiwon import *


# 관광지 상세정보 창
class ContentDetail(tk.Toplevel):
    def __init__(self, root, lang, cid):
        w, h = 1200, 300
        l = round((root.winfo_screenwidth()-w)/2) - 10
        t = round((root.winfo_screenheight()-h)/2) - 50

        self.lang = lang
        self.cid = cid
        self.data = get_json_from_file(f"spots/spots_{lang}.json")[cid]

        super().__init__(root)
        self.geometry(f"{w}x{h}+{l}+{t}")
        self.title(self.data["title"])

        self.__create_img_part()
        self.__create_info_part()

        self.grab_set() 
        self.transient(root)

    def __create_img_part(self):
        self.img_frame = tk.Frame(self, width=500, height=300)
        self.img_frame.place(x=0, y=0)

        self.img_label = tk.Label(self.img_frame)
        self.img_label.place(relx=0.5, rely=0.5, anchor='center')

        img = get_image_from_url(self.data["img_url"], (480, 280))
        if img:
            self.img_label.config(image=img)
            self.img_label.image = img
        else:
            self.img_label.config(text="No Image")

    def __create_info_part(self):
        self.info_frame = tk.Frame(self, width=700, height=300)
        self.info_frame.place(x=500, y=0)

        self.title_label = tk.Label(
            self.info_frame,
            font=tkfont.Font(size=15, weight='bold'),
            text=self.data["title"]
        )
        self.title_label.place(relx=0.5, y=20, anchor='n')
        
        self.addr_label = tk.Label(
            self.info_frame,
            font=tkfont.Font(size=11),
            text=f"{get_json_from_file("langs.json")[self.lang]["address"]}: {self.data["addr"]}"
        )
        self.addr_label.place(relx=0.5, y=60, anchor='n')

        self.detail_label = tk.Label(
            self.info_frame,
            width=95,
            height=11,
            font=tkfont.Font(size=10, family="맑은 고딕"),
            text=get_spot_detail(self.lang, self.cid),
            wraplength=660,
            relief='solid',
            borderwidth=1
        )
        self.detail_label.place(relx=0.5, rely=0.62, anchor='center')


def display_content_detail(e, root, lang, content_id):
    ContentDetail(root, lang, content_id)

