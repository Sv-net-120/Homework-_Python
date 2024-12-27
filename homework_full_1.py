# Create class Student.

class Student:

    counter = 0
    def __init__(self, name, surname, group_num):

        self.name = name
        self.surname = surname
        self.group_number = group_num
        self.courses_in_progress = []
        self.grades = {}
        self.aver_grades ={}
        Student.counter += 1

    # Put rate to mentors.
    def lector_rate(self, lector, course, grade):

        if isinstance(lector, Lecturer) and course in lector.courses_lectures and course in self.courses_in_progress:
            if course in lector.lector_grades:
                lector.lector_grades[course] += [grade]
            else:
                lector.lector_grades[course] = [grade]

    #  Find average grades for student
    def aver_student_grade(self, course):

        for course, grade in self.grades.items():
            self.aver_grades[course] = sum(grade)/len(grade)

# Find average grades at course for all students.
    def merge_grades(self, *aver_grades):

        global aver_result
        aver_result = self.aver_grades
        count  = 1
        for grades_student in aver_grades:
            for key, value in grades_student.items():
                if key in aver_result:
                    aver_result[key] += value
                    count += 1
                else:
                   aver_result[key] = value

                if count > 1:
                    aver_result[key] = round((aver_result[key] / Student.counter), 1)
                else:
                    aver_result[key] = value

        print(f'Средняя оценка за домашнее задание по курсу : {aver_result}')
        print()

    #   Print information about student.
    def __str__(self):

        return(f" Имя: {self.name}\n Фамилия: {self.surname}\n"
               f" Средняя оценка за домашнее задание: {self.aver_grades})\n"
               f" Курсы в процесс изучения: {", ".join(self.courses_in_progress)}\n Завершенные курсы: Введение в программирование\n")

    # Compare average grades of students with average grade of course.
    def __eq__(self, other):
        if self.aver_grades.get(course):
            return self.aver_grades[course] == aver_result[course]
        else:
            print(f'Такого курса в программе студента {self.name} {self.surname} нет\n')

# Create class Mentor and two subclasses: Lecturer and Reviewer.
class Mentor:

    def __init__(self, name, surname):

        self.name = name
        self.surname = surname
        self.courses_attached = []

    # Print informatiom about mentors.
    def __str__(self):

        return (f" Преподаватель:\n Имя: {self.name} \n Фамилия: {self.surname}: "
                f" читает курсы: {', '.join(self.courses_attached)} \n")

class Lecturer(Mentor):

    count_lectors = 0
    def __init__(self, name, surname):

        super().__init__(name, surname)
        self.courses_lectures = []
        self.lector_grades = {}
        self.aver_marks= {}
        Lecturer.count_lectors +=1

    # Find average marks for lectors.
    def aver_lector_marks(self, course):

        for course, marks in self.lector_grades.items():
            self.aver_marks[course] = sum(marks)/len(marks)

    #   Print informatiom about lectors.
    def __str__(self):

        return f' Имя: {self.name} \n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.aver_marks}'

    # Find average  marks for lectures for all lectors.
    def merge_mark(self, *aver_marks):
        global aver_lec_result
        aver_lec_result = self.aver_marks
        count  = 1
        for marks_lector in aver_marks:
            for key, value in marks_lector.items():
                if key in aver_result:
                    aver_lec_result[key] += value
                    count += 1
                else:
                   aver_lec_result[key] = value

                if count > 1:
                    aver_lec_result[key] = round((aver_lec_result[key] / Lecturer.count_lectors), 1)
                else:
                    aver_lec_result[key] = value
        print(f'Средние оценки студентов за лекции: {aver_lec_result}\n')

    # Compare average marks for lectors.
    def __eq__(self, other):
        if self.aver_marks.get(course):
            return self.aver_marks[course] == aver_lec_result[course]
        else:
            print(f'Лектор {self.name} {self.surname} не читает курс: {course}\n')


class Reviewer(Mentor):

    def __init__(self, name, surname):

        super().__init__(name, surname)
        self.courses_chek = []
        self.groups_number = []

    #  Put grades for students' homeworks.
    def rate_hw(self, student, course, grade):

        if (isinstance(student, Student) and course in self.courses_chek
                and student.group_number in self.groups_number and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]

# Create examples for each class and chek up code.
# Students:
student_1 = Student(name='Ludmila', surname='Lubimova', group_num= 10)
student_1.courses_in_progress += ['Python', 'C++', "Java", 'Marketing']

student_2 = Student(name='Sofa', surname='Svetikova', group_num=12)
student_2.courses_in_progress += ['C++','Python', 'Marketing', 'Java']

# Mentors:
mentor_1 = Mentor(name='Mixail',surname='Simagin')
mentor_1.courses_attached +=['Pyton', 'C++', 'Marketing']
mentor_2 = Mentor(name='Mixail', surname='Petrov')
mentor_2.courses_attached += ['Python', 'Java', 'C++', 'Marketing']

print(mentor_1, mentor_2, sep='\n')

# Mentors chek up homeworks:
mentor_1 = Reviewer (name='Mixail',surname='Simagin')
mentor_1.courses_chek += ['C++', 'Java', 'Marketing', 'Python']
mentor_1.groups_number += [10, 12]

mentor_1.rate_hw(student_1, course='C++', grade= 10)
mentor_1.rate_hw(student_1, course='C++', grade= 8)
mentor_1.rate_hw(student_1, course='Marketing', grade=5)

student_1.aver_student_grade(course = ['C++', 'Marketing'])

mentor_1.rate_hw(student_2, course='C++',grade= 7)
mentor_1.rate_hw(student_2, course='Python', grade= 6)

student_2.aver_student_grade(course = ['Python', 'C++'])

mentor_2 = Reviewer (name='Mixail', surname='Petrov')
mentor_2.courses_chek += ['Python', 'Marketing', 'C++', 'Java']
mentor_2.groups_number += [12, 13]

mentor_2.rate_hw(student_1, course='Python',grade= 5)
mentor_2.rate_hw(student_1, course='Python', grade= 6)

mentor_2.rate_hw(student_2, course='Python', grade= 7)
mentor_2.rate_hw(student_2, course='Python', grade= 8)

student_1.merge_grades(student_2.aver_grades)
print(student_1.aver_grades['Python'] == aver_result['Python'])
print(student_2.aver_grades['C++'] == aver_result['C++'])
print()
print('Оценки студента за домашнее задание', student_1, sep='\n')
print('Оценки студента за домашнее задание', student_2, sep='\n')


# Mentors reads lectures:
mentor_1 = Lecturer(name='Mixail',surname='Simagin')
mentor_1.courses_lectures += ['Python', 'C++']

student_1.lector_rate(mentor_1,course='Python', grade= 10)
student_1.lector_rate(mentor_1,course='C++', grade=  8)

student_2.lector_rate(mentor_1,course='Python',grade= 9)
student_2.lector_rate(mentor_1,course='C++', grade= 7)

mentor_1.aver_lector_marks(course=['Python', 'C++'])

mentor_2 = Lecturer(name='Mixail', surname='Petrov')
mentor_2.courses_lectures += ['Python', 'C++']

student_1.lector_rate(mentor_2,course='Python', grade= 9)
student_1.lector_rate(mentor_2,course='Python', grade= 8)
student_1.lector_rate(mentor_2,course='C++', grade= 7)
student_1.lector_rate(mentor_2,course='C++', grade= 6)

student_2.lector_rate(mentor_2,course='Python', grade= 10)
student_2.lector_rate(mentor_2,course='Python', grade= 5)
student_2.lector_rate(mentor_2,course='C++', grade= 4)
student_2.lector_rate(mentor_2,course='C++', grade= 3)

mentor_2.aver_lector_marks(course=['Python', 'C++'])

mentor_1.merge_mark(mentor_2.aver_marks)

print(mentor_1.aver_marks['Python'] == aver_lec_result['Python'])
print(mentor_2.aver_marks['C++'] == aver_lec_result['C++'])
print()
print('Оценки преподавателю за лекции:', mentor_1, sep = '\n')
print()
print('Оценки преподавателям за лекции:', mentor_2, sep = '\n')

# Преподаватель:
#  Имя: Mixail
#  Фамилия: Simagin:  читает курсы: Pyton, C++, Marketing
#
#  Преподаватель:
#  Имя: Mixail
#  Фамилия: Petrov:  читает курсы: Python, Java, C++, Marketing
#
# Средняя оценка за домашнее задание по курсу : {'C++': 8.0, 'Marketing': 5.0, 'Python': 3.0}
#                           *****student_1.merge_grades(student_2.aver_grades)*****
# True
# False
#
# Оценки студента за домашнее задание - вызов mentor_1.rate_hw с различным набором аргументов
#  Имя: Ludmila
#  Фамилия: Lubimova
#  Средняя оценка за домашнее задание: {'C++': 8.0, 'Marketing': 5.0, 'Python': 3.0})
#                           ****student_1.aver_student_grade(course = ['C++', 'Marketing'])***
#  Курсы в процесс изучения: Python, C++, Java, Marketing
#  Завершенные курсы: Введение в программирование
#
# Оценки студента за домашнее задание
#  Имя: Sofa
#  Фамилия: Svetikova
#  Средняя оценка за домашнее задание: {'C++': 7.0, 'Python': 6.0})
#  Курсы в процесс изучения: C++, Python, Marketing, Java
#  Завершенные курсы: Введение в программирование
#
# Средние оценки студентов за лекции: {'Python': 8.8, 'C++': 6.2}
#                               ****mentor_1.merge_mark(mentor_2.aver_marks)****
#
# True
# False
#
# Оценки преподавателю за лекции: mentor_1.aver_lector_marks(course=['Python', 'C++'])
#  Имя: Mixail
#  Фамилия: Simagin
#  Средняя оценка за лекции: {'Python': 8.8, 'C++': 6.2}
#
# Оценки преподавателям за лекции:
#                   *****mentor_2.aver_lector_marks(course=['Python', 'C++'])*****
#  Имя: Mixail
#  Фамилия: Petrov
#  Средняя оценка за лекции: {'Python': 8.0, 'C++': 5.0}

