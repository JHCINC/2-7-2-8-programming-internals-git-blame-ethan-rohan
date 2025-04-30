# -- External Imports -- #
import shelve

# -- Internal Imports --#
from Classes.note import note as note_class

# -- Constants --#
noteTitles = []

# -- Internal Functions -- #
def save_note(object, org="No"):
    with shelve.open("notes") as notes:
        try:
            notes[object.title] = object
        except Exception:
            print(Exception)    
    
    if not org == "No":
        original = noteTitles.index(org)
        print(f"Original Index: {original}")
        print(f"Original Title: {noteTitles[original]}")
        del noteTitles[original]

    noteTitles.append(object.title)

def fetch_note(objectTitle):
    with shelve.open("notes") as notes:
        try:
            requestedObject = notes[objectTitle]
        except Exception:
            print(Exception)
            return str(Exception)
        return requestedObject

# -- Importable functions -- #
def create_new_note(title, content, date):
    print(f"Created new note: {title}")
    note_object = note_class(title, content, date)
    save_note(note_object)
    return note_object

def modify_note(object_title, contentChanged, contentData):
    print(f"Modifying note: {object_title}")
    object = fetch_note(object_title)
    object.modify(contentChanged, contentData)

    save_note(object, object_title)
    return object

def delete_note(object_title):
    object = fetch_note(object_title)
    object.delete()

    object_in_list_index = noteTitles.index(object_title)
    del noteTitles[object_in_list_index]

def fetch_all_notes():
    with shelve.open("notes") as notes:
        requestedList = []
        for title in noteTitles:
            requestedObject = notes[title]
            requestedList.append(requestedObject)
    return requestedList