import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk
import json

def get_json_from_file(dir):
    with open(f"./DB/{dir}", 'r', encoding='utf-8') as f:
        return json.load(f)

def get_program_title_label(master):
    lb = tk.Label(
        master,
        height=1
    )

    return lb

def get_language_selection(master, bt_command):
    frame = tk.Frame(
        master,
        bg='white',
        width = 860,
        height=55,
        relief='solid',
        borderwidth=2
    )

    langs = list(get_json_from_file("langs.json").items())
    
    for i, lang in enumerate(langs):
        tk.Button(
            frame,
            name=lang[0].lower(),
            bg="#989898",
            width=10,
            height=2,
            relief='solid',
            borderwidth=2,
            text=lang[1]["lang_name"],
            command=lambda lang=lang[0]: bt_command(lang)
        ).place(relx=(0.005 + i/9.05), rely=0.5, anchor='w')

    return frame

def get_filtering_container(master, combo_command):
    frame = tk.Frame(
        master,
        bg='white',
        width = 1220,
        height=70,
        relief='solid',
        borderwidth=2
    )

    style = ttk.Style()
    style.configure('TCombobox', padding=(1, 8, 1, 8))

    area_combo = ttk.Combobox(
        frame,
        width=22,
        height=17,
        font=tkfont.Font(size=14),
        justify='center',
    )
    category_combos = [
        ttk.Combobox(
            frame,
            width=33,
            height=17,
            font=tkfont.Font(size=13),
            justify='center'
        ) for _ in range(3)
    ]

    area_combo.bind("<<ComboboxSelected>>", lambda e, changed='area': combo_command(e, changed))
    area_combo.place(relx=0.12, rely=0.5, anchor='center')

    for i in range(3):
        category_combos[i].bind("<<ComboboxSelected>>", lambda e, changed=f'cat{i+1}': combo_command(e, changed))
        category_combos[i].place(relx=0.38 + 0.24*i, rely=0.5, anchor='center')

    return frame

def get_contents_container(master):
    frame = tk.Frame(
        master,
        bg='white',
        width = 1220,
        height=600,
        relief='solid',
        borderwidth=2
    )

    search_frame = tk.Frame(
        frame, 
        width=1180, 
        height=50,
        relief='solid',
        borderwidth=2
    )
    search_frame.place(relx=0.5, y=20, anchor='n') 

    tk.Label(
        search_frame,
        height=1
    ).place(x=0, rely=0.5, anchor='w')
    tk.Entry(
        search_frame,
        width=59,
        font=tkfont.Font(size=20, family="맑은 고딕"),
        relief='groove'
    ).place(x=167, rely=0.5, anchor='w')
    tk.Button(
        search_frame,
        width=10,
        height=1,
        font=tkfont.Font(size=13, family="맑은 고딕"),
        relief='groove'
    ).place(x=1063, rely=0.5, anchor='w')

    return frame