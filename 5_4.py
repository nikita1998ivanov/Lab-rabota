import csv

def get_struct():
    my_list = []
    with open("students.csv") as f:
        next(f)
        for line in f:
            temp = []
            h, nm, a, db = line.split(";")
            db = db[:-1]
            temp.append(h)
            temp.append(nm)
            temp.append(a)
            temp.append(db)
            my_list.append(temp)
    my_list.sort()
    return my_list


def add_one(my_list):
    for i in my_list:
        t = int(i[2])
        i[2] = str(t + 1)
    return my_list


def save_in_file(my_list):
    with open("students.csv", 'w') as f:
        f.write('№;ФИО;Возраст;Группа\n')
        for i in range(len(my_list)):
            str = ''
            for j in range(len(my_list[i])):
                str += my_list[i][j]
                if(j != (len(my_list[i])-1)):
                    str += ";"
            print('%s' % str)
            f.write('%s\n' % str)


def menu():
    my_list = []
    while True:
        print("1) увеличить возраст всех студентов на один")
        print("2) Вывести студентов")
        print("3) Сохранить в файл")
        print("4) Exit")
        select = int(input("ответ: "))
        if select == 1:
            my_list = add_one(my_list)
        elif select == 2:
            my_list = get_struct()
            print(my_list)
        elif select == 3:
            save_in_file(my_list)
        elif select == 4:
            return "EXIT"


menu()

