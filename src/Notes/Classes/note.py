"""
This is used as the notes class.
"""
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
            # Changes the content if the contentChanged is 'title'
            self.title = contentData
        elif contentChanged == "content":
            # Changes the content if the contentChanged is 'content'
            self.content = contentData

    def delete(self):
        # Deletes the note object
        del self
