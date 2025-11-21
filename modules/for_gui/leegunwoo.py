from tkinter import *

def create_language_buttons(master, command):
    selected_button = {"btn": None}

    def select_button(btn):
        if selected_button["btn"] and selected_button["btn"] != btn:
            selected_button["btn"].config(bg="#d7c8ff", relief="flat")

        btn.config(relief="sunken", bg="#a7c7e7")
        selected_button["btn"] = btn

    # ✔ Hover 이벤트
    def on_enter(e, btn):
        if selected_button["btn"] != btn:     # 선택된 버튼은 색 유지
            btn.config(bg="#b7e4c7")

    def on_leave(e, btn):
        if selected_button["btn"] != btn:     # 선택된 버튼만 제외
            btn.config(bg="#d7c8ff")

    texts = [
        "한국어", "영어", "일본어", "중국어(간체)", "중국어(번체)",
        "프랑스어", "독일어", "스페인어", "러시아어"
    ]

    frame = Frame(master, bg="#f0f0f0")
    frame.pack(side=TOP, anchor="ne", padx=20, pady=20)

    buttons = []
    for t in texts:
        btn = Button(
            frame,
            text=t,
            font="HY견고딕 9",
            bg="#d7c8ff",
            relief="flat",
            width=12,
            height=2,
            padx=4,
            pady=4,
            command=command
        )

        btn.config(command=lambda b=btn: select_button(b))

        btn.bind("<Enter>", lambda e, b=btn: on_enter(e, b))
        btn.bind("<Leave>", lambda e, b=btn: on_leave(e, b))

        btn.pack(side=LEFT, padx=5)
        buttons.append(btn)