import __init__ as init

note1 = init.create_new_note("Test Title", "Test Content", "Test Date")
note_list = []

print("Testing Create new Note & modify note & delete note")

note_list.append(note1)
note_list.append(note1.title)
note_list.append(note1.content)
note_list.append(note1.date)

print(note_list)

modified_note = init.modify_note(note1.title, "title", "New Title")

print(modified_note.title)

print(init.fetch_all_notes())

print(f"Now deleting the note: {modified_note}")
init.delete_note(modified_note.title)

print(init.fetch_all_notes())