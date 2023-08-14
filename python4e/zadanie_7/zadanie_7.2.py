

tex=open('zadanie_7.2.txt')

total=0
count=0
for line in tex :
    line=line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        #print (line)
        #pos=line.find('0')
        #print (pos)            #pozycja20
        num=(line[20:])
        num=float(num)

        total=total+num
        count=count+1

print ('Average spam confidence:', total/count)
