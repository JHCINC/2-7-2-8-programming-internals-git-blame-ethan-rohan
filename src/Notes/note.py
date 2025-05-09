overload_title = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas fermentum congue nunc id sagittis. In tempor congue metus id condimentum. Fusce ut arcu at eros dignissim ultricies vitae ac lacus. "
overload_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas fermentum congue nunc id sagittis. In tempor congue metus id condimentum. Fusce ut arcu at eros dignissim ultricies vitae ac lacus. " * 20

import time
import sys

print(f"System Path: {sys.path}")

import __init__ as init

def txt_to_string(txt):
  with open(txt, 'r') as screens:
    for lines in screens:
        list = []
        list.append(lines.strip())
    screens.close()
    return list

# -- weird bug log
print("Testing Note delete checker")
print("attempting to fix bug")
print("Found the error it was that the code oes not check if it is the noteTitles list before attemping to delete it, this caused the code to crash")
print("bug solved")
print("testing lennox trying to break it")
print("t3eting brocks")

# -- add note test -- #
note1 = init.create_new_note("Test Title", "Test Content", "Test Date")
print(f"Title: {note1.title}, Content: {note1.content}, Date: {note1.date}. Object: {note1}")

# -- Lenny Input -- #

brock = init.create_new_note("asd", "asd", "asd")
print(f"brock Title: {brock.title}, Content: {brock.content}, Date: {brock.date}. Object: {brock}")
# -- overload test -- #
note_max = init.create_new_note(overload_title, overload_content, "ASD ASDHSASSHDAHSHASD")
start_time = time.perf_counter()
print(f"Max Title: {note_max.title}, Max Content: {note_max.content}, Max Date: {note_max.date}. Object: {note_max}")
end_time = time.perf_counter()
elapsed = end_time - start_time
print(f"Time taken to create max note: {elapsed} seconds")

# -- modified test -- #
modified_note = init.modify_note("Test Title", "title", "New Content 123")
print(f"Title: {modified_note.title}, Content: {modified_note.content}, Date: {modified_note.date}. Object: {modified_note}")

print(init.fetch_all_notes())

print("Above should prind one note ")


# -- delete test -- #
init.delete_note("New Content 123")
print(init.fetch_all_notes())
print("Above should print no notes")

# -- delete error test -- #
'''
print("below should show how the bug was fixed")
note2 = init.create_new_note("Test Title 2", "Test Content 2", "Test Date 2")
print(f"Title: {note2.title}, Content: {note2.content}, Date: {note2.date}. Object: {note2}")
print("Below a ValueError should be raised")

init.delete("One two three")'''