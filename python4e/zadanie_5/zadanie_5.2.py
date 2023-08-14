

max = None
min = None

while True:
    snum = input('Enter a number:')
    if snum == ("done"):
        break
    try:
        vnum = int(snum)

        if min is None:
            min = vnum
        elif vnum < min :
            min= vnum

        if max is None:
            max = vnum
        elif vnum > max :
            max = vnum
    except:
        print ('Invalid input')
print ('Minimum is', min)
print ('Maximum is',max)
