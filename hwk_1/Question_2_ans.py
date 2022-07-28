class Student:

    def __init__(self, name, age, id, subject_grade):
        self.name = name
        self.age = age
        self.id = id
        self.subject_grade = subject_grade


# student_1 = Student('Emma', 25, 1234, {'Geography': 90})
#
# print(student_1.name)
# print(student_1.age)
# print(student_1.id)
# print(student_1.subject_grade)


class CFGStudent(Student):
    def __init__(self, stream, name, age, id, subject_grade):
        self.stream = stream
        super(CFGStudent, self).__init__(name, age, id, subject_grade)

    def add_subject(self, new_sub):
        self.new_sub = new_sub
        self.subject_grade.update(new_sub)

    def remove_subject(self, drop_sub):
        self.drop_sub = drop_sub
        self.subject_grade.pop(drop_sub)

    def view_subjects(self):
        subjects = self.subject_grade.keys()
        print(subjects)

    def ave_grades(self):
        list = []
        values = self.subject_grade.values()
        for grade in values:
            list.append(grade)
        overall_grade = sum(list)/len(list)
        print(overall_grade)


student_1 = CFGStudent('Software', 'Emma', 25, 1234, {'Geography': 90})
student_1.add_subject({'Python': 80})
print(student_1.subject_grade)
student_1.view_subjects()
student_1.ave_grades()
