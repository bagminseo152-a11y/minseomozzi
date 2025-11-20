from tkinter import *

def create_search_area(win):
    """
    관광지명 검색란(Entry)과 검색 버튼을 생성하고 배치합니다. 
    (사용자님 담당 부분)
    """
    
    # 1. 검색 영역을 담을 메인 프레임 생성
    # win 창 전체를 채우지 않고, 가운데에 적절한 여백을 두고 배치합니다.
    search_frame = Frame(win)
    search_frame.pack(pady=30, padx=20, fill="x") 
    
    # 2. 레이블 생성 (관광지명 검색 안내)
    Label(
        search_frame,
        text="📍 관광지명 검색:",
        font=("HY견고고딕", 12) 
    ).pack(side=LEFT, padx=(0, 10))
    
    # 3. Entry 위젯 (검색 입력란) 생성
    search_entry = Entry(
        search_frame,
        font=("맑은 고딕", 12),
        width=50, 
        bd=2,     
        relief="groove"
    )
    # 남은 공간을 입력란이 채우도록 설정 (expand=True, fill="x")
    search_entry.pack(side=LEFT, padx=5, expand=True, fill="x")
    
    # 4. 검색 함수 정의
    def perform_search():
        """검색 버튼 클릭 시 실행될 임시 함수"""
        query = search_entry.get()
        # 검색어가 콘솔(터미널)에 출력됩니다.
        print(f"검색 실행됨 - 입력된 검색어: {query}")
        
    # 5. 검색 버튼 생성
    search_button = Button(
        search_frame,
        text="검색 🔍",
        command=perform_search,
        font=("HY견고딕", 11),
        bg="#ff9a85",
        fg="white",
        relief="raised",
        padx=10,
        pady=5
    )
    search_button.pack(side=LEFT, padx=(10, 0))
    
    return search_entry

# ----------------------------------------------------------------------

# ===================== 단독 실행부 =====================
# 이 부분이 메인 실행 코드로, 언어 버튼 코드를 호출하지 않습니다.

if __name__ == "__main__":
    # 1. 메인 창 (Tk) 생성
    win = Tk()
    win.title("Search Area Test - My Part")
    win.geometry("1500x900") # 테스트하기 좋은 크기로 설정

    # 2. 사용자님이 만든 검색 영역만 호출
    search_entry_widget = create_search_area(win) 

    # 3. 이벤트 루프 시작 (GUI 창 표시)
    win.mainloop()