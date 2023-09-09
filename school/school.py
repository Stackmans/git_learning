class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.classes = []
        # self.teachers = []

    def check_student_in_school(self, student_obj):
        for school_class in self.classes:
            for student in school_class.students:
                if student == student_obj:
                    return True
        return False

    # def get_teachers_in_school(self):
    #     return self.teachers
    #
    # def check_teachers_in_school(self, teacher_obj):
    #     for teacher in self.teachers:
    #         if teacher == teacher_obj:
    #             return teacher
    #     print('Teacher not found')

    def add_class(self, new_class):
        self.classes.append(new_class)

    def del_class(self, class_to_del):  # try
        if class_to_del in self.classes:
            self.classes.remove(class_to_del)
            print(f'{class_to_del.class_name} removed')
        else:
            print(f'{class_to_del.class_name} not found in the {self.school_name}.')

    def add_student(self, class_obj, student):
        for school_class in self.classes:
            if school_class == class_obj and not self.check_student_in_school(student):
                school_class.students.append(student)
                print(f'student has been added in class: {school_class}')
        print(f"Class '{class_obj}' not found in the school or student in school.")

    def del_student(self, class_name, student_obj):
        for school_class in self.classes:
            if school_class.class_name == class_name:
                school_class.students.remove(student_obj)
                return f"Student '{student_obj.name}' removed from class '{class_name}'."
            else:
                return 'Student not found.'

    def get_classes_count(self):  # prop
        return len(self.classes)

    def get_classes(self):
        return self.classes

    def get_school_students_count(self):  # prop
        total_students = 0
        for school_class in self.classes:
            total_students += school_class.get_class_students_count()
        return total_students


class Classroom:
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []
        self.subjects = []

    def __repr__(self):
        return f"Class(class_name='{self.class_name}', students={len(self.students)}, subjects={self.subjects})"

    # TODO properties try
    def get_class_students_count(self):  # prop
        return len(self.students)

    def get_class_students(self):  # prop
        return self.students

    def add_subject(self, subject, hours):
        for existing_subject in self.subjects:
            if existing_subject['subject'] == subject:
                print(f"Subject '{subject}' already exists.")
                return
        self.subjects.append({'subject': subject, 'hours': hours})

    def del_subject(self, subject):
        for existing_subject in self.subjects:
            if existing_subject['subject'] == subject:
                self.subjects.remove(existing_subject)
                print(f"Subject '{subject}' removed from class.")
                return
        print(f"Subject '{subject}' not found in the class.")

    def get_subjects(self):
        return self.subjects


# class Teacher:  # salary, add t, del, get
#     def __init__(self, name, age, sex, main_subject):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.main_subject = main_subject
#
#     def __repr__(self):
#         return f"(Teacher name: '{self.name}', age: {self.age}, sex: '{self.sex}, main_subject: {self.main_subject}')"


class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.subjects = dict()  # переробити під список

    def __repr__(self):
        return f"Student name: '{self.name}', age: {self.age}, sex: '{self.sex}'"

    def add_subject_hours(self, subject, hours):
        if subject in self.subjects:
            self.subjects[subject]['hours'] += hours
        else:
            self.subjects[subject] = {'hours': hours, 'marks': [], 'skips': 0}

    # -----SKIPS------------------------------------------------------------------------------------

    def plus_subject_skips(self, subject, count):
        if subject in self.subjects.keys():
            self.subjects[subject]['skips'] += count
        else:
            print(f'Subject {subject} not found.')

    def set_subject_skips(self, subject, count):
        if subject in self.subjects:
            self.subjects[subject]['skips'] = count
        else:
            print(f"Subject: {subject} not found.")

    def get_student_skips(self, subject):
        if subject in self.subjects:
            skips = self.subjects[subject]['skips']
            return f"Student has {skips} skips for subject: {subject}"
        else:
            return f"Subject '{subject}' not found in student's records."

    def get_all_skips(self):
        count = 0
        for subject, info in self.subjects.items():
            count += info['skips']
        return count

    def get_all_subject_skips(self):
        for subject, info in self.subjects.items():
            skips = info['skips']
            print(f"Student has {skips} skips for subject: {subject}")

    # ---------------------------------------------------------------------------------------------------------------------

    def del_subject(self, subject):
        if subject in self.subjects:
            self.subjects.pop(subject)
            print(f"Subject: {subject} removed from student records.")
        else:
            print(f"Subject: {subject} not found.")

    # def get_subjects(self):
    #     return list(self.subjects.keys())

    def get_grade_point_average(self, subject):
        if len(self.subjects[subject]['marks']) == 0:
            print('there are no marks')
        elif subject in self.subjects:
            return round(sum(self.subjects[subject]['marks']) / len(self.subjects[subject]['marks']), 1)
        else:
            print(f'Subject {subject} not found.')

    def get_subjects(self):
        return self.subjects

    def set_hours(self, subject, hours):  # ?
        if subject in self.subjects:
            self.subjects[subject]['hours'] = hours
        else:
            print(f"Subject: {subject} not found.")

    def add_mark(self, subject, mark):
        if subject in self.subjects:
            self.subjects[subject]['marks'].append(mark)
        else:
            print(f"Subject: {subject} not found.")

    def get_marks(self, subject):
        if subject in self.subjects:
            return self.subjects[subject]['marks']
        else:
            print(f"Subject: {subject} not found.")
            return []


class Subject:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"


math = Subject("Math")
physics = Subject("Physics")
chemistry = Subject("Chemistry")

gymnasium = School("Gymnasium")
class_A = Classroom("Class A")
class_B = Classroom("Class B")
class_C = Classroom("Class C")
gymnasium.add_class(class_A)
gymnasium.add_class(class_B)

student1 = Student("Alice Willy", 15, "female")
student2 = Student("Bob Cat", 16, "male")
student3 = Student("Kob Bok", 16, "male")
# student4 = Student("Kob Bok", 16, "male")  # check
# student4 = student3 # check
student4 = Student("Gabimaru", 20, "transgender")

gymnasium.add_student("Class A", student1)
gymnasium.add_student("Class A", student2)
gymnasium.add_student("Class B", student3)
# gymnasium.add_student("Class B", student4)
# gymnasium.del_student("Class A", student2)

student1.add_subject_hours(math, 3)
student1.add_subject_hours(physics, 2)
student1.plus_subject_skips(math, 1)
student1.plus_subject_skips(physics, 1)
############################
# student1.add_mark(math, 10)
# student1.add_mark(math, 8)
# student1.add_mark(math, 10)
# student1.add_mark(math, 7)

# student1.set_hours(physics, 1)
# student1.del_subject(math)

# student2.add_subject_hours(math, 5)
# student2.add_subject_hours(physics, 5)
# student3.add_subject_hours(chemistry, 5)
# student3.add_subject_hours(physics, 5)

class_A.add_subject(math, 5)
class_A.add_subject(physics, 5)
# class_A.del_subject(physics)

# class_B.add_subject(math, 5)
# class_B.add_subject(physics, 5)
# gymnasium.del_class(class_B)

# print(f"Total students in class A: {class_A.get_class_students_count()}")
# print(f"Total students in class B: {class_B.get_class_students_count()}")
# print()
# print(f"Total students in the school: {gymnasium.get_school_students_count()}")

# print(student1.get_marks(math))

# print(student1.get_student_skips(math))
# print(student1.get_all_skips())
print(student1)
print(student1.get_subjects())
print(student1, student1.get_subjects())
# print(student1.get_grade_point_average(math))
# print(class_A.get_subjects())
# print(class_A.get_class_students())
# print(gymnasium.check_student_in_school(student3))