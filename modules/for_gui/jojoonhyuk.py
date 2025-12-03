import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("관광지 카드 예시")
root.geometry("1500x900")
root.configure(bg="white")

# -----------------------------
# 카드 프레임 (height = 200 유지)
# -----------------------------
card = tk.Frame(root, width=320, height=200, bg="white", bd=4, relief="ridge")
card.pack(pady=20)
card.pack_propagate(False)

# -----------------------------
# 사진 영역 (높이 줄여서 공간 확보)
# -----------------------------
img_frame = tk.Frame(card, width=300, height=110, bg="#d9d9d9", bd=2, relief="ridge")
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
    font=("Arial", 15, "bold"),
    bg="white"
)
name_label.pack(pady=5)

root.mainloop()
