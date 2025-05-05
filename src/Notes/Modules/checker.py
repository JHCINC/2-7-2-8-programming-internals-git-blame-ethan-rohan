# -- External Imports -- #

# -- Internal Imports -- #

# -- Internal functions -- #
def check_if_not_empty(string):
    if string:
        return True
    else:
        return False


# -- Importable functions -- #
def check_create_note(title: str, content: str, date: str):

    if not isinstance(title, str) or not isinstance(content, str) or not isinstance(date, str):
        raise TypeError(f"Title, and or content, and or date must be strings. Request can be found here: {title}, {content}, {date}")
        return False
    
    if not check_if_not_empty(title) or not check_if_not_empty(content) or not check_if_not_empty(date):
        raise IndexError(f"Title, and or content, and or date cannot be empty. Request can be found here: {title}, {content}, {date}")
        return False

    return True

def check_modify_note(object_title: str, contentChanged: str, contentData: str):

    if not isinstance(object_title, str) or not isinstance(contentChanged, str) or not isinstance(contentData, str):
        raise IndexError(f"Object Title, and or contentChanged, and or contentData must be strings. Request can be found here: {object_title}, {contentChanged}, {contentData}")
        return False
    
    if not check_if_not_empty(object_title) or not check_if_not_empty(contentChanged) or not check_if_not_empty(contentData):
        raise IndexError(f"Object Title, and or contentChanged, and or contentData cannot be empty. Request can be found here: {object_title}, {contentChanged}, {contentData}")
        return False

    return True

def check_delete_note(object_title: str):

    if not isinstance(object_title, str):
        raise IndexError(f"Object Title must be a string. Request can be found here: {object_title}")
        return False
    
    if not check_if_not_empty(object_title):
        raise IndexError(f"Object Title cannot be empty. Request can be found here: {object_title}")
        return False

    return True