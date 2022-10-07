#Check if year is Leap year
leap_yr = int(input("enter the year:"))

if(leap_yr%400 == 0 or (leap_yr%100 !=0 and leap_yr%4==0)):
    print(leap_yr,"is leap year")
else:
    print(leap_yr,"is not leap year")
