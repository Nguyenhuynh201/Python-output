FILENAME = 'book.txt'
READ_MODE = 'r'

with open(FILENAME, READ_MODE) as names_file:
        lines = names_file.readlines()
        print(lines)
