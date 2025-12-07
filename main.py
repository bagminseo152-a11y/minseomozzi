import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk
from modules.for_gui.sonjiho import *

selected_lang = None

def set_lang(lang):
    global selected_lang

    selected_lang = lang

    all_contents.clear()
    all_contents.update(get_json_from_file(f"spots/spots_{lang}.json"))

    text = get_json_from_file("langs.json")[lang]

    # 프로그램명 설정
    program_title_label.config(
        text=get_json_from_file("program_titles.json")[lang],
        width=18 if lang == "Rus" else 16,
        font=tkfont.Font(size=26 if lang == "Rus" else 30, weight='bold', family='HY견고고딕')
    )

    # 언어 선택 버튼 설정
    for bt in language_selection.winfo_children():
        if bt.winfo_name() == lang.lower():
            bt.config(fg='black', font=tkfont.Font(size=10, weight='bold'))
        else:
            bt.config(fg='white', font=tkfont.Font(size=11, weight='normal'))

    # 필터링 콤보박스 설정
    filters = filtering_container.winfo_children()
    area_filter = filters[0]
    category_filters = filters[1:]

    areas_names = [names[lang] for _, names in get_json_from_file(f"code_info/area.json").items()]
    area_filter.config(values=areas_names)
    area_filter.set(text["select_area"])

    theme_data = get_json_from_file(f"code_info/theme.json")
    for i in range(1, 4):
        category_names = [names[lang] for _, names in theme_data[f"cat{i}"].items()]
        if i == 1:
            category_filters[0].config(values=category_names)
            category_filters[0].set(text["select_cat1"])
        else:
            category_filters[i-1].config(values=[])
            category_filters[i-1].set("─")

    # 컨텐츠 목록
    search_frame = contents_container.winfo_children()[0]
    serch_label, search_bt = search_frame.winfo_children()[::2]
    serch_label.config(text=text["content_name"])
    search_bt.config(text=text["search_content"])

    if lang == "Ger":
        serch_label.config(width=26, font=tkfont.Font(size=8, family="맑은 고딕"))
    else:
        serch_label.config(width=16, font=tkfont.Font(size=13, family="맑은 고딕"))


def get_filtered_contents(e, changed):
    text = get_json_from_file("langs.json")[selected_lang]

    filters = filtering_container.winfo_children()

    theme_data = get_json_from_file(f"code_info/theme.json")
    categories_info = [[(code, names[selected_lang]) for code, names in theme_data[f"cat{i}"].items()] for i in range(1, 4)]

    if changed == "cat1":
        parent_code = [code for code, name in categories_info[0] if name == filters[1].get()][0]
        print(parent_code)
        filters[2].config(values=[name for code, name in categories_info[1] if parent_code in code])
        filters[2].set(text["select_cat2"])
        filters[3].config(values=[])
        filters[3].set("─")
    elif changed == "cat2":
        parent_code = [code for code, name in categories_info[1] if name == filters[2].get()][0]
        print(parent_code)
        filters[3].config(values=[name for code, name in categories_info[2] if parent_code in code])
        filters[3].set(text["select_cat3"])

all_contents = {}

win = tk.Tk()
screen_width, screen_height = win.winfo_screenwidth(), win.winfo_screenheight()
win_width, win_height = 1380, 900
win.geometry(f"{win_width}x{win_height}+{int((screen_width-win_width)/2)}+{int((screen_height-win_height)/2) - 40}")

program_title_label = get_program_title_label(win)
program_title_label.place(x=25, y=30)

language_selection = get_language_selection(win, set_lang)
language_selection.place(x=440, y=30)

filtering_container = get_filtering_container(win, get_filtered_contents)
filtering_container.place(x=80, y=130)

contents_container = get_contents_container(win)
contents_container.place(x=80, y=230)

set_lang("Kor")

win.mainloop()