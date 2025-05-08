"""This is used as the notes class."""


class Note:
    """Represnts a note object."""

    # Note Class
    def __init__(self, title, content, date):
        """Get self, title, content, date. Create object."""
        self.title = title  # Title of the note
        self.content = content  # Content of the note
        self.date = date  # Created at timestamp

    def modify(self, content_changed, content_data):
        """Modify note object, with content changed and content data."""
        if content_changed == "title":
            # Changes the content if the content changed is 'title'
            self.title = content_data
        elif content_changed == "content":
            # Changes the content if the content changed is 'content'
            self.content = content_data

    def delete(self):
        """Delete the note object."""
        del self
