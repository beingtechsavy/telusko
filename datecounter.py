days=int(input("enter the date today"))
month=int(input("enter the month now"))
year=int(input("enter the year now"))
if year%4==0:
    if month%2==0:
        if month==2:
            print(29-days,"is the no. of days left") 
        else:
            print(30-days,"is the days left this month")
    elif month%2!=0:
        print(31-days,"is the days left this month")
    elif month==2:
        print(29-days,"is the no. of days left") 
elif year%4!=0:
    if month%2==0:
        if month==2:
            print(28-days,"is the no. of days left") 
        else:
            print(30-days,"is the days left this month")
    elif month%2!=0:
        print(31-days,"is the days left this month")
    elif month==2:
        print(29-days,"is the no. of days left") 