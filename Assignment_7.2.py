# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
sum = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print(line)
    count += 1
    n = line.find('0.',20)
    x = float(line[n:])
    sum = (sum + x)
#print(c)
print('Average spam confidence:',(s/c))
#print("Done")
