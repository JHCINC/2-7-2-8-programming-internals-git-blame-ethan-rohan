# -- Basic Documentation -- #
'''
Save_Note(self, list) - Saves a note to a specific list,
modify_note(self, contentChanged, contentData) - Modify an element in the note
delete_note(self, , list) - Deletes the object instance
'''

# -- Internal Imports --#

# -- Notes Class -- #
class note:
    # Note Class
    def __init__(self, title, content, date):
       # Creates a new note object
        self.title = title # Title of the note
        self.content = content # Content of the note
        self.date = date # Created at timestamp

    def modify(self, contentChanged, contentData):
        # Creates a new file with the note content
        if contentChanged == "title":
            self.title = contentData
        elif contentChanged == "content":
            self.content = contentData

    def delete(self):
        del self
