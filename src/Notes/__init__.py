# -- External Imports -- #
"""
This import is used to import the shelve module.

Which is used to store the notes.
"""
import shelve

# -- Internal Imports --#
from Classes.note import note as note_class
from Modules.checker import check_create_note as create_checker
from Modules.checker import check_modify_note as modify_checker

# -- Constants --#
note_titles = []

# -- Internal Functions -- #


def save_to_shelve(object):
    """
    Get object, and then save it to the shelve.

    Function saves the note object to shelve, and adds it
    to the noteTitles list.

    Args:
        object (object): The note object being saved.

    Returnss nothing.
    """
    with shelve.open("notes") as notes:
        # Uses the shelve.open function to open the 'notes' shelve
        try:
            # Attempts to put the object into the shelve
            notes[object.title] = object
        except Exception:
            # Prints exception if it fails
            raise Exception


def save_note(object, org="No"):
    """
    Will save the note object.

    Saves the note object to the shelve, and adds it to the note_title list.

    Args:
        object (object): The note object being saved.
        org (str): The original title of the note.
            Default is "No".
            If the note is being modified, this will be the original title.

    Returns nothing.
    """
    # Will save the note object to the shelve
    save_to_shelve(object)

    # Will remove the original title from the noteTitles list
    if not org == "No":
        # Removes the original title from the noteTitles list
        original = note_titles.index(org)
        del note_titles[original]

    # Adds the title to the noteTitles list
    note_titles.append(object.title)


def fetch_note(object_title):
    """
    Get object title and then use shelve to find the object.

    Will open the notes shelve, and get the note object.

    Args:
        object_title (str): The title of the note object.

    Returns the note object.
    """
    # Function fetches the note object from the shelve
    with shelve.open("notes") as notes:
        # Uses shelve.open function to open the 'notes' shelve
        try:
            # Attempts to get the object from the shelve
            requested_object = notes[object_title]
        except Exception:
            # Raises exception if it fails
            raise(Exception)

        # Returns the requested object
        return requested_object

# -- Importable functions -- #
def create_new_note(title: str, content: str, date: str):
    if create_checker(title, content, date):
        print(f"Created new note: {title}")
        note_object = note_class(title, content, date)
        save_note(note_object)
        return note_object

def modify_note(object_title, contentChanged, contentData):
    if modify_checker(object_title, contentChanged, contentData):
        print(f"Modifying note: {object_title}")
        object = fetch_note(object_title)
        object.modify(contentChanged, contentData)

        save_note(object, object_title)
        return object

def delete_note(object_title):
    object = fetch_note(object_title)
    object.delete()

    if object_title in note_titles:
        object_in_list_index = note_titles.index(object_title)
        del note_titles[object_in_list_index]
        raise ValueError(f"{object_title} was not found in the list.")

def fetch_all_notes():
    with shelve.open("notes") as notes:
        requestedList = []
        for title in note_titles:
            requestedObject = notes[title]
            requestedList.append(requestedObject)
    return requestedList