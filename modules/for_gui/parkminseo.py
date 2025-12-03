
import tkinter as tk
from tkinter import messagebox

class TourApp:

    IMAGE_DATA = {
        "im1": "경복궁: 조선의 법궁으로, 아름다운 건축과 역사를 자랑합니다.", #예시
        "im2": "남산타워: 서울의 상징적인 랜드마크이며, 멋진 도시 전망을 제공합니다.",
    }

    def __init__(self, master):
        self.master = master
        master.title("다국어 관광 정보 제공 서비스")
        
        self.current_info = tk.StringVar()
        self.current_info.set("이미지 장소 버튼을 클릭하여 정보를 확인하세요.")
        
        self._setup_widgets()

    def _setup_widgets(self):
        
        info_label = tk.Label(
            self.master,
            textvariable=self.current_info,
            font=("Malgun Gothic", 16, "bold"),
            wraplength=700,
            justify=tk.CENTER,
            fg="#0056b3" 
        )
        info_label.pack(pady=30, padx=20)
        
        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=20)

        btn_a = tk.Button(
            button_frame,
            text="경복궁 (im1)",
            command=lambda: self.show_image_info("im1"),
            width=20,
            height=3,
            bg="#f0f0f0", 
            font=("Malgun Gothic", 12)
        )
        btn_a.pack(side=tk.LEFT, padx=30)

        btn_b = tk.Button(
            button_frame,
            text="남산타워 (im2)",
            command=lambda: self.show_image_info("im2"),
            width=20,
            height=3,
            bg="#f0f0f0",
            font=("Malgun Gothic", 12)
        )
        btn_b.pack(side=tk.LEFT, padx=30)

    def show_image_info(self, image_key):
    
        info = self.IMAGE_DATA.get(image_key, "해당 정보가 없습니다.")
        
        
        
   
        messagebox.showinfo(image_key + " 상세 정보", info)

def run_app():
    root = tk.Tk()
    root.geometry("800x450") 
    app = TourApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()