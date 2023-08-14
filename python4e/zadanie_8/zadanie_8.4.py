
romeoe=input("Enter file name: ")

#romeo=open('zadanie_8.4.txt')
imp=romeo.read()
x=imp
#print (x)


y=type(x)
#print(y)

line = x.split()
#print (line)


f=type(line)
#print(f)

line.sort()
#print(line)

del line[5:7]
#print (line)
del line[11:13]
#print (line)
del line[19:22]
#print (line)

a=len(line)
#print(a)
#print(line[25])

del line[25]

line.append("But")

line.sort()
print(line)
