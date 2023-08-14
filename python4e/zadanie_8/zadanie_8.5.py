#fname = input("Enter file name: ")
fh=open('zadanie_8.5.txt')

#if len(fname) < 1:
    #fname = "mbox-short.txt"

#fh = open(fname)

count = 0

for line in fh:
    line= line.rstrip()
#    print(line)

    if line.startswith('From '):
        line=line.split()
        print(line[1])
        count=count+1
#print (count)

print("There were", count, "lines in the file with From as the first word")
