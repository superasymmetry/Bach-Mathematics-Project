import winsound

class note:
    def __init__(self, pitch):
        self.pitch = pitch

    def play(self, duration):
        winsound.Beep(self.pitch, duration)

class phrase:
    def __init__(self, notes):
        self.notes = []

    def play(self):
        for i in self.notes:
            i.play(self)