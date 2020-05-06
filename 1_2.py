my_list = [1, 2, 'hi', 4 , 'ok', 5]
for i in my_list:
    if(str(i).isdigit()):
        if(i % 2 == 0):
            print(i)