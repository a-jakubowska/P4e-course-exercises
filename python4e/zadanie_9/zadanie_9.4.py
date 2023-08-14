#name = input("Enter file:")
#if len(name) < 1:
#    name = "mbox-short.txt"
#handle = open(name)

fname=open('zadanie_9.4.txt')
count= dict()


for line in fname:
    line= line.rstrip()
    #print(line)

    if line.startswith('From '):
        str = line.split()

        #print (line)

        #print (str[1])

        lista=list()
        lista.append(str[1])

        #print (lista)

        for name in lista:
            count[name]=count.get(name,0)+1

#print(count)

bigcount= None
bigword=None

for word, n in count.items():
    if bigword is None or n > bigcount:
        bigword = word
        bigcount = n

print(bigword, bigcount)
