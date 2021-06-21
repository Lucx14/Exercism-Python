CHROMATIC_SHARP = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
CHROMATIC_FLAT = ["F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E"]

FLAT_TONICS = ["F", "Bb", "Eb", "g", "d", "Db"]
SHARP_TONICS = ["C", "F#", "A", "G", "f#", "a"]

MOVES = {"M": 2, "m": 1, "A": 3}


class Scale:
    def __init__(self, tonic):
        self.tonic = tonic
        self.base_scale = self.fetch_base_scale()

    def chromatic(self):
        i = self.base_scale.index(self.upper_tonic())
        return self.base_scale[i:] + self.base_scale[0:i]

    def interval(self, intervals):
        count = 0
        indexes = []
        for interval in intervals:
            indexes.append(count)
            count += MOVES[interval]

        return [self.chromatic()[i] for i in indexes]

    def upper_tonic(self):
        if len(list(self.tonic)) == 1:
            return self.tonic.upper()

        note, variation = list(self.tonic)
        return "".join([note.upper(), variation])

    def fetch_base_scale(self):
        if self.tonic in SHARP_TONICS:
            return CHROMATIC_SHARP
        return CHROMATIC_FLAT
