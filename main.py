import random
import winsound
from Algs.objs import Note, Phrase

if __name__ == "__main__":
    # Create an empty phrase
    phrase = Phrase()

    # Add notes to the phrase
    note1 = Note(60)  # C4
    note2 = Note(62)  # D4
    note3 = Note(64)  # E4

    phrase.add_note(note1)
    phrase.add_note(note2)
    phrase.add_note(note3)

    # Play the phrase
    phrase.play()

    phrase.retrograde().play()

    phrase.inversion().play()

    phrase.transpose(2).play()