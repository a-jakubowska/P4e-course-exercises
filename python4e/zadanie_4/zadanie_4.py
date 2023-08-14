
hrs=input("hours")
rate=10.50
try:
    hrs=float(hrs)

    if hrs<=40 :
        pay=hrs*rate
        print(pay)
    else :
        ovh= hrs-40 #amount of overtime
        pay=(40*rate)+(ovh*(rate*1.5))
        print(pay)

except :
    print("Please enter your working hours with a numeric value ")
