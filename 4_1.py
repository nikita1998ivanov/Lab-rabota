my_list = [[1,2,3],[4,5,6],[7,8,9]]

summ = 0

for i in range(len(my_list)):
    summ += sum(my_list[i])
    print(my_list[i])
    
print('sum = ',summ)