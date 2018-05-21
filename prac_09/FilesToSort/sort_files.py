import shutil
import os

def main():
    file_types = {}
    for file in os.listdir('.'):
        if file == 'sort_files.py' or file == 'temp':
            continue
        else:
            file_type = file.split('.')[1]
            print(file_type)
            print(file_types)
            if file_type in file_types:
                file_folder = file_types[file_type]
                print(file_folder)
            else:
                file_folder = input('What category would you like to sort "{}" files into?'.format(file_type))
                file_types[file_type] = file_folder
                if os.path.exists(file_folder) is False:
                    os.mkdir(file_folder)
            shutil.move(file, file_folder)
    print('All files sorted')

main()