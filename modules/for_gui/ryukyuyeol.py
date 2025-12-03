import tkinter as tk
from tkinter import ttk
import math

# ==========================================================
# Mock Data (페이지네이션 테스트를 위해 충분한 데이터가 필요합니다.)
# ==========================================================
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
    {"name": "N서울타워", "desc": "남산에 위치한 상징적인 타워입니다.", "rating": "⭐️⭐️⭐️⭐️⭐️"}, # 12번째 데이터 추가
    {"name": "잠실", "desc": "복합 쇼핑몰과 엔터테인먼트 구역입니다.", "rating": "⭐️⭐️⭐️"}, # 다음 페이지 데이터
    {"name": "이태원", "desc": "다양한 문화가 공존하는 지역입니다.", "rating": "⭐️⭐️⭐️⭐️"}, # 다음 페이지 데이터
]


class CardApp:
    def __init__(self, master, data_list, max_cols=4, cards_per_page=12): # 👈 max_cols=4, cards_per_page=12 로 변경
        self.master = master
        self.data_list = data_list
        self.max_cols = max_cols
        
        self.cards_per_page = cards_per_page
        self.total_pages = math.ceil(len(self.data_list) / self.cards_per_page)
        self.current_page = 0
        
        # 1. 카드 목록을 담을 컨테이너 프레임
        self.card_container = ttk.Frame(master, padding="10")
        self.card_container.pack(fill="both", expand=True)

        # 2. 페이지 버튼을 담을 프레임 (중앙 정렬을 위해 grid 사용)
        self.button_frame = ttk.Frame(master, padding="5")
        self.button_frame.pack(fill="x")
        
        # 3. 버튼 및 레이블 생성 및 배치 (중앙 정렬 로직)
        
        # button_frame을 3개의 컬럼으로 나누고 중앙 컬럼만 확장되도록 설정
        self.button_frame.grid_columnconfigure(0, weight=1)  # 왼쪽 빈 공간 확장
        self.button_frame.grid_columnconfigure(1, weight=0)  # 중앙 그룹은 확장 X
        self.button_frame.grid_columnconfigure(2, weight=1)  # 오른쪽 빈 공간 확장
        
        # 중앙 그룹을 담을 내부 프레임
        center_group = ttk.Frame(self.button_frame)
        center_group.grid(row=0, column=1, sticky="n") # button_frame의 중앙 컬럼에 배치

        # 버튼들을 center_group 내에 배치
        self.prev_button = ttk.Button(center_group, text="◀ 이전", command=self.prev_page)
        self.prev_button.pack(side="left", padx=5)
        
        self.page_label = ttk.Label(center_group, text="페이지 정보")
        self.page_label.pack(side="left", padx=10)
        
        self.next_button = ttk.Button(center_group, text="다음 ▶", command=self.next_page)
        self.next_button.pack(side="left", padx=5)
        
        # 초기 카드 그리기
        self.draw_cards()
        
    def draw_cards(self):
        """현재 페이지의 카드들만 화면에 그립니다."""
        
        for widget in self.card_container.winfo_children():
            widget.destroy()

        start_index = self.current_page * self.cards_per_page
        end_index = start_index + self.cards_per_page
        
        current_page_data = self.data_list[start_index:end_index]
        
        # ----------------------------------------------------
        # 카드를 그리는 반복문 (4x3 레이아웃)
        # ----------------------------------------------------
        for index, data in enumerate(current_page_data):
            # 4열 배치를 위한 행/열 계산
            row_num = index // self.max_cols  # 0~3은 0행, 4~7은 1행, 8~11은 2행
            col_num = index % self.max_cols  # 0, 1, 2, 3, 0, 1, 2, 3...
            
            # 개별 카드 프레임 생성
            card_frame = ttk.Frame(self.card_container, padding="10", relief="groove", borderwidth=2)
            card_frame.grid(row=row_num, column=col_num, padx=5, pady=5, sticky="nsew") 
            
            # 카드 내부 위젯
            name_label = ttk.Label(card_frame, text=data["name"], font=("나눔고딕", 12, "bold"))
            name_label.pack(pady=(0, 5))
            
            desc_label = ttk.Label(card_frame, text=data["desc"], wraplength=100) # wraplength 조정
            desc_label.pack()
            
            rating_label = ttk.Label(card_frame, text=data["rating"], foreground="orange")
            rating_label.pack(pady=(5, 0))

        # 카드 영역의 열(column)이 균등하게 확장 가능하도록 설정
        for col in range(self.max_cols):
            self.card_container.grid_columnconfigure(col, weight=1)
            
        self.update_pagination_status()

    def update_pagination_status(self):
        """페이지 레이블 텍스트와 버튼의 활성화/비활성화 상태를 업데이트합니다."""
        
        page_info = f"페이지 {self.current_page + 1} / {self.total_pages}"
        self.page_label.config(text=page_info)
        
        # 이전 버튼 활성화/비활성화
        if self.current_page == 0:
            self.prev_button.config(state=tk.DISABLED)
        else:
            self.prev_button.config(state=tk.NORMAL)
            
        # 다음 버튼 활성화/비활성화
        if self.current_page >= self.total_pages - 1:
            self.next_button.config(state=tk.DISABLED)
        else:
            self.next_button.config(state=tk.NORMAL)

    def next_page(self):
        """다음 페이지로 이동합니다."""
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
            self.draw_cards()

    def prev_page(self):
        """이전 페이지로 이동합니다."""
        if self.current_page > 0:
            self.current_page -= 1
            self.draw_cards()


# ==========================================================
# 5. Tkinter 메인 실행
# ==========================================================
if __name__ == "__main__":
    root = tk.Tk()
    root.title("관광지 추천 카드 목록 (4x3 페이지네이션)")
    
    # 4열, 12개 카드가 한 페이지에 표시되도록 설정합니다.
    app = CardApp(root, TOURISM_DATA_LIST, max_cols=4, cards_per_page=12)
    
    root.mainloop()