lst = [[1, 'Иванов И.И.', 19, '777'], [2, 'Пупкин С.Д.', 24, '666'], [3, 'Васильев А.Р.', 20, '444']]
students = {}

for student in lst:
    students[student[0]] = [student[1], student[2], student[3]]


fio = input('Введите ФИО студента: ')
student_num = None
for student in students:
    if students[student][0] == fio:
        student_num = student

if student_num is not None:
    students[student_num][1] += 1
    student_num = None
else:
    print('Студент с ФИО "{}" не найден'.format(fio))

print(students)
