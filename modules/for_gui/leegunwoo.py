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

import tkinter as tk
from PIL import Image, ImageTk
def card_frame():
    # -----------------------------
    # 카드 프레임 (height = 200 유지)
    # -----------------------------
    card = tk.Frame(root, width=320, height=200, bg="white", bd=4, relief="ridge")
    card.pack(pady=20)
    card.pack_propagate(False)

    # -----------------------------
    # 사진 영역 (높이 줄여서 공간 확보)
    # -----------------------------
    img_frame = tk.Frame(card, width=300, height=160, bg="#d9d9d9", bd=2, relief="ridge")
    img_frame.pack(pady=5)
    img_frame.pack_propagate(False)

    # 이미지 대신 임시 텍스트
    tk.Label(img_frame, text="(관광지 사진)", bg="#d9d9d9").pack(expand=True)

    # -----------------------------
    # 관광지 이름만 표시
    # -----------------------------
    name_label = tk.Label(
        card,
        text="N Seoul Tower",
        font=("Arial", 11, "bold"),
        bg="white"
    )
    name_label.pack(pady=5)
    return card

root = tk.Tk()
root.title("관광지 카드 예시")
root.geometry("1500x900")
root.configure(bg="white")
card_frame().pack()
root.mainloop()
