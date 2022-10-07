#Reverse a given number

num = int(input("Enter a number:"))
rev_num = 0
while (num>0):
    num1=num%10
    rev_num =rev_num*10+num1
    print(rev_num)
    num=num//10;
print("Reversed number is",rev_num)
    
