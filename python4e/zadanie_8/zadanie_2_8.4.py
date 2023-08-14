

#fname = input("Enter file name: ")
fname=open('zadanie_8.4.txt')

#fh = open(fname)
lst = list()

for line in fname:
    wers= line.rstrip()
    #print(wers)
    words=wers.split()
    #print(word)

    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
