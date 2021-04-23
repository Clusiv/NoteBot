import tkinter as tk
from tkinter import END

from tkinter import ttk

import time
from NB2 import NoteBook

window = tk.Tk()

window.title("NoteBook")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(2, minsize=800, weight=1)

window.configure(bg='#494949')

notebooks_frame = tk.Frame(window)
notebooks_frame.config(background = '#494949', )

notes_frame = tk.Frame(window)
notes_frame.config(background = '#494949')

txt_edit_frame = tk.Frame(window)
txt_edit_frame.config(background = '#494949')

txt_edit = tk.Text(master=txt_edit_frame)

notebook1 = NoteBook('Code Snippets','Code Snippets', master=notebooks_frame)
notebook1.create_note('C# Snippets', 'Snippets C#', master=notes_frame)
notebook1.create_note('Python Snippets', 'Snippets Python', master=notes_frame)

notebook2 = NoteBook('Life Hacks', 'Life Hacks', master=notebooks_frame)
notebook2.create_note('Morning routine', 'Tea, gym, ...', master=notes_frame)
notebook2.create_note('Health', 'Drink water', master=notes_frame)

notebooks = [notebook1, notebook2]


notebooks_frame.grid(row=0, column=0,  padx=5, sticky=tk.NSEW)
notes_frame.grid(row=0, column=1,  padx=5, sticky=tk.NSEW)
txt_edit_frame.grid(row=0, column=2, sticky=tk.NSEW)

def show_notes(event, notebook):
    for index, note in notebook.book.items():
        note.bind("<Button-1>", lambda event, widget=note: show_note(event, widget))
        note.pack()

def show_note(event, note):
    txt_edit.delete(1.0, END)
    txt_edit.insert(1.0, note.txt)

for notebook in notebooks:
    notebook.bind("<Button-1>", lambda event, widget=notebook: show_notes(event, widget))
    notebook.pack()



txt_edit.pack()

window.mainloop()