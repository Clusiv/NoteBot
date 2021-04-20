import tkinter as tk
import time
from NB2 import NoteBook


notebook1 = NoteBook('Code Snippets')
notebook1.create_note('C# Snippets', 'Snippets Python')
notebook1.create_note('Python Snippets', 'Snippets C#')

notebook2 = NoteBook('Life Hacks')
notebook2.create_note('Morning routine', 'Tea, gym, ...')
notebook2.create_note('Health', 'Drink water')

notebooks = {1:notebook1, 2:notebook2}

window = tk.Tk()

window.title("NoteBook")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(2, minsize=800, weight=1)

notebooks_frame = tk.Frame(window)
notes_frame = tk.Frame(window)
txt_edit_frame = tk.Frame(window)

notebooks_frame.grid(row=0, column=0,  padx=5)
notes_frame.grid(row=0, column=1,  padx=5)
txt_edit_frame.grid(row=0, column=2)

def handle_click(event,notebook):
    for note in notebook:
        note_widget = tk.Label(master=notes_frame, text=note.id)
        note_widget.pack()

for notebook in notebooks:
    notebook_widget = tk.Label(master=notebooks_frame, text=notebooks[notebook])
    notebook_widget.pack()
    notebook_widget.bind("<Button-1>", lambda event, obj=notebook: handle_click(event, notebook))


notes = tk.Label(master=notes_frame, text="I'm in Frame b")
txt_edit = tk.Text(master=txt_edit_frame)


notes.pack()
txt_edit.pack()

window.mainloop()