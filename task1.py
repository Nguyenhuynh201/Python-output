import os
OUTPUTFILE = 'log.txt'
WRITE_MODE = "w"
FILENAME = 'scores.txt'
READ_MODE = 'r'
total = 0
count = 0
with open(OUTPUTFILE, WRITE_MODE) as output:
    try:
        with open(FILENAME, READ_MODE) as names_file:
            for line in names_file:
                try:
                    name, score = line.split()
                    total = total + int(score)
                    count = count + 1 
                except ValueError as error:
                    output.write(f'Bad score value for {name},ignored.\n')      
            output.write(f'The class average is {total/count:.2f} for {count} students.\n')
    except OSError as error:
        output.write(f'{FILENAME} is not a valid file, error message: {error}\n')
    except IOError as error:
        output.write(f'IOError, error message: {error}\n')



