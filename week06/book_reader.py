# Have your program open the file, 

# read through it line by line, strip

# off leading and trailing whitespace

# and display each book to the screen.

with open("week06\\books.txt") as book_files:
    for line in book_files:
        line = line.strip()
        print(line)