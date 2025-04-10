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

note_in_list = note_class.fetchNote(note.title)

time.sleep(1)
print("note should be going now")

note.modify_note("title", "New Title")
note.modify_note("content", "this is a really good note idea")
print(f"Self (Testing): {note}")
print(f"Title (In list): {note_in_list[0]}")
print(f"Title: {note.title}")
print(f"Content: {note.content}")

note.delete_note()