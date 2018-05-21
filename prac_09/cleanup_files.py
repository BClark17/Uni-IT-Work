
import shutil
import os


def main():
    print("Current directory is", os.getcwd())
    for filename in os.listdir('Lyrics'):
        print(os.listdir('Lyrics'))
        if filename == 'Temp':
            continue
        else:
            print(filename)
            print('Files in the directory >>> {}'.format('Lyrics/' + filename))
            for sub_file in os.listdir('Lyrics/' + filename):
                sub_file_location = os.getcwd() + '/' + 'Lyrics' + '/' + filename + '/' + sub_file
                print(sub_file_location)
                if os.path.exists(sub_file_location):
                    shutil.move(sub_file_location, os.getcwd() + '/' + 'Lyrics' + '/' + filename + '/' +
                                get_fixed_filename(sub_file))


def get_fixed_filename(filename):
    new_name = ""
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    for i, char in enumerate(filename, 0):
        if i == 0 or filename[i-1] == '_' or filename[i-1] == '(':
            new_name += char.upper()
        elif char.isupper() and filename[i-1] != '_' or char == '(':
            new_name += ('_' + char)
        else:
            new_name += char
    return new_name

main()
