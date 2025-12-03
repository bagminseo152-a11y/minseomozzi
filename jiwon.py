import tkinter as tk
from tkinter import ttk
import math

TOURISM_DATA_LIST = [
    {"name": "경복궁", "desc": "조선 시대의 법궁입니다.", "rating": "⭐️⭐️⭐️⭐️"},
    {"name": "남산타워", "desc": "서울의 아름다운 야경을 볼 수 있습니다.", "rating": "⭐️⭐️⭐️⭐️⭐️"},
    {"name": "북촌 한옥마을", "desc": "전통 한옥이 밀집된 곳입니다.", "rating": "⭐️⭐️⭐️"},
    {"name": "롯데월드", "desc": "실내외 테마파크가 있는 곳입니다.", "rating": "⭐️⭐️⭐️⭐️"},
    {"name": "DDP", "desc": "독특한 디자인의 복합 문화 공간입니다.", "rating": "⭐️⭐️⭐️"},
    {"name": "창덕궁", "desc": "아름다운 후원이 유명한 궁궐입니다.", "rating": "⭐️⭐️⭐️⭐️"},
    {"name": "코엑스", "desc": "무역과 전시를 위한 대형 공간입니다.", "rating": "⭐️⭐️⭐️"},
    {"name": "인사동", "desc": "전통 공예품과 찻집이 많은 거리입니다.", "rating": "⭐️⭐️⭐️⭐️"},
    {"name": "광화문", "desc": "대한민국의 상징적인 문입니다.", "rating": "⭐️⭐️⭐️⭐️"},
    {"name": "홍대 거리", "desc": "젊음과 예술의 거리입니다.", "rating": "⭐️⭐️⭐️⭐️"},
    {"name": "여의도 한강공원", "desc": "도심 속 휴식 공간입니다.", "rating": "⭐️⭐️⭐️"},
    {"name": "N서울타워", "desc": "남산에 위치한 상징적인 타워입니다.", "rating": "⭐️⭐️⭐️⭐️⭐️"},
    {"name": "잠실", "desc": "복합 쇼핑몰과 엔터테인먼트 구역입니다.", "rating": "⭐️⭐️⭐️"},
    {"name": "이태원", "desc": "다양한 문화가 공존하는 지역입니다.", "rating": "⭐️⭐️⭐️⭐️"},
]

class CardApp:
    def __init__(self, master, data_list, max_cols=4, cards_per_page=12):
        self.master = master
        self.data_list = data_list
        self.max_cols = max_cols
        self.cards_per_page = cards_per_page
        self.total_pages = math.ceil(len(data_list) / cards_per_page)
        self.current_page = 0

        # 카드 고정 크기
        self.CARD_WIDTH = 180
        self.CARD_HEIGHT = 150

        # 카드 컨테이너
        self.card_container = ttk.Frame(master)
        self.card_container.pack(fill="both", expand=True)

        # 버튼 영역
        self.button_frame = ttk.Frame(master)
        self.button_frame.pack(fill="x")
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=0)
        self.button_frame.grid_columnconfigure(2, weight=1)

        center = ttk.Frame(self.button_frame)
        center.grid(row=0, column=1)

        self.prev_button = ttk.Button(center, text="◀ 이전", command=self.prev_page, width=8)
        self.prev_button.pack(side="left", padx=5)
        self.page_label = ttk.Label(center, text="")
        self.page_label.pack(side="left", padx=10)
        self.next_button = ttk.Button(center, text="다음 ▶", command=self.next_page, width=8)
        self.next_button.pack(side="left", padx=5)

        self.draw_cards()

        # 창 크기 고정
        master.update_idletasks()
        width = master.winfo_width()
        height = master.winfo_height()
        master.geometry(f"{width}x{height}")
        master.minsize(width, height)

    def draw_cards(self):
        # 기존 카드 삭제
        for w in self.card_container.winfo_children():
            w.destroy()

        start = self.current_page * self.cards_per_page
        end = start + self.cards_per_page
        page_data = self.data_list[start:end]

        rows_per_page = math.ceil(self.cards_per_page / self.max_cols)
        total_cells = rows_per_page * self.max_cols

        for i in range(total_cells):
            row = i // self.max_cols
            col = i % self.max_cols

            frame = ttk.Frame(
                self.card_container,
                width=self.CARD_WIDTH,
                height=self.CARD_HEIGHT,
                relief="groove" if i < len(page_data) else "flat",
                borderwidth=2 if i < len(page_data) else 0
            )
            frame.grid(row=row, column=col, padx=5, pady=5)
            frame.grid_propagate(False)  # 크기 절대 고정

            if i < len(page_data):
                data = page_data[i]
                # 내부 글씨 중앙 정렬
                container = ttk.Frame(frame)
                container.place(relx=0.5, rely=0.5, anchor="center")
                ttk.Label(container, text=data["name"], font=("나눔고딕", 12, "bold")).pack()
                ttk.Label(container, text=data["desc"], wraplength=self.CARD_WIDTH-10, justify="center").pack(pady=4)
                ttk.Label(container, text=data["rating"], foreground="orange").pack()

        for c in range(self.max_cols):
            self.card_container.grid_columnconfigure(c, weight=1, minsize=self.CARD_WIDTH)
        for r in range(rows_per_page):
            self.card_container.grid_rowconfigure(r, minsize=self.CARD_HEIGHT)

        self.update_status()

    def update_status(self):
        self.page_label.config(text=f"페이지 {self.current_page + 1} / {self.total_pages}")
        self.prev_button.config(state="normal" if self.current_page > 0 else "disabled")
        self.next_button.config(state="normal" if self.current_page < self.total_pages - 1 else "disabled")

    def next_page(self):
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
            self.draw_cards()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.draw_cards()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("관광지 추천 카드 목록")
    app = CardApp(root, TOURISM_DATA_LIST)
    root.mainloop()


