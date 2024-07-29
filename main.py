import random
from objs import *

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

    # Transpose the phrase and play
    transposed_phrase = phrase.transpose(2)
    transposed_phrase.play()

    # Invert the phrase and play
    inverted_phrase = phrase.inversion()
    inverted_phrase.play()

    # Retrograde the phrase and play
    retrograded_phrase = phrase.retrograde()
    retrograded_phrase.play()

    # Retrograde inversion and play
    retrograded_inverted_phrase = phrase.retrograde_inversion()
    retrograded_inverted_phrase.play()