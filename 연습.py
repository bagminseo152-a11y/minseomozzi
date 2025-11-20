from tkinter import *

def change_btn1_label():
    btn1["text"] = "안녕하세요" # 들여쓰기 수정
    
def change_btn2_label():
    btn2["text"] = "hello" # 들여쓰기 수정

def change_btn3_label():
    btn3["text"] = "곤니찌와" # 들여쓰기 수정

def change_btn4_label():
    btn4["text"] = "간체 중국어" # 들여쓰기 수정

def change_btn5_label():
    btn5["text"] = "번체어" # 들여쓰기 수정

def change_btn6_label():
    btn6["text"] = "프랑스어" # 들여쓰기 수정

def change_btn7_label():
    btn7["text"] = "독일어" # 들여쓰기 수정

def change_btn8_label():
    btn8["text"] = "스페인어" # 들여쓰기 수정

def change_btn9_label():
    btn9["text"] = "러시아어" # 들여쓰기 수정

win = Tk()

btn1 = Button(win, text="한국어")
btn2 = Button(win, text="영어", command=change_btn2_label)
btn3 = Button(win, text="일본어")
btn4 = Button(win, text="간체")
btn5 = Button(win, text="번체")
btn6 = Button(win, text="프랑스")
btn7 = Button(win, text="독일")
btn8 = Button(win, text="스페인")
btn9 = Button(win, text="러시아")

btn1.pack(side=LEFT,padx=10)
btn2.pack(side=LEFT,padx=10)
btn3.pack(side=LEFT,padx=10)
btn4.pack(side=LEFT,padx=10)
btn5.pack(side=LEFT,padx=10)
btn6.pack(side=LEFT,padx=10)
btn7.pack(side=LEFT,padx=10)
btn8.pack(side=LEFT,padx=10)
btn9.pack(side=LEFT,padx=10)


btn1.config(command=change_btn1_label)
btn2.config(command=change_btn2_label)
btn3.config(command=change_btn3_label)
btn4.config(command=change_btn4_label)
btn5.config(command=change_btn5_label)
btn6.config(command=change_btn6_label)
btn7.config(command=change_btn7_label)
btn8.config(command=change_btn8_label)
btn9.config(command=change_btn9_label)

win.mainloop()