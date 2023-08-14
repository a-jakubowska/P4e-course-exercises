fname=open('zadanie_9.4.txt')
count=dict()
for line in fname:
    line= line.rstrip()
    #print(line)

    if line.startswith('From '):
        str = line.split()
        hour=str[5]
        #print(hour)

        h= hour.split(':')
        #print(h)

        k=h[0]
        #print(k)
        #print(type(k))


        count[k]=count.get(k,0)+1
#print(count)

for key, val in sorted(count.items()):
    print(key, val)
