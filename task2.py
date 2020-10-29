OUTPUT = 'summary.txt'
WRITE_MODE = 'w'
FILENAME = 'book.txt'
READ_MODE = 'r'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open(OUTPUT, WRITE_MODE) as output:
    #function to summarize letters 
    def summarize_letters(string):
        letters = []
        counts = []
        
        for letter in string.upper(): 
            if letter in ALPHABET:
                if letter in letters:
                    index = letters.index(letter)
                    counts[index] += 1
                else:
                    letters.append(letter)
                    counts.append(1)
            
        tuples = list(zip(letters, counts))
        tuples.sort()
        return tuples
    #read the txt file and run function
    with open(FILENAME, READ_MODE) as book:
        data = book.read()

    summary = summarize_letters(data)

    #display the count in each letter
    for char, count in summary:
        output.write(f'{char} {count}\n')

    # check if all letters of the alphabet are in the 
    all_letters = True

    if len(summary) == len(ALPHABET):
        for item in summary:
            if item[0] not in ALPHABET:
                all_letters = False
                break  
    else:
        all_letters = False

    if all_letters:
        output.write('It has all letters.\n')
    else:
        output.write('It does not have all letters.\n')