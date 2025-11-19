import tkinter as tk

class MultiTabCategoryViewer:
    def __init__(self, root):
        self.root = root
        root.title("대-중-소분류 연동 시스템 (간격 조정)")
        
        root.geometry("1500x900") 
        root.resizable(True, True) 
        
        # --- 상수 및 데이터 정의 ---
        self.DEFAULT_BG = 'white'      
        self.SELECTED_BG = 'lightgray'    
        self.MAJOR_WIDTH = 80
        self.MEDIUM_WIDTH = 100
        self.MINOR_WIDTH = 60
        
        self.selected_major_panel = None      
        self.selected_medium_panel = None
        
        self.category_data = {
            "지역 분류": {
                "서울/수도권": ["강남", "홍대", "명동"],
                "부산/경남": ["해운대", "남포동", "통영"],
                "제주/강원": ["서귀포", "강릉", "속초"]
            },
            "테마 분류": {
                "힐링/휴식": ["스파", "자연휴양림"],
                "미식/투어": ["맛집투어", "재래시장", "푸드트럭"],
                "역사/문화": ["궁궐", "박물관", "미술관"]
            },
            "예산 분류": {
                "저가": ["게스트하우스", "대중교통 이용"],
                "중가": ["비즈니스호텔", "렌터카"],
                "고가": ["5성급호텔", "프리미엄 택시"]
            }
        }
        
        # --- 메인 컨테이너 프레임 ---
        self.main_container = tk.Frame(root, padx=20, pady=30)
        self.main_container.pack(fill='both', expand=True)

        
        # 탭 패널 생성 및 배치
        self.major_panel = self._create_category_panel(self.main_container, "대분류", self.MAJOR_WIDTH) 
        self.major_panel.pack(side='left', fill='y', padx=(0, 10)) 

        self.medium_panel = self._create_category_panel(self.main_container, "중분류", self.MEDIUM_WIDTH)
        self.minor_panel = self._create_category_panel(self.main_container, "소분류", self.MINOR_WIDTH)
        # 오른쪽 빈 작업 공간
        self.workspace_panel = tk.Frame(self.main_container, bg='white')
        self.workspace_panel.pack(side='right', fill='both', expand=True, padx=(0, 0))
        tk.Label(self.workspace_panel, text="선택된 분류에 따른 최종 정보 표시 영역", fg='gray', font=('Helvetica', 14)).pack(pady=15)

        self.populate_major_categories()


    def _create_category_panel(self, parent, title, width):
       
        panel = tk.Frame(
            parent, 
            bg='#F0F0F0',
            width=width
        )
        panel.pack_propagate(False) 
        
        tk.Label(panel, text=title, font=('Helvetica', 12, 'bold'), bg='#F0F0F0', pady=2).pack(fill='x')
        
        content_frame = tk.Frame(panel, bg='#F0F0F0')
        # 🚨 padx를 0으로 설정하여 탭의 폭을 꽉 채우도록 함 🚨
        content_frame.pack(fill='both', expand=True, padx=0) 
        
        panel.content_frame = content_frame 
        return panel


    def _configure_content_grid(self, content_frame, count):
        """항목 수만큼 행(row)을 구성하고 weight=1을 주어 공간을 균등 분배합니다."""
        for i in range(count + 5): # 넉넉한 범위로 초기화 (현재 항목 수 + 여유분)
             content_frame.grid_rowconfigure(i, weight=0)
        
        for i in range(count):
            content_frame.grid_rowconfigure(i, weight=1)


    def populate_major_categories(self):
        """대분류 탭에 항목을 채우고 그리드 간격을 설정합니다."""
        content_frame = self.major_panel.content_frame
        categories = list(self.category_data.keys())
        
        for i, text in enumerate(categories):
            self._create_clickable_item(
                parent_frame=content_frame, 
                text=text, 
                command=self.on_major_click,
                row=i 
            )
        self._configure_content_grid(content_frame, len(categories))


    def _create_clickable_item(self, parent_frame, text, command, row):
        """클릭 가능한 분류 항목을 생성하고 grid로 배치합니다."""
        
        frame = tk.Frame(parent_frame, bg=self.DEFAULT_BG, relief=tk.RIDGE, borderwidth=1)
        # 🚨 padx와 pady 값을 2로 줄여 간격을 좁게 만듦 🚨
        frame.grid(row=row, column=0, sticky='nsew', padx=2, pady=2) 
        
        label = tk.Label(frame, text=text, bg=self.DEFAULT_BG)
        label.pack(expand=True, fill='both', padx=3, pady=3)
        
        frame.bind('<Button-1>', lambda event, p=frame, name=text: command(p, name))
        label.bind('<Button-1>', lambda event, p=frame, name=text: command(p, name))


    def _create_static_item(self, parent_frame, text, row):
        """클릭 기능 없는 단순 표시 항목을 생성하고 grid로 배치합니다."""
        frame = tk.Frame(parent_frame, bg='#FDFDFD', relief=tk.FLAT, borderwidth=1)
        # 🚨 padx와 pady 값을 2로 줄여 간격을 좁게 만듦 🚨
        frame.grid(row=row, column=0, sticky='nsew', padx=2, pady=2)
        
        label = tk.Label(frame, text=text, bg='#FDFDFD', anchor='w')
        label.pack(expand=True, fill='both', padx=5, pady=5)


    # --- (나머지 클릭 및 클리어 함수) ---

    def _reset_selection(self, current_selection_var):
        panel = current_selection_var
        if panel:
            panel.config(bg=self.DEFAULT_BG)
            for child in panel.winfo_children():
                child.config(bg=self.DEFAULT_BG)

    def _set_selection(self, clicked_panel):
        clicked_panel.config(bg=self.SELECTED_BG)
        for child in clicked_panel.winfo_children():
            child.config(bg=self.SELECTED_BG)

    def _clear_panel(self, panel):
        panel.pack_forget()
        for widget in panel.content_frame.winfo_children():
            widget.destroy()
        self._configure_content_grid(panel.content_frame, 0) # grid weight 초기화


    def on_major_click(self, clicked_panel, major_name):
        self._reset_selection(self.selected_major_panel)
        self._set_selection(clicked_panel)
        self.selected_major_panel = clicked_panel
        
        self._clear_panel(self.medium_panel)
        self._clear_panel(self.minor_panel)
        self.selected_medium_panel = None 
        
        medium_categories = list(self.category_data.get(major_name, {}).keys())
        content_frame = self.medium_panel.content_frame
        
        for i, text in enumerate(medium_categories):
             self._create_clickable_item(
                parent_frame=content_frame, 
                text=text, 
                command=lambda p, name: self.on_medium_click(p, major_name, name),
                row=i
            )
        self._configure_content_grid(content_frame, len(medium_categories))
        self.medium_panel.pack(side='left', fill='y', padx=(0, 15))
        self._update_workspace(f"대분류 '{major_name}' 선택됨. 중분류를 선택해주세요.")


    def on_medium_click(self, clicked_panel, major_name, medium_name):
        self._reset_selection(self.selected_medium_panel)
        self._set_selection(clicked_panel)
        self.selected_medium_panel = clicked_panel
        
        self._clear_panel(self.minor_panel)
        
        minor_categories = self.category_data.get(major_name, {}).get(medium_name, [])
        content_frame = self.minor_panel.content_frame
        
        for i, text in enumerate(minor_categories):
             self._create_static_item(content_frame, text, row=i) 
             
        self._configure_content_grid(content_frame, len(minor_categories))
        self.minor_panel.pack(side='left', fill='y', padx=(0, 15))
        
        self._update_workspace(f"선택 완료: {major_name} > {medium_name}\n\n최종 항목:\n{', '.join(minor_categories)}")

    def _update_workspace(self, text):
        self._clear_workspace()
        tk.Label(self.workspace_panel, text=text, fg='blue', font=('Helvetica', 14)).pack(pady=50)

    def _clear_workspace(self):
        for widget in self.workspace_panel.winfo_children():
            widget.destroy()


# --- 프로그램 실행 ---
if __name__ == "__main__":
    root = tk.Tk()
    app = MultiTabCategoryViewer(root)
    root.mainloop()
