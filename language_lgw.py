from tkinter import *

win = Tk()
win.title("Language Buttons")
win.geometry("1100x80")

selected_button = None

def select_button(btn):
    global selected_button

    # ▷ 같은 버튼 다시 누르면 → 비활성화
    if selected_button == btn:
        btn.config(bg="#7f8282", relief="flat")
        selected_button = None
        return

    # ▷ 다른 버튼 눌렀을 때 → 이전 버튼 비활성화
    if selected_button and selected_button != btn:
        selected_button.config(bg="#7f8282", relief="flat")

    # ▷ 현재 버튼 활성화
    btn.config(relief="sunken", bg="#8ed1dc")
    selected_button = btn


texts = [
    "한국어", "영어", "일본어", "중국어(간체)", "중국어(번체)",
    "프랑스어", "독일어", "스페인어", "러시아어"
]

buttons = []

for t in texts:
    btn = Button(
        win,
        text=t,
        font="HY견고딕 9",
        bg="#7f8282",
        relief="flat",
        width=15,
        height=3,
        padx=8,
        pady=8
    )

    btn.config(command=lambda b=btn: select_button(b))
    btn.pack(side=LEFT, padx=10, pady=5)
    buttons.append(btn)

win.mainloop()
