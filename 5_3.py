import csv

def get_struct():
    my_list = []
    with open("students.csv") as f:
        next(f)
        for line in f:
            temp = []
            h, nm, a, db = line.split(";")
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
        i[2] = t + 1


def menu(my_list):
    while True:
        print("1) увеличить возраст всех студентов на один")
        print("2) Вывести студентов")
        print("3) Exit")
        select = int(input("ответ: "))
        if select == 1:
            add_one(my_list)
        elif select == 2:
            print(my_list)
        elif select == 3:
            return "EXIT"


my_list = get_struct()
menu(my_list)

