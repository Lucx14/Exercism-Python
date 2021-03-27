class School:
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        # self.students[grade].append(name)
        # return self.students[grade]

        self.students.append((grade, name))

    def roster(self):
        # sorted_students = [
        #     sorted(self.students[i]) for i in range(1, len(self.students))
        # ]

        # return [student for grade in sorted_students for student in grade]

        return [name for _, name in sorted(self.students)]

    def grade(self, grade_number):
        # return sorted(self.students[grade_number])

        return sorted([name for grade, name in self.students if grade == grade_number])
