#Q1
num=int(input("Enter a number:"))


def daysCoversion(num_of_days):
    years=num_of_days//365
    months = (num_of_days-(years*365))//30
    days = (num_of_days - (years*365)-(months*31))
    print("Years:",years)
    print("Months:",months)
    print("Days:",days)
    
        
daysCoversion(num)
                
                
                
    
    
    
    
    
