'''
5.2 Write a program that repeatedly prompts a user for integer numbers until the
user enters 'done'. Once 'done' is entered, print out the largest and smallest
of the numbers. If the user enters anything other than a valid number catch it
with a try/except and put out an appropriate message and ignore the number.'''

largest=-1
smallest=None

while True:
    inp=input("Enter a number:")
    if inp=='done':
        break
    try:
        num=int(inp)
        #print('Fine!')
    except:
        print('Invalid input')
        continue
    if num > largest:
        largest=num
    if smallest is None or num < smallest:
        smallest = num
print('Maximum is',largest)
print('Minimum is',smallest)
