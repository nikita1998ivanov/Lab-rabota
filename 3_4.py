s1 = 'helloooo wolrd! how are youuuu? ...'
s2 = ' ,:!.?'

length = len(s1) 
for i in s2:
    s1 = s1.replace(i, ' ')
s1 = list(filter(None, s1.split()))

count = 0
for item in s1:
    count += 1

print('Кол-во симвлов: ', length)
print('Кол-во слов: ', count)