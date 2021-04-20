class NoteBook:
    def __init__(self, name):
        self.name = name
        self.book = {}
        self.count = 0

    def __repr__(self):
        return self.name

    def create_note(self, name, txt):
        self.count += 1
        self.book[self.count] = Note(self.count, name, txt)
        return self.count
    
    def get_note(self, id):
        return self.book[id]
    
    def find_note(self, st):
        for note_id in self.book:
            if st in self.book[note_id]:
                return self.book[note_id]
        return "Nothing found"

        searched_notes = set(searched_notes)
        return ''.join(searched_notes) + '\n'

class Note:
    def __init__(self, id, name, txt):
        self.id = id
        self.name = name
        self.txt = txt
    