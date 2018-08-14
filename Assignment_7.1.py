'''7.1 Write a program that prompts for a file name, then opens that file
and reads through the file, and print the contents of the file in upper case.
Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt'''

file = input('Enter a file name: ')
try:
    fhand = open(file)
except:
    print('Cannot open',file)
    quit()
for line in fhand:
    line = line.rstrip()
    inp = fhand.read()
    print(inp.upper())
