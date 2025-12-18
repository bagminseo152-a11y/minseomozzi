import tkinter as tk
import tkinter.font as tkfont
from modules.for_gui.sonjiho import *
from modules.for_gui.ryukyuyeol import *
from modules.for_gui.ryuhyeyeon import *
from modules.for_gui.parkminseo import *
from modules.for_gui.leegunwoo import *
from modules.for_gui.jojoonhyuk import *
from modules.for_data.choijiwon import *


selected_lang = None
contents = {}


# 언어 선택 함수
def set_lang(lang):
    global selected_lang

    selected_lang = lang
    text = get_json_from_file("langs.json")[lang]

    program_name = get_json_from_file("program_titles.json")[lang]

    win.title(program_name)
    program_title_label.config(
        text=program_name,
        width=18 if lang == "Rus" else 16,
        font=tkfont.Font(size=26 if lang == "Rus" else 30, weight='bold', family='HY견고고딕')
    )

    for bt in language_selection.winfo_children():
        if bt.winfo_name() == lang.lower():
            bt.config(fg='black', font=tkfont.Font(size=10, weight='bold'))
        else:
            bt.config(fg='white', font=tkfont.Font(size=11, weight='normal'))

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

    search_frame = contents_container.winfo_children()[0]
    serch_label, search_bt = search_frame.winfo_children()[::2]
    serch_label.config(text=text["content_name"])
    search_bt.config(text=text["search_content"])

    if lang == "Ger":
        serch_label.config(width=26, font=tkfont.Font(size=8, family="맑은 고딕"))
    else:
        serch_label.config(width=16, font=tkfont.Font(size=13, family="맑은 고딕"))

    contents.clear()
    contents.update(get_json_from_file(f"spots/spots_{lang}.json"))
    display_content_cards(0)


# 관광지 지역, 분류 필터링 함수
def filter_contents(e, changed):
    text = get_json_from_file("langs.json")[selected_lang]

    filters = filtering_container.winfo_children()

    theme_data = get_json_from_file(f"code_info/theme.json")
    categories_info = [[(code, names[selected_lang]) for code, names in theme_data[f"cat{i}"].items()] for i in range(1, 4)]

    if changed == "cat1":
        parent_code = [code for code, name in categories_info[0] if name == filters[1].get()][0]
        filters[2].config(values=[name for code, name in categories_info[1] if parent_code in code])
        filters[2].set(text["select_cat2"])
        filters[3].config(values=[])
        filters[3].set("─")
    elif changed == "cat2":
        parent_code = [code for code, name in categories_info[1] if name == filters[2].get()][0]
        filters[3].config(values=[name for code, name in categories_info[2] if parent_code in code])
        filters[3].set(text["select_cat3"])


    find_area_code = [
        code for code, names in get_json_from_file("code_info/area.json").items() 
        if names[selected_lang] == filters[0].get()
    ][0] if filters[0].get() != text["select_area"] else None

    find_cat_codes = [
        (
            [
                code for code, names in get_json_from_file("code_info/theme.json")[f"cat{i}"].items() 
                if names[selected_lang] == filters[i].get()
            ][0] 
            if (filters[i].get() != text[f"select_cat{i}"]) and (filters[i].get() != "─") else None
        )
        for i in range(1, 4)
    ]

    filtered_contents = {}
    all_contents = get_json_from_file(f"spots/spots_{selected_lang}.json")
    for code, data in all_contents.items():
        if (find_area_code is not None) and (data["area_code"] != find_area_code):
            continue
        if (find_cat_codes[0] is not None) and (data["theme_code"]["cat1"] != find_cat_codes[0]):
            continue
        if (find_cat_codes[1] is not None) and (data["theme_code"]["cat2"] != find_cat_codes[1]):
            continue
        if (find_cat_codes[2] is not None) and (data["theme_code"]["cat3"] != find_cat_codes[2]):
            continue

        filtered_contents[code] = data

    contents.clear()
    contents.update(filtered_contents)
    display_content_cards(0)


# 관광지 검색 필터링 함수
def get_searched_contents():
    search_text = contents_container.search_entry.get()
    filtered_contents = dict(filter(lambda data: data[1]["title"] == search_text, contents.items()))

    contents.clear()
    contents.update(filtered_contents)
    display_content_cards(0)


# 전체 또는 필터링된 관광지 카드 띄워주는 함수
def display_content_cards(index):
    contents_data = list(contents.items())

    if len(contents_data) <= index*12:
        return
    elif len(contents_data[index*12:]) < 12:
        target_contents = contents_data[index:]
    else:
        target_contents = contents_data[index*12 : (index+1)*12]
    

    contents_frame = contents_container.contents_frame

    for content_frame in contents_frame.winfo_children():
        content_frame.destroy()

    for i, (code, data) in enumerate(target_contents):
        card = ContentCard(
            contents_container.contents_frame,
            data=data,
            content_id=code,
            lang=selected_lang,
            click_command=lambda e, lang, cid: display_content_detail(e, win, lang, cid)
        )
        card.place(
            x=297 * (i % 4),
            y=166 * (i // 4)
        )

    indexings = index_changing_buttons_container.winfo_children()
    
    if index != 0:
        indexings[0].config(command=lambda i=index-1: display_content_cards(i))
    else:
        indexings[0].config(command=None)
    
    indexings[1].config(text=f"{index+1}")

    if len(contents_data) <= (index+1)*12:
        indexings[2].config(command=None)
    else:
        indexings[2].config(command=lambda i=index+1: display_content_cards(i))


# 메인 창 생성
win = tk.Tk()
win.title("")
screen_width, screen_height = win.winfo_screenwidth(), win.winfo_screenheight()
win_width, win_height = 1380, 900
win.geometry(f"{win_width}x{win_height}+{int((screen_width-win_width)/2)}+{int((screen_height-win_height)/2) - 40}")


# 프로그램 타이틀 라벨 생성 및 배치
program_title_label = ProgramTitleLabel(win)
program_title_label.place(x=25, y=30)


# 언어 선택란 생성 및 배치
language_selection = LanguageSelection(win, set_lang)
language_selection.place(x=440, y=30)


# 필터링 컨테이너 생성 및 배치
filtering_container = FilteringContainer(win, filter_contents)
filtering_container.place(x=80, y=130)


# 관광지 목록 컨테이너 생성 및 배치
contents_container = ContentsContainer(win, get_searched_contents)
contents_container.place(x=80, y=230)


# 관광지 목록 인덱스 전환 버튼 생성 및 배치
index_changing_buttons_container = IndexChangingButtons(win)
index_changing_buttons_container.place(relx=0.5, y=840, anchor='n')


# 초기 언어를 한국어로 지정
set_lang("Kor")


win.mainloop()