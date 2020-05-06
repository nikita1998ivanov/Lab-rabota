s1 = 'helloooo wolrd! how are youuuu? ...'
s2 = ' ,:!.?'

for i in s2:
    s1 = s1.replace(i, ' ')
    
s1 = list(filter(None, s1.split()))
str = ''

for item in s1:
    if(len(item) > 5):
        str += item + ' '

print(str)