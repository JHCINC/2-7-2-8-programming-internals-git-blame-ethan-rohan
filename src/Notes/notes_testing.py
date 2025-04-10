#-- External Imports --#
import time

# -- Internal Imports -- #
from Classes import note_class

note = note_class.note("asd", "asd", "asd")
note.create_new_file()

print(note)
print(f"Title: {note.title}")
print(f"Content: {note.content}")
print(f"Date: {note.date}")

time.sleep(1)
print("note should be going now")

note.modify_note("Title", "New Title")
print(f"Title: {note.title}")