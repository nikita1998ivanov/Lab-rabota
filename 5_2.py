import csv

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

print(my_list)

