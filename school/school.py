class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.classes = []

    def check_student_in_school(self, student_obj):
        for school_class in self.classes:
            for student in school_class.students:
                if student == student_obj:
                    return True
        return False

    def add_class(self, new_class):
        self.classes.append(new_class)

    def del_class(self, class_to_del):
        if class_to_del in self.classes:
            self.classes.remove(class_to_del)
            print(f'{class_to_del.class_name} removed')
        else:
            print(f'{class_to_del.class_name} not found in the {self.school_name}.')

    def add_student(self, student, school_class):
        if school_class in self.classes:
            school_class.students.append(student)
            print(f"{student.name} added to {school_class.class_name}")
        else:
            print(f"{school_class.class_name} not found in the {self.school_name}. Cannot add student.")

    def del_student(self, student, school_class):
        if school_class in self.classes and student in school_class.students:
            school_class.students.remove(student)
            print(f"{student.name} removed from {school_class.class_name}")
        else:
            print(
                f"{student.name} not found in {school_class.class_name} of {self.school_name}. Cannot remove student.")

    def get_classes_count(self):
        return len(self.classes)

    def get_classes(self):
        return self.classes

    def get_school_students_count(self):
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


class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.subjects = []

    def __repr__(self):
        return f"Student name: '{self.name}', age: {self.age}, sex: '{self.sex}'"

    def add_subject_hours(self, subject, hours):
        for sub_info in self.subjects:
            if sub_info['subject'] == subject:
                sub_info['hours'] += hours
                break
        else:
            self.subjects.append({'subject': subject, 'hours': hours, 'marks': [], 'skips': 0})

    # -----SKIPS------------------------------------------------------------------------------------

    def plus_subject_skips(self, subject, count):
        for sub_info in self.subjects:
            if sub_info['subject'] == subject:
                sub_info['skips'] += count
                return 'skips added'

        print(f"Subject '{subject}' not found.")

    def set_subject_skips(self, subject, count):
        for sub_info in self.subjects:
            if sub_info['subject'] == subject:
                sub_info['skips'] = count
                break
        else:
            print(f"Subject '{subject}' not found.")

    def get_student_skips(self, subject):
        for sub_info in self.subjects:
            if sub_info['subject'] == subject:
                skips = sub_info['skips']
                return f"Student has {skips} skips for subject: {subject}"
        else:
            return f"Subject '{subject}' not found in student's records."

    def get_all_skips(self):
        count = 0
        for sub_info in self.subjects:
            count += sub_info['skips']
        return count

    def get_all_subject_skips(self):
        skips_info = ""
        for sub_info in self.subjects:
            subject = sub_info['subject']
            skips = sub_info['skips']
            skips_info += f"Student has {skips} skips for subject: {subject}\n"
        return skips_info

    # ---------------------------------------------------------------------------------------------------------------------

    def del_subject(self, subject):
        for sub_info in self.subjects:
            if sub_info['subject'] == subject:
                self.subjects.remove(sub_info)
                print(f"Subject: {subject} removed from student records.")
                break
        else:
            print(f"Subject: {subject} not found.")

    def get_grade_point_average(self, subject):
        for sub_info in self.subjects:
            if sub_info['subject'] == subject:
                if len(sub_info['marks']) == 0:
                    print('There are no marks')
                else:
                    return round(sum(sub_info['marks']) / len(sub_info['marks']), 1)
        else:
            print(f"Subject: {subject} not found.")

    def get_subjects(self):
        return self.subjects

    def set_hours(self, subject, hours):
        for sub_info in self.subjects:
            if sub_info['subject'] == subject:
                sub_info['hours'] = hours
                break
        print(f"Subject: {subject} not found.")

    def add_mark(self, subject, mark):
        for sub_info in self.subjects:
            if sub_info['subject'] == subject:
                sub_info['marks'].append(mark)
                break
        else:
            print(f"Subject: {subject} not found.")

    def get_marks(self, subject):
        for sub_info in self.subjects:
            if sub_info['subject'] == subject:
                return sub_info['marks']
        else:
            print(f"Subject: {subject} not found.")
            return []


math = "Math"
physics = "Physics"
chemistry = "Chemistry"

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

gymnasium.add_student(student1, class_A)
gymnasium.add_student(student2, class_A)
gymnasium.add_student(student3, class_B)
# gymnasium.add_student("Class B", student4)
# gymnasium.del_student("Class A", student2)

student1.add_subject_hours(math, 3)
student1.add_subject_hours(physics, 2)
student1.plus_subject_skips(math, 1)
student1.plus_subject_skips(physics, 1)
############################
student1.add_mark(math, 10)
student1.add_mark(math, 8)
student1.add_mark(math, 10)
student1.add_mark(math, 7)

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
print(student1.get_all_subject_skips())

# print(student1.get_student_skips(math))
# print(student1.get_all_skips())
# print(student1)
# print(student1.get_subjects())
# print(student1, student1.get_subjects())
# print(student1.get_grade_point_average(math))
# print(class_A.get_subjects())
# print(class_A.get_class_students())
# print(gymnasium.check_student_in_school(student3))
