
import re
file=open('example.txt')
lista=list()
sum=list()
suma=int()
for line in file:
    line = line.rstrip()
    number= re.findall('[0-9]+',line)

     #print(number)

     #print(type(number))

    lista = lista + number

#print(lista)

for value in lista:
    sum = int(value)

    suma= suma+sum

print(suma)
