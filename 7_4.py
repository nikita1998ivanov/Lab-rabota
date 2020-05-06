d = {}
with open("students.csv") as f:
    next(f)
    for line in f:
        h, nm, a, db = line.split(";")
        d.setdefault(int(h), []).append((nm, int(a), db))
l = d.values()
l = list(l)
l.sort()
print(l)

def t():
    count = 0
    while True:
        print("Для увеличения возраста всех студентов, введите: age++")
        print("Чтобы сохранить, введите: save")
        print("Чтобы выйти, введите: quit")

        command = input()

        if command == "age++":
            count += 1
            for i in range(len(l)):
                for j in range(len(l[i])):
                    for k in range(len(l[i][j])):
                        if(k == 1):
                            print(l[i][j][k] + count)
                        else:
                            print(l[i][j][k])

        elif command == "save":
            with open("students.csv", 'w') as f:
                f.write('№;ФИО;Возраст;Группа\n')
                for i in range(len(l)):
                    f.write('%s\n' % l[i])
            print("Успешно сохранено!\n")

        elif command == "quit":
            break

        else:
            print("Команда не верна.\n")


t()
