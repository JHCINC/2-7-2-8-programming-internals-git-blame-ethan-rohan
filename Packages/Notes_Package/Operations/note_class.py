# -- Internal Imports --#

# -- Constants --#

# -- Fetch Notes Operations --#
def __init__():
    print("Notes Class init loaded")

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
        with open(f"{self.tilte}.txt", "w") as note_file:
            note_file.write(f"Title: {self.title}\n")
            note_file.write(f"Creation Date: {self.date}\n")
            note_file.write(f"Content: {self.content}\n")
