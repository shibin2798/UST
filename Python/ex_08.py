#Q8

cities={"Charlotte":183,"Tampa":220,"Pittsburgh":222,"Los Angeles":475}
city = int(input("""Please enter your destination:
                1. Charlotte
                2. Tampa
                3. Pittsburgh
                4. Los Angeles\n"""))
days = int(input("Enter no of days:"))
spending_money = int(input("Enter the amount:"))
      
def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    for i in cities:
        res = int(list(cities.keys()).index(i))+1
        if city==res:
            plane_ticket_cost=cities[i]
            break
    return plane_ticket_cost

def rental_car_cost(days):
    if days >= 7:
        car_rental_cost=(40*days)-50
    elif days>=3:
        car_rental_cost=40*days-20
    else:
        car_rental_cost=40*days
    return car_rental_cost

def trip_cost(city,days,spending_money):
    total_trip_cost = int(hotel_cost(days)+ rental_car_cost(days)+ plane_ride_cost(city)+ spending_money)
    print("Total trip cost: $",total_trip_cost)
    
    
    
trip_cost(city,days,spending_money)    
