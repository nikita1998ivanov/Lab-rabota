import random

alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
str = ''
for i in range(5):
    a = random.randint(0,len(alphabet))
    str += alphabet[a]
    
print(str)