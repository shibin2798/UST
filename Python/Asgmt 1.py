#Q1
num1 = 15
num2 = 24
print("Before swapping: num1=", num1, "num2=", num2)
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("After swapping: num1=", num1, "num2=", num2)



#Q2
initial_cost_100_apples= (100*7.5)
print("Total cost of 100 Apples at Rs.7.5 each: Rs.", initial_cost_100_apples)
initial_cost_50_apples= initial_cost_100_apples/2
print("Total cost of 50 Apples at Rs.7.5 each: Rs.",initial_cost_50_apples)
total_apples_sold = (20*10)+(30*50)
print("Total Apples sold: Rs.",total_apples_sold)
profit = total_apples_sold - initial_cost_50_apples
print("Total profit for selling 50 apples is: Rs.", profit)
new_apples_purchase = profit//7.5
print("Can purchase",new_apples_purchase,"apples")
