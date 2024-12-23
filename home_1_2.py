import random

class Student:
    def __init__(self, name, surname,group_num):
        self.name = name
        self.surname = surname
        self.group_number = group_num
        self.courses_in_progress = []
        self.grades = {}
    def lector_rate(self, lector, course):
        sum = 0
        chet = 0
        if isinstance(lector, Lecturer) and course in lector.courses_lectures and course in self.courses_in_progress:
            mark_st = int(random.randint(1, 10))
            if course in lector.lector_grades:
                lector.lector_grades[course] += [mark_st]
                sum +=mark_st
                chet += 1
            else:
                lector.lector_grades[course] = [mark_st]
                sum += mark_st
                chet += 1
        else:
            pass

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_lectures = []
        self.lector_grades = {}

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_chek = []
        self.groups_number = []
    def rate_hw(self, student, course):

        if isinstance(student, Student) and course in self.courses_chek and student.group_number in self.groups_number and course in student.courses_in_progress:
            grade = int(random.randint(1, 10))
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            pass



student_1 = Student('Ivan', 'Ivanov', group_num= 13)
student_1.courses_in_progress += ['Python']

student_2 = Student(name='Olga', surname='Svetikova', group_num=12)
student_2.courses_in_progress += ['C++','Python', 'Marketing']

mentor_1 = Mentor('Oleg', 'Petrov')
mentor_1.courses_attached += ['Python', 'Java', 'C++']

mentor_2 = Reviewer (name='Mixail',surname='Simagin')
mentor_2.courses_chek += ['Python', 'Marketing']
mentor_2.groups_number += [12, 13]

mentor_3 = Lecturer(name='Danil',surname='Golotsin')
mentor_3.courses_lectures += ['Python', 'C++']


mentor_2.rate_hw(student_1, 'Python')
mentor_2.rate_hw(student_1, 'Java')
mentor_2.rate_hw(student_1, 'Marketing')

mentor_2.rate_hw(student_2, 'C++')
mentor_2.rate_hw(student_2, 'Marketing')
mentor_2.rate_hw(student_2, 'Python')

student_1.lector_rate(mentor_3,course='Python')
student_1.__str__()

print(mentor_2.name, mentor_2.surname, mentor_2.courses_chek, mentor_2.groups_number)
print(student_1.name, student_1.surname, student_1.group_number, student_1.grades,sep = '  ')
print(student_2.name, student_2.surname, student_2.group_number, student_2.grades, sep = '  ')
print()
print(mentor_3.name, mentor_3.surname, mentor_3.courses_lectures, mentor_3.lector_grades, sep = '  ')
print(student_1.name, student_1.surname, sep = '  ')
