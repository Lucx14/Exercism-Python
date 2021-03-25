STUDENTS = (
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Fred",
    "Ginny",
    "Harriet",
    "ILeana",
    "Joseph",
    "Kincaid",
    "Larry",
)

PLANTS = {"R": "Radishes", "C": "Clover", "G": "Grass", "V": "Violets"}


class Garden:
    def __init__(self, diagram, students=STUDENTS):
        self.students = sorted(students)
        self.sorted_plants = Garden.sort_plants(diagram)

    def plants(self, student):
        return [[PLANTS[p] for p in group] for group in self.sorted_plants][
            self.students.index(student)
        ]

    @staticmethod
    def sort_plants(diagram):
        rows = [
            [row[i : i + 2] for i in range(0, len(row), 2)]
            for row in diagram.split("\n")
        ]
        return ["".join(pots) for pots in zip(rows[0], rows[1])]
