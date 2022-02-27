"""NOTE CLASS"""


import datetime


last_id = 0


class Note:
    """
    Represent a note in the notebook. Match against a
    string in searches and store tags for each note.
    """
    def __init__(self, memo, tags=''):
        """
        Initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id.
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """
        Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and
        tags.
        """
        return filter in self.memo or filter in self.tags

    def contains(self, search_string):
        """
        Determines if the note contains the search_string.
        Check both the note_text and note_tags for the presence
        of the search_string as a sub string in the note.
        """
        return search_string in self.memo or search_string in self.tags

    def __str__(self):
        """
        String representation of the object
        """
        return ('Note Id = {0}, Date = {1}, Text = {2}, Tags = {3}'
                .format(self.id, self.creation_date, self.memo, self.tags))
