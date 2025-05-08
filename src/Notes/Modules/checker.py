"""This document is used for all of the checking involved."""
# -- Internal functions -- #


def check_if_not_empty(string):
    """
    Get the string, check if empty. Return True/False.

    Checks if the string is empty.

    Args:
        string (str): The string.

    Returns:
        true: If it is empty
        false: If it isn't empty
    """
    if string:
        return True
    else:
        return False

# -- Importable functions -- #


def check_create_note(title: str, content: str, date: str):
    """
    Get title, content, date. Check if valid.

    Checks if the all the paremeters are valid.

    Args:
        title (str): The note's title.
        content (str): The note's content.
        date (str): The note's date

    Returns:
        True: If it's valid
        False: If it's not valid
    """
    passed_1a = isinstance(title, str)
    passed_2a = isinstance(content, str)
    passed_3a = isinstance(date, str)

    # Tests if it is a string
    if not passed_1a or not passed_2a or not passed_3a:
        # Raises error if returns false
        raise TypeError(
            f"Must be strings, Request: {title}, {content}, {date}")
        return False

    passed_1b = check_if_not_empty(title)
    passed_2b = check_if_not_empty(content)
    passed_3b = check_if_not_empty(date)

    # Tests if the string is empty
    if not passed_1b or not passed_2b or not passed_3b:
        # Raises error if returns false
        raise TypeError(
            f"Cannot be empty, Request: {title}, {content}, {date}")
        return False

    return True


def check_modify_note(title: str, change: str, data: str):
    """
    Get title, change, data.

    Checks if the all the paremeters are valid.

    Args:
        title (str): The note's title.
        change (str): The note's content being changed.
        data (str): The note's contentData

    Returns:
        True: If it's valid
        False: If it's not valid
    """
    passed_1a = isinstance(title, str)
    passed_2a = isinstance(change, str)
    passed_3a = isinstance(data, str)

    # Tests if it is a string
    if not passed_1a or not passed_2a or not passed_3a:
        # Raises error if returns false
        raise TypeError(
            f"Must be strings, Request: {title}, {change}, {data}")
        return False

    passed_1b = check_if_not_empty(title)
    passed_2b = check_if_not_empty(change)
    passed_3b = check_if_not_empty(data)

    # Tests if the string is empty
    if not passed_1b or not passed_2b or not passed_3b:
        # Raises error if returns false
        raise TypeError(
            f"Cannot be empty, Request: {title}, {change}, {data}")
        return False

    return True


def check_delete_note(object_title: str):
    """
    Get title. Check if valid.

    Checks if the all the paremeters are valid.

    Args:
        title (str): The note's title.

    Returns:
        True: If it's valid
        False: If it's not valid
    """
    # Tests if it is a string
    if not isinstance(object_title, str):
        # Raises error if returns false
        raise IndexError(
            f"Must be strings, Request: {object_title}")
        return False

    # Tests if the string is empty
    if not check_if_not_empty(object_title):
        # Raises error if returns false
        raise IndexError(
            f"Cannot be empty, Request: {object_title}")
        return False

    return True
