"""
This import is used to import the shelve module.

Which is used to store the notes.
"""
# -- External Imports -- #
import shelve

# -- Internal Imports --#
from note_class import Note as note_class
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
    """
    Get the title, content, and date. Then send that to the note class.

    Will get the title, content, date and then use the note class to save it.

    Args:
        title (str): The title title of the note.
        content (str): The content of the note.
        date (str): The date the note was created.

    Returns the note object.
    """
    if create_checker(title, content, date):
        # Will check if the title, content, dand date are valid
        print(f"Created new note: {title}")

        # Uses note_class to create a new note object
        note_object = note_class(title, content, date)

        # Saves the note object
        save_note(note_object)
        return note_object


def modify_note(object_title, content_changed, content_data):
    """
    Get the object_title, content changed, and data.

    Then send that to the note class's modify.

    Will get the object title, and the content changed, and content data.
    Then send it to the note class's modify function.

    Args:
        object_title (str): The title title of the note.
        content_changed (str): What content needs to be changed.
        content_data (str): The data itself that neededs to be changed.

    Returns the note object.
    """
    if modify_checker(object_title, content_changed, content_data):
        # Will check if the object title, content changed,
        # and content data are valid
        print(f"Modifying note: {object_title}")

        # Will get the note object from the shelve
        object = fetch_note(object_title)

        # Will modify the note object
        object.modify(content_changed, content_data)

        # Saves the note, and makes sure the old one is deleted
        save_note(object, object_title)
        return object


def delete_note(object_title):
    """
    Get the object title, and then delete it.

    Will get the object title, check if valid.
    Then send it to the note class's delete function.

    Args:
        object_title (str): The title title of the note.

    Returns the note object.
    """
    # Gets the object
    object = fetch_note(object_title)

    # Deletes the object
    object.delete()

    if object_title in note_titles:
        # Checks if the object title is in the noteTitles list
        object_in_list_index = note_titles.index(object_title)

        # Deletes the title from the noteTitles list
        del note_titles[object_in_list_index]
        raise ValueError(f"{object_title} was not found in the list.")


def fetch_all_notes():
    """
    Return all of the notes saved.

    Will return all of then notes saved in the shelve.

    Returns a list of the notes.
    """
    with shelve.open("notes") as notes:
        # Uses the shelve.open function to open the 'notes' shelve
        # Uses the list below to save them all
        requested_list = []
        for title in note_titles:
            # Gets the object from the shelve
            requested_object = notes[title]
            # Appends the object to the list
            requested_list.append(requested_object)
    return requested_list
