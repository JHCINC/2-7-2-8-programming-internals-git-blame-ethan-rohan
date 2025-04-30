# -- Basic Documentation -- #
'''
Save_Note(self, list) - Saves a note to a specific list,
modify_note(self, contentChanged, contentData) - Modify an element in the note
delete_note(self, , list) - Deletes the object instance
'''

# -- Internal Imports --#

# -- Constants --#
operationsNumber = {
    "title": 0,
    "content": 1,
    "date": 2
}

# -- Fetch Note --#
def fetchNote(list, noteTitle):
    for note in list:
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
    
    def save_note(self, list):
        # Creates a new file with the note content
        note = []

        note.append(self.title)
        note.append(self.content)
        note.append(self.date)

        list.append(note)

    def modify_note(self, contentChanged, contentData):
        # Creates a new file with the note content
        note_in_list = fetchNote(list, self.title)
        type = checkContentChanged(contentChanged)

        print(f"Self: {self}")
        print(f"Type: {type}")
        print(f"Content Date: {contentData}")
        if contentChanged == "title":
            self.title = contentData
        elif contentChanged == "content":
            self.content = contentData
        elif contentChanged == "date":
            self.date = contentData

        note_in_list[type] = contentData
        print(f"Updated Note Content (Self): {self.title}")
        print(f"Updated Note Content (In list): {note_in_list[type]}")

    def delete_note(self, list):
        # Creates a new file with the note content
        note = fetchNote(self.title)
        note_index = list.index(note)
        print("deleting note")
        # havent tested this 
        del list[note_index]
    

