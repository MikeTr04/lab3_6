"""NOTEBOOK CLASS"""

from note import Note


class Notebook:
    """
    Represent a collection of notes that can be tagged,
    modified, and searched.
    """

    def __init__(self):
        """
        Initialize a notebook with an empty list.
        """
        self.notes = []

    def new_note(self, memo, tags=''):
        """
        Create a new note and add it to the list.
        """
        self.notes.append(Note(memo, tags))

    def _find_note(self, id):
        """
        Returns the note with id that matches given one.
        Currently performs an inefficient linear scan.
        """
        for note in self.notes:
            if str(note.id) == str(id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        """Find the note with the given id and change its
        memo to the given value."""
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        """Find the note with the given id and change its
        tags to the given value."""
        for note in self.notes:
            if str(note.id) == str(note_id):
                note.tags = tags
                break

    def search(self, filter):
        """Find all notes that match the given filter
        string."""
        return [note for note in self.notes if
                note.match(filter)]
