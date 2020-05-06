users = {'1': ['Aшков Илья Петрович', '24', 'БО-222222'], '2': ['Иванов Иван Иванович', '23', 'БО-111111'], '3': ['Сидоров Семен Семенович', '24', 'БО-222222']}
number = input('number: ')
name = input('name: ')
age = input('age: ')
group = input('group: ')
l = []
l.append(name)
l.append(age)
l.append(group)
users[number] = l

print(users)
