# -- Internal Imports --#
import note_class

# -- Constants --#
note_class = note_class.note

# -- Add Note Operation --#
def __init__(title, content, date):
    # Adds a note to the notes list    
    note = note_class(title, content, date)
    note.create_new_file()