from tkinter import *

def create_language_buttons(win):
    """
    오른쪽 상단에 언어 선택 버튼들을 생성하고 배치합니다.
    """
    selected_button = {"btn": None}

    def select_button(btn):
        """버튼 클릭 시 색상 및 릴리프 변경"""
        if selected_button["btn"] and selected_button["btn"] != btn:
            # 이전에 선택된 버튼의 스타일을 초기화
            selected_button["btn"].config(bg="#d7c8ff", relief="flat")

        # 새로 선택된 버튼의 스타일 적용
        btn.config(relief="sunken", bg="#b7e4c7")
        selected_button["btn"] = btn

    texts = [
        "한국어", "영어", "일본어", "중국어(간체)", "중국어(번체)",
        "프랑스어", "독일어", "스페인어", "러시아어"
    ]

    # ✔ 오른쪽 상단 Frame
    frame = Frame(win, bg="#f0f0f0")
    frame.pack(side=TOP, anchor="ne", padx=20, pady=20)

    buttons = []
    for t in texts:
        btn = Button(
            frame,
            text=t,
            # 안전한 글꼴 지정을 위해 튜플 사용
            font=("HY견고딕", 9),
            bg="#d7c8ff",
            relief="flat",
            width=12,
            height=2,
            padx=4,
            pady=4
        )

        btn.config(command=lambda b=btn: select_button(b))
        btn.pack(side=LEFT, padx=5)

        buttons.append(btn)

    return buttons



def create_search_area(win):
    """
    관광지명 검색란(Entry)과 검색 버튼을 생성하고 배치합니다.
    """
    
    # 검색 영역을 담을 메인 프레임 생성 (언어 버튼 아래에 위치)
    search_frame = Frame(win)
    # padx로 좌우 여백, fill="x"로 창 너비에 맞게 확장, pady로 상하 간격
    search_frame.pack(pady=10, padx=20, fill="x")
    
    # 1. 레이블 생성
    Label(
        search_frame,
        text="📍 관광지명 검색:",
        # 오류 해결을 위해 폰트 튜플 사용
        font=("HY견고고딕", 12) 
    ).pack(side=LEFT, padx=(0, 10))
    
    # 2. Entry 위젯 (검색 입력란) 생성 및 배치
    search_entry = Entry(
        search_frame,
        # 오류 해결을 위해 폰트 튜플 사용
        font=("맑은 고딕", 12),
        width=50, 
        bd=2,     
        relief="groove"
    )
    # 입력란이 남은 공간을 채우도록 expand=True, fill="x" 설정
    search_entry.pack(side=LEFT, padx=5, expand=True, fill="x")
    
    # 3. 검색 함수 정의
    def perform_search():
        """검색 버튼 클릭 시 실행될 임시 함수"""
        query = search_entry.get()
        print(f"검색 실행됨 - 입력된 검색어: {query}")
        # 실제 검색 로직(예: API 호출, 리스트 필터링 등)은 여기에 추가하시면 됩니다.
        
    # 4. 검색 버튼 생성
    search_button = Button(
        search_frame,
        text="검색 🔍",
        command=perform_search,
        # 안전한 글꼴 지정을 위해 튜플 사용
        font=("HY견고딕", 11),
        bg="#ff9a85",
        fg="white",
        relief="raised",
        padx=10,
        pady=5
    )
    search_button.pack(side=LEFT, padx=(10, 0))
    
    return search_entry # 검색어를 가져올 때 유용하도록 Entry 위젯 반환



# ===================== 실행부 =====================

# 1. 메인 창 (Tk) 생성
win = Tk()
win.title("Language Buttons and Search Interface")
win.geometry("1500x900")   # 전체 창 크기

# 2. 언어 버튼 생성 및 배치
create_language_buttons(win)

# 3. 검색 영역 생성 및 배치
search_entry_widget = create_search_area(win) 

# 4. 이벤트 루프 시작
win.mainloop()