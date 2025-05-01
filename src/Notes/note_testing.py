import __init__ as init

print("Testing Note delete checker")
print("attempting to fix bug")
print("Found the error it was that the code oes not check if it is the noteTitles list before attemping to delete it, this caused the code to crash")
print("bug solved")

note1 = init.create_new_note("Test Title", "Test Content", "Test Date")
print(f"Title: {note1.title}, Content: {note1.content}, Date: {note1.date}. Object: {note1}")


modified_note = init.modify_note("Test Title", "title", "New Content 123")
print(f"Title: {modified_note.title}, Content: {modified_note.content}, Date: {modified_note.date}. Object: {modified_note}")

print(init.fetch_all_notes())

print("Above should prind one note ")

init.delete_note("New Content 123")
print(init.fetch_all_notes())
print("Above should print no notes")

print("below should show how the bug was fixed")
note2 = init.create_new_note("Test Title 2", "Test Content 2", "Test Date 2")
print(f"Title: {note2.title}, Content: {note2.content}, Date: {note2.date}. Object: {note2}")
print("Below a ValueError should be raised")

init.delete("One two three")