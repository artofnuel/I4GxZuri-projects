# This will allow python receive and then read a file
# Ps. I always start a new document to screen out possible confusion from the instructions. Hope that's okay.

def read_file(file):
    file = open(input("What is your file or path:  "))
    return file.read()

# This creates a dictionary from said file

def c_word():
    text = read_file("")

    c_word = dict()
    w_word = text.split()

    for word in w_word:
        if word in c_word:
            c_word[word] += 1
        else:
            c_word[word] = 1
            

    return c_word

print (c_word())