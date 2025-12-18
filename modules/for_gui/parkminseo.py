import tkinter as tk
import tkinter.font as tkfont


# 관광지 목록 컨테이너
class ContentsContainer(tk.Frame):
    def __init__(self, master, search_command):
        super().__init__(
            master,
            bg='white',
            width=1220,
            height=600,
            relief='solid',
            borderwidth=2
        )
        self.__create_search(search_command)
        self.__create_contents()

    def __create_search(self, command):
        self.search_frame = tk.Frame(self, width=1180, height=50, relief='solid', borderwidth=2)
        self.search_frame.place(relx=0.5, y=20, anchor='n')

        self.search_label = tk.Label(self.search_frame)
        self.search_label.place(x=0, rely=0.5, anchor='w')

        self.search_entry = tk.Entry(
            self.search_frame,
            width=59,
            font=tkfont.Font(size=20, family="맑은 고딕")
        )
        self.search_entry.place(x=167, rely=0.5, anchor='w')

        self.search_button = tk.Button(
            self.search_frame,
            width=10,
            font=tkfont.Font(size=13, family="맑은 고딕"),
            command=command
        )
        self.search_button.place(x=1063, rely=0.5, anchor='w')

    def __create_contents(self):
        self.contents_frame = tk.Frame(self, width=1180, height=490, bg='white')
        self.contents_frame.place(relx=0.5, y=90, anchor='n')