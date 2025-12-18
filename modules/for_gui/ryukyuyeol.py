import tkinter as tk
import tkinter.font as tkfont


# 프로그램 타이틀 라벨
class ProgramTitleLabel(tk.Label):
    def __init__(self, master):
        super().__init__(master, height=1)


# 관광지 목록 인덱스 전환 버튼
class IndexChangingButtons(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width=200, height=50)

        self.prev = tk.Button(self, text="◀", width=4, font=tkfont.Font(size=16))
        self.prev.place(relx=0.2, rely=0.5, anchor='center')

        self.label = tk.Label(self, width=3, font=tkfont.Font(size=14))
        self.label.place(relx=0.5, rely=0.5, anchor='center')

        self.next = tk.Button(self, text="▶", width=4, font=tkfont.Font(size=16))
        self.next.place(relx=0.8, rely=0.5, anchor='center')