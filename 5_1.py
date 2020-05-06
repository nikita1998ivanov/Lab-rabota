import os.path
path = '.'
num_files = len([f for f in os.listdir(path)
                   if os.path.isfile(os.path.join(path, f))])
print('Кол-во файлов: ',num_files)