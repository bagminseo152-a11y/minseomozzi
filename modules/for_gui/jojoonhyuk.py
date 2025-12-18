import tkinter as tk
import tkinter.font as tkfont
from modules.for_gui.choijiwon import *


# 언어 선택란
class LanguageSelection(tk.Frame):
    def __init__(self, master, command):
        super().__init__(
            master,
            bg='white',
            width=860,
            height=55,
            relief='solid',
            borderwidth=2
        )
        self.buttons = {}
        self.command = command
        self.__create_buttons()

    def __create_buttons(self):
        langs = get_json_from_file("langs.json")
        for i, (code, data) in enumerate(langs.items()):
            bt = tk.Button(
                self,
                name=code.lower(),
                bg="#989898",
                width=10,
                height=2,
                text=data["lang_name"],
                command=lambda c=code: self.command(c)
            )
            bt.place(relx=(0.005 + i / 9.05), rely=0.5, anchor='w')
            self.buttons[code] = bt

    def highlight(self, lang):
        for code, bt in self.buttons.items():
            if code == lang:
                bt.config(fg='black', font=tkfont.Font(size=10, weight='bold'))
            else:
                bt.config(fg='white', font=tkfont.Font(size=11))