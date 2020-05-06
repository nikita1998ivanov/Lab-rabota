my_string = """Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса"""
 
ls = my_string.split(';_')

fio, name, sername, age, cat = ls[0].split(';')
print(fio,name,sername,'\t\t\t', cat, '\t\t',age)
 
for i in ls[1:]:
    fio, name, sername, age, cat = i.split(';')
    print(fio,name,sername,'\t', cat,'\t', age)
