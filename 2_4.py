str = 'hello12hi65go0'
new_str = ''
for i in range(len(str)):
    if(str[i].isdigit()):
        new_str += str[i]
    
print(new_str)