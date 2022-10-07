#Find all prime numbers in a given range

start_range = int(input("Enter start range:"))
end_range = int(input("Enter end range:"))


for x in range (start_range,end_range):
    count = 0
    for y in range (2,(x//2+1)):
        if (x%y)==0:
            count  = count +1
            break
    if (count == 0 and x!=1):
        print(x)
