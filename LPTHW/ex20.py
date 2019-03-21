from sys import argv

script, input_file = argv
# read the files and return it into a string
def print_all(f):
    print f.read()
# start from the beginning
def rewind(f):
    f.seek(0)
# prints the line number and then prints the line
def print_a_line(line_count, f):
    print line_count, f.readline()
# loads the current file
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)