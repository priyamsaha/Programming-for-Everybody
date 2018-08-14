'''
9.4 Write a program to read through the mbox-short.txt and figure out who
has the sent the greatest number of mail messages. The program looks for
'From ' lines and takes the second word of those lines as the person who sent
the mail. The program creates a Python dictionary that maps the sender's mail
address to a count of the number of times they appear in the file. After the
dictionary is produced, the program reads through the dictionary using a maximum
loop to find the most prolific committer.
'''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
counts = dict()
for line in fh:
    if line.startswith('From:'):
        word = line.split();
        counts[word[1]] = counts.get(word[1],0)+1


largest = None
theword = None
for k,v in counts.items():
    if largest is None or v>largest:
        largest = v
        theword = k
print(theword,largest)










'''name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
res={}
for line in handle:
    temp_list=[]
    if line.startswith('From'):
        temp_list=line.split()
        res[temp_list[1]]=res.get(temp_list[1],0)+1
maximum=res.values()
max_val=max(maximum)
for i,j in res.items():
    if j==max_val:
        print(i,str(int(j/2)))'''
