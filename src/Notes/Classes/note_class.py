# -- Internal Imports --#
import os

# -- Constants --#
notes = []

operationsNumber = {
    "Title": 0,
    "Content": 1,
    "Date": 2
}

# -- Fetch Note --#
def fetchNote(noteTitle):
    for note in notes:
        if note[0] == noteTitle:
            return note

#-- Check contentChanged --#
def checkContentChanged(contentChanged):
    return int(operationsNumber[contentChanged])

# -- Notes Class -- #
class note:
    # Note Class
    def __init__(self, title, content, date):
       # Creates a new note object
        self.title = title # Title of the note
        self.content = content # Content of the note
        self.date = date # Created at timestamp
    
    def create_new_file(self):
        # Creates a new file with the note content
        note = []

        note.append(self.title)
        note.append(self.content)
        note.append(self.date)

        notes.append(note)

    def modify_note(self, contentChanged, contentData):
        # Creates a new file with the note content
        note = fetchNote(self.title)
        type = checkContentChanged(contentChanged)

        print(f"Type: {type}")
        print(f"Content Date: {contentData}")
        self.contentChanged = contentData
        note[type] = contentData
        print(f"Updated Note Content: {note[type]}")

    def delete_note(self):
        # Creates a new file with the note content
        note = fetchNote(self.title)
        del notes[note]

