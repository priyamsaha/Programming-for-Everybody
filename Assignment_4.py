'''
4.6 Write a program to prompt the user for hours and rate per hour using input
to compute gross pay. Award time-and-a-half for the hourly rate for all hours
worked above 40 hours. Put the logic to do the computation of time-and-a-half
in a function called computepay() and use the function to do the computation.
The function should return a value.'''

def computePay(h,r):
    if h <=40:
        return (h*r)
    else:
        return (r * 40 + (r * 1.5) * (h - 40))

hour = float(input("Enter hours:"))
rate = float(input("Enter rate:"))
p = computePay(hour,rate)
print(p)
