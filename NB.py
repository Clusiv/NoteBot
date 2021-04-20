class NoteBook:
    book = {}
    count = 0
    
    def create_note(self, txt):
        self.count += 1
        self.book[self.count] = txt
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
