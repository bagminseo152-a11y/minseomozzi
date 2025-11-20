from tkinter import *

def create_language_buttons(win):
    selected_button = {"btn": None}

    def select_button(btn):
        if selected_button["btn"] and selected_button["btn"] != btn:
            selected_button["btn"].config(bg="#d7c8ff", relief="flat")

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
            font="HY견고딕 9",
            bg="#d7c8ff",
            relief="flat",

            # ✔ 버튼 크기 조절
            width=12,
            height=2,

            # ✔ 버튼 내부 여백
            padx=4,
            pady=4
        )

        btn.config(command=lambda b=btn: select_button(b))

        # ✔ 버튼 간격 조절
        btn.pack(side=LEFT, padx=5)

        buttons.append(btn)

    return buttons



# ===================== 실행부 =====================

win = Tk()
win.title("Language Buttons")
win.geometry("1500x900")   # 전체 창 크기

create_language_buttons(win)

win.mainloop()
