# -- Internal Imports --#
import note_class

# -- Constants --#
note_class = note_class.note

# -- Operation Class --#
class operation_class:
    # Operation Class
    def __init__(self, name, function):
        self.name = name # Operation Name
        self.function = function  # Function attached to operation

    def call_function(self):
        # Call the function attached to the operation
        return self.function()
    
# -- Add Note Operation --#
def add_note(Title, Content, Date):
    # Add Note Operation
    print("Add Note Operation")
    # Create a new note object
    new_note = note_class(Title, Content, Date)
    new_note.create_new_file()

# -- Modify Note Operation --#
def modify_note(note, contentChanged, contentData):
    # Modify Note Operation
    print("Modify Note Operation")
    # Create a new note object
    note.modify_note(contentChanged, contentData)

# -- Delete Note Operation --# 
def delete_note(noteName):
    # Delete Note Operation
    print("Delete Note Operation")
    # Create a new note object
    if noteName is str:
        note = fetch_note(noteName)
        note_class.delete_note(noteName)
    elif noteName.isclass(noteName):
        noteName.delete_note(noteName.title)

def fetch_note(noteName):
    # Fetches the note
    return note_class.fetchNote(noteName)
