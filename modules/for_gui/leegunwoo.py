import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk


# 관광지 지역, 분류 필터 컨테이너
class FilteringContainer(tk.Frame):
    def __init__(self, master, command):
        super().__init__(
            master,
            bg='white',
            width=1220,
            height=70,
            relief='solid',
            borderwidth=2
        )
        self.command = command
        self.__setup_style()
        self.__create_widgets()

    def __setup_style(self):
        ttk.Style().configure('TCombobox', padding=(1, 8, 1, 8))

    def __create_widgets(self):
        self.area_combo = ttk.Combobox(self, width=22, font=tkfont.Font(size=14), justify='center')
        self.area_combo.place(relx=0.12, rely=0.5, anchor='center')
        self.area_combo.bind("<<ComboboxSelected>>",
            lambda e: self.command(e, 'area')
        )

        self.category_combos = []
        for i in range(3):
            combo = ttk.Combobox(self, width=33, font=tkfont.Font(size=13), justify='center')
            combo.place(relx=0.38 + 0.24 * i, rely=0.5, anchor='center')
            combo.bind("<<ComboboxSelected>>",
                lambda e, idx=i: self.command(e, f'cat{idx+1}')
            )
            self.category_combos.append(combo)