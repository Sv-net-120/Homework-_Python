# Домашнее задание к лекции "Объекты и классы. Инкапсуляция, наследование и полиморфизм

Задание № 1, Задание №2
фаил home_1_2.py

Фаил homework_full.py включает в себя решение заданиий 1,2,3,4 с примерами по каждому классу для проверки функций
отправлен в GitHub 25.12.2024

Уважаемый Александр!
Прочла ваши замечания к работе homework_full.py и позволю с Вами не согласиться.
В коде есть несколько функций, которые выполняют указанную в вашем комментарии задачу,
в частности:
1. class Students:
   def aver_student_grades(self,course)
   вызывается: student_2.aver_student_grade(course = ['Python', 'C++'])
   как результат наполняется словарь student{course: aver_grade}
   это средние оценки исследуемого студента по вмем курсам, которые он изучает

   def merge_grades(self,*aver_student_grades)
   вызывается: student_1.merge_grades(student_2.aver_grades)
   как результат наполняется словарь aver_result{course: value}
   это средняя оценка от всех студентов по исследуемому курсу.

2. Аналогично представлены две функции в class Lecturer(Mentor):
   def aver_lector_marks(self, course)
   def merge_mark(self, *aver_marks):

Дополнительно, при описании класса, по каждому классу считается число созданных 
объектов: студентов и лекторов
Далее словарям, в которые собираются сведения по каждому студенту и лектору об 
их средних оценках присваиваются статус глобальных, чтобы они передавались словарями,
в функции, которые получают уже средние оценки по курсам у студентов и лекторов. 

В качестве экземпляров при тестировании кода было создано по три объекта студентов и 
лекторов. По два объекта оставлено в соответствии с требованиями к выполнению дз.

В качестве подтверждения работоспособности кода позволю себе дополнить
 задание полученными результатами по представленным объектам
            


