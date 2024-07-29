import winsound

class Note:
    def __init__(self, pitch):
        self.pitch = pitch

    def play(self, duration):
        # do a pitch conversion
        frequency = 440 * (2 ** ((self.pitch - 69) / 12))
        winsound.Beep(int(frequency), duration)

    def show(self):
        print(self.pitch)

class Phrase:
    def __init__(self, notes=None):
        self.notes = notes if notes is not None else []

    def play(self, duration=200):  # Default duration of 500ms for each note
        for note in self.notes:
            note.play(duration)

    def inversion(self):
        if not self.notes:
            return Phrase()
        
        central_pitch = self.notes[0].pitch
        inverted_notes = [Note(2 * central_pitch - note.pitch) for note in self.notes]
        for i in range(len(inverted_notes)):
            self.notes[i].show()
            inverted_notes[i].show()
        return Phrase(inverted_notes)
    
    def transpose(self, interval):
        transposed_notes = [Note((note.pitch + interval) % 12) for note in self.notes]
        return Phrase(transposed_notes)
    
    def retrograde(self):
        retrograded_notes = self.notes[::-1]
        return Phrase(retrograded_notes)

    def retrograde_inversion(self):
        return self.retrograde().inversion()

    def add_note(self, note):
        self.notes.append(note)

    def show(self):
        for i in self.notes:
            i.show()