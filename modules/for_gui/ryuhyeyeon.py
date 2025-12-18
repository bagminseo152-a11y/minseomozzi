import tkinter as tk
import tkinter.font as tkfont
from modules.for_gui.choijiwon import *


# 관광지 카드
class ContentCard(tk.Frame):
    def __init__(self, master, data, content_id, lang, click_command):
        super().__init__(
            master,
            width=289,
            height=158,
            relief='solid',
            borderwidth=2
        )

        self.data = data
        self.content_id = content_id
        self.lang = lang
        self.click_command = click_command

        self.__create_widgets()
        self.__bind_events()

    def __create_widgets(self):
        self.img_label = tk.Label(self)
        self.img_label.place(relx=0.5, rely=0.5, anchor='center')

        img = get_image_from_url(self.data["img_url"], (269,140))
        if img:
            self.img_label.config(image=img)
            self.img_label.image = img
        else:
            self.img_label.config(text="No Image")

        self.title_label = tk.Label(
            self,
            width=38,
            height=2,
            text=self.data["title"],
            font=tkfont.Font(size=9, weight='bold'),
            wraplength=280
        )
        self.title_label.place(relx=0.5, rely=0.88, anchor='center')

    def __bind_events(self):
        for widget in (self, self.img_label, self.title_label):
            widget.bind(
                "<Button-1>",
                lambda e: self.click_command(e, self.lang, self.content_id)
            )