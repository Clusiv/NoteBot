import tkinter as tk
from tkinter import ttk

class NoteBook(ttk.Button):
    def __init__(self, label, name, master):
        tk.Button.__init__(self, text=label, master = master, bg='black')
        self.name = name
        self.book = {}
        self.count = 0

    def __repr__(self):
        return self.name

    def create_note(self, name, txt, master):
        self.count += 1
        self.book[self.count] = Note(self.count, name, txt, master=master)
        return self.count
    
    def get_note(self, id):
        return self.book[id]
    
    def find_note(self, st):
        for note_id in self.book:
            if st in self.book[note_id]:
                return self.book[note_id]
        return "Nothing found"

        # searched_notes = set(searched_notes)
        # return ''.join(searched_notes) + '\n'

    def get_all(self):
        return self.book

class Note(tk.Button):
    def __init__(self, id, name, txt, master):
        tk.Button.__init__(self, text = name, master = master, bg='#ffb3fe')
        self.id = id
        self.name = name
        self.txt = txt

if __name__ == '__main__':
    pass