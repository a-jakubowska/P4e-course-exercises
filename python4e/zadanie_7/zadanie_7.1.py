
fname = input("Enter file name: ")

fh = open(fname)
#count = 0
#for line in fh:
#    count = count +1
#print(count)


fn=fh.read()
fn=fn.rstrip()
print(fn.upper())
