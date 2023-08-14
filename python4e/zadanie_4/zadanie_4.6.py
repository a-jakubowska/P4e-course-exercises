
def computepay(h,r):
    if h<=40 :
        p=h*r
        return p
    else :
        ovh= h-40 #amount of overtime
        p=(40*r)+(ovh*(r*1.5))
        return p

hrs = input("Enter Hours:")
h=float(hrs)

rate =input ("Enter rate")
r= float (rate)

p= computepay(h,r)


print ("Pay",p)
